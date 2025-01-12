import unittest
from unittest.mock import patch
from src.app.revendedor.controller import RevendedorController
from src.app.revendedor.model import RevendedorIn, RevendedorOut, RevendedorFilter


class TestRevendedor(unittest.TestCase):

    def setUp(self):
        self.revendedor_controller = RevendedorController()

    @patch('src.app.revendedor.controller.RevendedorController.core_insert')
    @patch('src.system.core.model_core.ModelCore.utils_core')
    async def test_insert_success(self, mock_utils_core, mock_core_insert):
        mock_utils_core.get_password_hash.return_value = "hashed_password"
        mock_core_insert.return_value = RevendedorOut(
            id=1, cpf="12345678900", name="Revendedor Teste", email="teste@exemplo.com"
        )
        data = RevendedorIn(
            cpf="12345678900",
            name="Revendedor Teste",
            email="teste@exemplo.com",
            password="senha123"
        )
        response = await self.revendedor_controller.insert(data)
        self.assertEqual(response.id, 1)
        self.assertEqual(response.cpf, "12345678900")
        self.assertEqual(response.name, "Revendedor Teste")
        self.assertEqual(data.password, "hashed_password")
        mock_utils_core.get_password_hash.assert_called_once_with(password="senha123")
        mock_core_insert.assert_called_once_with(data=data)

    @patch('src.app.revendedor.controller.RevendedorController.core_read')
    async def test_read_success(self, mock_core_read):
        mock_core_read.return_value = [
            RevendedorOut(id=1, cpf="12345678900", name="Revendedor Teste", email="teste@exemplo.com")
        ]
        data = RevendedorFilter(cpf="12345678900")
        response = await self.revendedor_controller.read(data)
        self.assertEqual(len(response), 1)
        self.assertEqual(response[0].cpf, "12345678900")
        self.assertEqual(response[0].name, "Revendedor Teste")
        mock_core_read.assert_called_once_with(data=data)

    @patch('src.app.revendedor.controller.RevendedorController.core_update')
    @patch('src.system.core.model_core.ModelCore.utils_core')
    async def test_update_success(self, mock_utils_core, mock_core_update):
        mock_utils_core.get_password_hash.return_value = "hashed_password"
        mock_core_update.return_value = RevendedorOut(
            id=1, cpf="12345678900", name="Revendedor Atualizado", email="teste@exemplo.com"
        )
        data = RevendedorIn(
            cpf="12345678900",
            name="Revendedor Atualizado",
            email="teste@exemplo.com",
            password="nova_senha"
        )
        response = await self.revendedor_controller.update(id=1, data=data)
        self.assertEqual(response.id, 1)
        self.assertEqual(response.name, "Revendedor Atualizado")
        self.assertEqual(data.password, "hashed_password")
        mock_utils_core.get_password_hash.assert_called_once_with(password="nova_senha")
        mock_core_update.assert_called_once_with(id=1, data=data)

    @patch('src.app.revendedor.controller.RevendedorController.core_delete')
    async def test_delete_success(self, mock_core_delete):
        mock_core_delete.return_value = {"id":1,"detail":"successfully deleted"}
        response = await self.revendedor_controller.delete(id=1)
        self.assertIsNone(response)
        mock_core_delete.assert_called_once_with(id=1)
