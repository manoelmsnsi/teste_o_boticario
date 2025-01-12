import unittest
from unittest.mock import patch, Mock
from src.app.cashback.controller import CashbackController
from src.app.cashback.model import CashbackCreditOut, CashbackOut


class TestCashback(unittest.TestCase):

    def setUp(self):
        self.cashback_api = CashbackController()

    @patch('src.system.integrations.cashback_api.get_cashback')
    async def test_get_cashback_success(self, mock_request):
        mock_response = Mock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = CashbackOut(statusCode=200,body=CashbackCreditOut(credit=2000))

    
        response = await self.cashback_api.get_cashback()
        
        self.assertEqual(response.statusCode, 200)
        self.assertEqual(response.body.credit, 2000)
        