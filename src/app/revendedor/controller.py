from typing import List
from src.system.core.model_core import ModelCore
from src.system.core.utils_core import UtilsCore
from src.app.revendedor.model import Revendedor, RevendedorIn, RevendedorOut, RevendedorFilter

# Definições de tabela e modelos
TABLE = Revendedor
TABLEFILTER = RevendedorFilter
TABLEIN = RevendedorIn
TABLEOUT = RevendedorOut

class RevendedorController(ModelCore):    
    def __init__(self) -> None:
        super().__init__()
        self.utils_core = UtilsCore()
        self.TABLE = TABLE
        self.TABLEFILTER = TABLEFILTER
        self.TABLEIN = TABLEIN
        self.TABLEOUT = TABLEOUT

    async def insert(self, data: TABLEIN) -> TABLEOUT:
        """
        Insere um novo registro no banco de dados após aplicar a regra de status.
        """
        try:
            if data.password:
                data.password = self.utils_core.get_password_hash(password=data.password)
            data = await self.core_insert(data=data)
            return data
        except Exception as error:
            raise Exception(f"Erro ao inserir registro: {error}")

    async def read(self, data: TABLEFILTER) -> List[TABLEOUT]:
        """
        Lê registros do banco de dados com base nos filtros fornecidos.
        """
        try:
            data = await self.core_read(data=data)
            return data
        except Exception as error:
            raise Exception(f"Erro ao ler registros: {error}")

    async def update(self, id: int, data: TABLEIN) -> TABLEOUT:
        """
        Atualiza um registro no banco de dados após aplicar a regra de status.
        """
        try:
            if data.password:
                data.password = self.utils_core.get_password_hash(password=data.password)
            data = await self.core_update(id=id, data=data)
            return data
        except Exception as error:
            raise Exception(f"Erro ao atualizar registro com ID {id}: {error}")

    async def delete(self, id: int):
        """
        Exclui um registro do banco de dados.
        """
        try:
            data = await self.core_delete(id=id)
            return data
        except Exception as error:
            raise Exception(f"Erro ao excluir registro com ID {id}: {error}")
        
