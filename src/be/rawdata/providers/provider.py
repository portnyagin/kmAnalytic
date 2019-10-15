# import requests
from be.rawdata.repository.client_repository import ClientRepository


client = {
    "id": "123",
    "type": "1",
    "last_name": "Ivanov"
}


class ClientProvider(object):

    def read_client(self) -> str:
        return client, 200

    def get_all(self, clientRepository:ClientRepository):
        return clientRepository.get_all()

    def get_by_id(self, id):
        pass