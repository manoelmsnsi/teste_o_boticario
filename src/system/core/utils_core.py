
import os
import jwt
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
class UtilsCore():    
    def __init__(self) -> None:
        self.ALGORITHM = os.environ.get("ALGORITHM", "HS256")
        self.ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES", 15))
        self.SECRET_KEY = os.environ.get("SECRET_KEY", "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7")

    def get_password_hash(self,password):
        return pwd_context.hash(password) 
    def token_decode(self,token):
        data = jwt.decode(token, self.SECRET_KEY, algorithms=[self.ALGORITHM])
        return data