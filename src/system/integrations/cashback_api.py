import os
import requests
from tenacity import retry, stop_after_attempt, wait_fixed
from typing import Any, Dict

from src.app.cashback.model import CashbackOut

class CashbackAPI:
    def __init__(self):
        """
        Inicializa a classe CashbackAPI com a URL base e o token.

        Args:
            base_url (str): URL base da API externa.
            token (str): Token de autenticação necessário para as requisições.
        """
        self.base_url = os.environ.get("BASE_URL_CASHBACK","https://mdaqk8ek5j.execute-api.us-east-1.amazonaws.com/")
        self.token = os.environ.get("TOKEN_CASHBACK","ZXPURQOARHiMc6Y0flhRC1LVlZQVFRnm")

    #@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
    async def get_cashback(self, cpf: str = "12312312323") -> CashbackOut:
        """
        Consulta o cashback de um CPF na API externa com retry configurado.

        Args:
            cpf (str): CPF do revendedor a ser consultado.

        Returns:
            CashbackOut: Dados retornados pela API em formato de dicionário.
        """
        url = f"{self.base_url}/v1/cashback?cpf={cpf}"
        headers = {"token": self.token}
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Lança uma exceção para status de erro HTTP
        return response.json()  # Retorna os dados no formato JSON
