from calendar import c
from src.app.cashback.model import CashbackOut
from src.system.integrations.cashback_api import CashbackAPI
from src.system.core.utils_core import UtilsCore


class CashbackController():    
    def __init__(self):
        self.cashback_api = CashbackAPI()
        self.utils_core = UtilsCore()
    async def get_cashback(self,token) -> CashbackOut:
        """
        Insere um novo registro no banco de dados após aplicar a regra de status.
        """
        try:
            data=self.utils_core.token_decode(token=token)
            data = await self.cashback_api.get_cashback(cpf=data.get("cpf",None))
            return data
        except Exception as error:
            raise Exception(f"Erro ao Consultar CASHBACK: {error}")
