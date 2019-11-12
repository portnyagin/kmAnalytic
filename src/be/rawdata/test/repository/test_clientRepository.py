from unittest import TestCase
from be.rawdata.repository.client_repository import ClientRepository
from be.rawdata.domain.domain import  Client

class TestClientRepository(TestCase):
    def setUp(self) -> None:
        self.repository = ClientRepository()
        cl = Client()
        cl.id = 1
        cl.is_ip = 0
        cl.type = 1
        self.repository.add(cl)


    def test_get_by_id(self):
        cl = Client()
        cl.id = 2
        cl.is_ip = 0
        cl.type = 1
        self.repository.add(cl)

        self.assertEqual(self.repository.get_by_id(2),cl, "ClientReposittory.get_by_id (2) is failed")
