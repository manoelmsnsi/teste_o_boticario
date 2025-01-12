from typing import Annotated
from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordBearer

from src.app.cashback.model import CashbackOut
from src.app.cashback.controller import CashbackController


#CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG#
backend = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

cashback_controller= CashbackController()


#BACKEND-BACKEND-BACKEND-BACKEND-BACKEND-BACKEND-BACKEND-BACKEND-BACKEND-BACKEND-BACKEND-BACKEND-BACKEND-BACKEND-BACKEND-BACKEND-BACKEND-BACKEND-BACKEND-BACKEND#
@backend.get("/cashback",response_model=CashbackOut, tags=["CACHEBACK"])
async def get_cashback(token: Annotated[str, Depends(oauth2_scheme)]):  
    result = jsonable_encoder( await cashback_controller.get_cashback())    
    return result


