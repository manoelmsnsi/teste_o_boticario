from src.app.cashback.model import CashbackOut
from src.system.integrations.cashback_api import CashbackAPI


class CashbackController():    
    def __init__(self):
        self.cashback_api = CashbackAPI()
    async def get_cashback(self) -> CashbackOut:
        """
        Insere um novo registro no banco de dados após aplicar a regra de status.
        """
        try:            
            data = await self.cashback_api.get_cashback()
            return data
        except Exception as error:
            raise Exception(f"Erro ao Consultar CACHEBACK: {error}")
