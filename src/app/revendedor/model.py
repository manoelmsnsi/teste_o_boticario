import sqlalchemy
from typing import Optional
from datetime import datetime
from pydantic import BaseModel,EmailStr, field_validator
from sqlalchemy.ext.declarative import declarative_base

from src.app.revendedor.validation import create_at_to_str, validar_cpf


metadata = sqlalchemy.MetaData()
Base = declarative_base()

class Revendedor(Base):
    __tablename__ = "app_revendedor"
    metadata

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    full_name = sqlalchemy.Column(sqlalchemy.String)
    username = sqlalchemy.Column(sqlalchemy.String)
    password = sqlalchemy.Column(sqlalchemy.String)
    cpf = sqlalchemy.Column(sqlalchemy.String)
    email = sqlalchemy.Column(sqlalchemy.String)
    phone = sqlalchemy.Column(sqlalchemy.String)

    create_at = sqlalchemy.Column(sqlalchemy.DateTime,default=datetime.now)
    update_at = sqlalchemy.Column(sqlalchemy.DateTime)
    deleted_at = sqlalchemy.Column(sqlalchemy.DateTime)   


class RevendedorIn(BaseModel):
    full_name : Optional[str] = None
    username : Optional[str] = None
    password : Optional[str] = None
    cpf : Optional[str] = None
    email : Optional[EmailStr] = None
    phone : Optional[str] = None  
     
    @field_validator('cpf', mode="after")
    def validar(cls,cpf):
        return validar_cpf(cpf=cpf)
    
class RevendedorOut(BaseModel):
    id : int = None
    full_name : Optional[str] = None
    username : Optional[str] = None
    cpf : Optional[str] = None
    email : Optional[EmailStr] = None
    phone : Optional[str] = None  
    create_at:str
    create_at: Optional[str] = None
    @field_validator("create_at",mode="before")
    def validar(cls, create_at):
        return create_at_to_str(data=create_at)
   
    class Config:
        from_attributes = True


class RevendedorFilter(BaseModel):
    id: Optional[int] = None
    cpf: Optional[int] = None
    username: Optional[str] = None
    
