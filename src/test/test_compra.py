import unittest
from unittest.mock import patch
from src.app.revendedor.model import RevendedorFilter
from src.app.compra.controller import CompraController


class TestCompra(unittest.TestCase):

    def setUp(self):
        self.compra_controller = CompraController()

    @patch('src.app.revendedor.controller.RevendedorController.read')
    @patch('src.app.compra.controller.CompraController.core_insert')
    async def test_insert_success(self, mock_core_insert, mock_revendedor_read):
        mock_revendedor_read.return_value = [{"cpf": "15350946056"}]
        mock_core_insert.return_value = {
            "id": 1,
            "status": "Aprovado",
            "cashback": "10%"
        }
        data = {
            "revendedor_id": 1,
            "valor": 500
        }
        response = await self.compra_controller.insert(data)
        self.assertEqual(response["status"], "Aprovado")
        self.assertEqual(response["cashback"], "10%")
        mock_revendedor_read.assert_called_once_with(data=RevendedorFilter(id=1))
        mock_core_insert.assert_called_once_with(data=data)

    @patch('src.app.compra.controller.CompraController.core_read')
    async def test_read_success(self, mock_core_read):
        mock_core_read.return_value = [{"id": 1, "status": "Aprovado"}]
        data = {"status": "Aprovado"}
        response = await self.compra_controller.read(data)
        self.assertEqual(len(response), 1)
        self.assertEqual(response[0]["status"], "Aprovado")
        mock_core_read.assert_called_once_with(data=data)

    @patch('src.app.revendedor.controller.RevendedorController.read')
    @patch('src.app.compra.controller.CompraController.core_update')
    async def test_update_success(self, mock_core_update, mock_revendedor_read):
        mock_revendedor_read.return_value = [{"cpf": "12345678900"}]
        mock_core_update.return_value = {
            "id": 1,
            "status": "Em validação",
            "cashback": "15%"
        }
        data = {
            "revendedor_id": 2,
            "valor": 1200
        }
        response = await self.compra_controller.update(1, data)
        self.assertEqual(response["status"], "Em validação")
        self.assertEqual(response["cashback"], "15%")
        mock_revendedor_read.assert_called_once_with(data=RevendedorFilter(id=2))
        mock_core_update.assert_called_once_with(id=1, data=data)

    @patch('src.app.compra.controller.CompraController.core_delete')
    async def test_delete_success(self, mock_core_delete):
        mock_core_delete.return_value = {"id":1,"detail":"successfully deleted"}
        response = await self.compra_controller.delete(1)
        self.assertTrue({"id":1,"detail":"successfully deleted"})
        mock_core_delete.assert_called_once_with(id=1)

    async def test_regra_status(self):
        status_aprovado = await self.compra_controller.regra_status("15350946056")
        status_em_validacao = await self.compra_controller.regra_status("12345678900")
        self.assertEqual(status_aprovado, "Aprovado")
        self.assertEqual(status_em_validacao, "Em validação")

    async def test_regra_cashback(self):
        cashback_10 = await self.compra_controller.regra_cashback(500)
        cashback_15 = await self.compra_controller.regra_cashback(1200)
        cashback_20 = await self.compra_controller.regra_cashback(2000)
        self.assertEqual(cashback_10, "10%")
        self.assertEqual(cashback_15, "15%")
        self.assertEqual(cashback_20, "20%")
