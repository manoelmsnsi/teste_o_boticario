import sqlalchemy
from typing import Optional
from datetime import datetime
from pydantic import BaseModel
from sqlalchemy.orm import relationship,Mapped
from sqlalchemy.ext.declarative import declarative_base

from src.app.revendedor.model import Revendedor, RevendedorOut


metadata = sqlalchemy.MetaData()
Base = declarative_base()

class Compra(Base):
    __tablename__ = "app_compra"
    metadata

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    codigo = sqlalchemy.Column(sqlalchemy.Integer)
    valor = sqlalchemy.Column(sqlalchemy.Float)
    status = sqlalchemy.Column(sqlalchemy.String)
    cashback = sqlalchemy.Column(sqlalchemy.String)
    revendedor_id :Mapped[int] = sqlalchemy.Column(sqlalchemy.Integer,sqlalchemy.ForeignKey(Revendedor.id))
    revendedor:Mapped[RevendedorOut] = relationship(Revendedor, foreign_keys=[revendedor_id],lazy='joined')

    create_at = sqlalchemy.Column(sqlalchemy.DateTime,default=datetime.now)
    update_at = sqlalchemy.Column(sqlalchemy.DateTime)
    deleted_at = sqlalchemy.Column(sqlalchemy.DateTime)   


class CompraIn(BaseModel):
    codigo : Optional[int]
    valor : Optional[float]
    revendedor_id : Optional[int]    
    
class CompraInBff(BaseModel):
    codigo : Optional[int]
    valor : Optional[float]
    revendedor_id : Optional[int]
    status : Optional[str] = None
    cashback : Optional[str] = None

    
class CompraOut(CompraInBff):
    id : int = None
    revendedor: Optional[RevendedorOut] = None

    create_at:datetime
    class Config:
        from_attributes = True


class CompraFilter(BaseModel):
    id: Optional[int] = None
    revendedor_id: Optional[int] = None
    
