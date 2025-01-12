from typing import Annotated
from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordBearer
from fastapi_pagination import Page, add_pagination, paginate


from src.system.core.utils_core import UtilsCore
from src.app.revendedor.controller import RevendedorController
from src.app.revendedor.model import RevendedorFilter, RevendedorIn, RevendedorOut


#CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG-CONFIG#
backend = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

revendedor_controller= RevendedorController()
core_utils = UtilsCore()


#BACKEND-BACKEND-BACKEND-BACKEND-BACKEND-BACKEND-BACKEND-BACKEND-BACKEND-BACKEND-BACKEND-BACKEND-BACKEND-BACKEND-BACKEND-BACKEND-BACKEND-BACKEND-BACKEND-BACKEND#
@backend.get("/revendedor",response_model=Page[RevendedorOut], tags=["REVENDEDOR"])
async def get_revendedor(data:Annotated[RevendedorFilter,Depends()]):  
    result = jsonable_encoder( await revendedor_controller.read(data=data))    
    return paginate(result)

@backend.post("/revendedor",response_model=RevendedorOut, tags=["REVENDEDOR"])
async def post_revendedor(data:RevendedorIn):
    result=jsonable_encoder(await revendedor_controller.insert(data=data))
    return result
    
@backend.patch("/revendedor",response_model=RevendedorOut, tags=["REVENDEDOR"])
async def patch_revendedor(id:int,data:RevendedorIn,token: Annotated[str, Depends(oauth2_scheme)]):
    result=jsonable_encoder(await revendedor_controller.update(id=id,data=data))
    return  result

@backend.delete("/revendedor",response_model={}, tags=["REVENDEDOR"])
async def patch_revendedor(id:int,token: Annotated[str, Depends(oauth2_scheme)]):
    result=jsonable_encoder(await revendedor_controller.delete(id=id))
    return  {"id":id,"detail":"successfully deleted"}



add_pagination(backend)