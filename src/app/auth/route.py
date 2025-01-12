import logging
from typing import  Annotated
from fastapi_pagination import  add_pagination
from fastapi import APIRouter, Depends,  Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from src.app.auth.model import Token
from src.app.auth.controller import AuthController
from src.app.revendedor.model import  RevendedorOut


#CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG#
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")


backend = APIRouter()
auth_controller= AuthController()



#BACKEND-BACKEND-BACKEND-BACKEND-BACKEND-BACKEND-BACKEND-BACKEND-BACKEND-BACKEND-BACKEND-BACKEND-BACKEND-BACKEND-BACKEND-BACKEND-BACKEND-BACKEND-BACKEND-BACKEND#
@backend.get("/auth/me",response_model=RevendedorOut, tags=["AUTH"])
async def get_auth_me(request: Request,token:Annotated[str, Depends( oauth2_scheme)])->RevendedorOut:
    '''
        <h3><b>Para autenticar cadastre um revendedor.</b></h3>
    '''
    result = await auth_controller.get_current_user(token=token)
    return result

@backend.post("/token",response_model=Token, tags=["AUTH"])
async def post_auth_token(request: Request,data: Annotated[OAuth2PasswordRequestForm, Depends()])->Token:
    '''
        <h3><b>Para autenticar cadastre um revendedor.</b></h3>
    '''
    try:
        user = await auth_controller.authenticate_user(data.username, data.password)            
        access_token, expire = auth_controller.create_access_token(data=user)
        return {
            "access_token": access_token,
            "token_type": "bearer",
            "token_expire": expire.strftime("%Y-%m-%d %H:%M"),
        }
    except Exception as error:
        logging.exception(error)
        raise ValueError(
                "Usuário ou senha inválidos."
            )

add_pagination(backend)