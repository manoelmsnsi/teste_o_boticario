from typing import List
from src.system.core.model_core import ModelCore
from src.app.revendedor.model import RevendedorFilter
from src.app.revendedor.controller import RevendedorController
from src.app.compra.model import Compra, CompraInBff, CompraOut, CompraFilter

# Definições de tabela e modelos
TABLE = Compra
TABLEFILTER = CompraFilter
TABLEIN = CompraInBff
TABLEOUT = CompraOut

class CompraController(ModelCore):    
    def __init__(self) -> None:
        super().__init__()
        self.revendedor = RevendedorController()
        self.TABLE = TABLE
        self.TABLEFILTER = TABLEFILTER
        self.TABLEIN = TABLEIN
        self.TABLEOUT = TABLEOUT

    async def insert(self, data: TABLEIN) -> TABLEOUT:
        """
        Insere um novo registro no banco de dados após aplicar a regra de status.
        """
        try:
            revendedor = await self.revendedor.read(data=RevendedorFilter(id=data.revendedor_id))
            if len(revendedor) == 0:
                raise Exception(f"Revendedor com ID {data.revendedor_id} não encontrado.")
            data.status = await self.regra_status(cpf=revendedor[0].cpf)
            data.cashback = await self.regra_cashback(valor=data.valor)
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
            revendedor = await self.revendedor.read(data=RevendedorFilter(id=data.revendedor_id))
            if len(revendedor) == 0:
                raise Exception(f"Revendedor com ID {data.revendedor_id} não encontrado.")
            data.status = await self.regra_status(cpf=revendedor[0].cpf)
            data.cashback = await self.regra_cashback(valor=data.valor)
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
    
    async def regra_status(self, cpf:str):
        """
        Define a regra para o campo 'status' com base no CPF do revendedor.
        """
        if cpf == "15350946056":
            status = "Aprovado"
        else:
            status = "Em validação"
        return status

    async def regra_cashback(self, valor: float):
        """
        Define a regra para o campo 'Cashback' com base no VALOR da compra.
        """
        if valor <= 1000:
            cash_back = "10%"
        elif valor <= 1500:
            cash_back = "15%"
        else:
            cash_back = "20%"
        return cash_back
