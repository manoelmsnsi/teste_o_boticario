from typing import Annotated
from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordBearer
from fastapi_pagination import Page, add_pagination, paginate

from src.app.compra.controller import CompraController
from src.app.compra.model import CompraFilter, CompraIn, CompraInBff, CompraOut


#CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG#
backend = APIRouter()

compra_controller= CompraController()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")



#BACKEND-BACKEND-BACKEND-BACKEND-BACKEND-BACKEND-BACKEND-BACKEND-BACKEND-BACKEND-BACKEND-BACKEND-BACKEND-BACKEND-BACKEND-BACKEND-BACKEND-BACKEND-BACKEND-BACKEND#
@backend.get("/compra",response_model=Page[CompraOut], tags=["COMPRA"])
async def get_compra(data:Annotated[CompraFilter,Depends()],token: Annotated[str, Depends(oauth2_scheme)]):  
    result = jsonable_encoder( await compra_controller.read(data=data))    
    return paginate(result)

@backend.post("/compra",response_model=CompraOut, tags=["COMPRA"])
async def post_compra(data:CompraIn,token: Annotated[str, Depends(oauth2_scheme)]):
    result = jsonable_encoder(await compra_controller.insert(data=CompraInBff(**data.model_dump())))
    return result
    
@backend.patch("/compra",response_model=CompraOut, tags=["COMPRA"])
async def patch_compra(id:int,data:CompraIn,token: Annotated[str, Depends(oauth2_scheme)]):
    result=jsonable_encoder(await compra_controller.update(id=id,data=CompraInBff(**data.model_dump())))
    return  result

@backend.delete("/compra",response_model={}, tags=["COMPRA"])
async def patch_compra(id:int,token: Annotated[str, Depends(oauth2_scheme)]):
    result=jsonable_encoder(await compra_controller.delete(id=id))
    return  {"id":id,"detail":"successfully deleted"}



add_pagination(backend)