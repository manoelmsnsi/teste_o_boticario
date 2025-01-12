from datetime import datetime
from sqlalchemy import update
from sqlalchemy.sql import select

from src.system.core.database import Database

class ModelCore():
    def __init__(self) -> None:
        self.service_database = Database()
        self.TABLE = ""
        self.TABLEFILTER = ""
        self.TABLEIN = ""
        self.TABLEOUT = ""
 
    async def core_insert(self,data)-> dict:
        try:
            async with self.service_database.conexao() as session:
                data = self.TABLE(**data.__dict__)
                session.add(data)
                await session.commit()
                await session.refresh(data)
                 
            return data
        except Exception as error:
            raise Exception(f"{error}")
            
    async def core_read(self,data):
        try:
            filter = data.model_dump(by_alias=True, exclude_none=True)
            async with self.service_database.conexao() as session:                
                stmt = select(self.TABLE).filter_by(**filter, deleted_at = None).order_by(self.TABLE.id.desc())                
                result = await session.execute(stmt)
                result = result.scalars().all()
            return result
        except Exception as error:
            raise Exception(f"{error}")

    async def core_update(self,id,data):
        try:
            data = data.model_dump(by_alias=True, exclude_none=True)
            data["update_at"]=datetime.now()
            data["deleted_at"]=None
            async with self.service_database.conexao() as session:               
                stmt = update(self.TABLE).where(self.TABLE.id == id).values(data).returning(self.TABLE)
                result = await session.execute(stmt)
                updated_record = result.scalars().first()
                await session.commit()
                result = await self.core_read(self.TABLEFILTER(id=id))
                if not updated_record:
                    raise ValueError(f"Registro com ID {id} não encontrado.")
            return result[0]
        except Exception as error:
            raise Exception(f"{error}")
        
    async def core_delete(self,id):
        try:            
            async with self.service_database.conexao() as session:
                stmt = update(self.TABLE).where(self.TABLE.id == id).values({"deleted_at":datetime.now()}).returning(self.TABLE)
                result = await session.execute(stmt)
                await session.commit()
                result = await self.core_read(self.TABLEFILTER(id=id))           
            return result
        except Exception as error:
            raise Exception(f"{error}")

    