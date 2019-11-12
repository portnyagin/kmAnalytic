# import requests
from be.rawdata.repository.client_repository import ClientRepository
from be.rawdata.domain.domain import client_schemas, client_schema


class ClientProvider(object):
    def get_all(self, clientRepository:ClientRepository):
        clients = clientRepository.get_all()
        return  client_schemas.dump(clients)

    def get_by_id(self,clientRepository:ClientRepository, id):
        client = clientRepository.get_by_id(id)
        return client_schema.dump (client)