from flask_injector import inject
from be.rawdata.providers.provider import ClientProvider
from be.rawdata.repository.client_repository import ClientRepository
import json
from flask import jsonify


class Client(object):
    @inject
    # (data_provider=cp)
    def read_client(self, data_provider: ClientProvider) -> str:
        return data_provider.read_client()

    # @staticmethod
    @inject
    def read_all(self, data_provider: ClientProvider, client_repo: ClientRepository) -> list:
        return jsonify(data_provider.get_all(client_repo))


client = Client()
