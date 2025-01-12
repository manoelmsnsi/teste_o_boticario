import os
import pytz
import logging
from jose import jwt
from fastapi import Depends
from typing import Annotated
from pydantic import BaseModel
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta, timezone

from src.app.auth.model import TokenData
from src.app.revendedor.model import RevendedorFilter
from src.app.revendedor.controller import RevendedorController


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")
class AuthController():    
    def __init__(self) -> None:
        self.revendedor_controller=RevendedorController()
 
        self.ALGORITHM = os.environ.get("ALGORITHM", "HS256")
        self.ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES", 15))
        self.SECRET_KEY = os.environ.get("SECRET_KEY", "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7")
        self.TIMEZONE = pytz.timezone('America/Sao_Paulo')
    
    async def authenticate_user(self,username: str, password: str):
        user = await self.get_revendedor_auth(username)
        hashed = self.get_password_hash(password=password)
        if not user:
            return False
        if not await self.verify_password(password, user.password):
            return False
        return user
    
    async def get_current_user(self,token: Annotated[str, Depends(oauth2_scheme)]):
        try:
            payload = await self.token_access_decode(token=token)
            username: str = payload.get("username")
            token_data = TokenData(username=username)
            user = await self.get_revendedor_auth(username=token_data.username)
            if user is None:
                raise ValueError(
                    "Não foi possivel validar suas credenciais.",
                )
            return user
        except Exception:
            raise ValueError(
                "Não foi possivel validar suas credenciais.",
            )
    
    def create_access_token(self,data:BaseModel):
        to_encode = {
                        "full_name":data.full_name,
                        "email":data.email,
                        "phone":data.phone
                        
                    }
        expire = datetime.now(timezone.utc) + timedelta(minutes=self.ACCESS_TOKEN_EXPIRE_MINUTES)
        expire = expire.astimezone(self.TIMEZONE)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, self.SECRET_KEY, algorithm=self.ALGORITHM)
        return encoded_jwt, expire

    async def verify_password(self,plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)
    
    async def token_access_decode(self,token: str):
        try:
            data = jwt.decode(token, self.SECRET_KEY, algorithms=[self.ALGORITHM])            
            return data
        except:
            raise ValueError(
                "Não Autorizado.",
            ) 
    
    def get_password_hash(self,password):
        return pwd_context.hash(password) 
    
    async def get_revendedor_auth(self,username):
        routes = []
        try:
          
            user_result = await self.revendedor_controller.read(data=RevendedorFilter(username=username))
            user_result=user_result[0]
            return user_result
        except Exception as error:
            logging.exception(error)
            raise ValueError(
                "Não foi possivel validar suas credenciais.."
            )