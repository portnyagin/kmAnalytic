# import requests

client = {
    "id": "123",
    "type": "1",
    "last_name": "Ivanov"
}


class ClientProvider(object):

    def read_client(self) -> str:
        return client, 200