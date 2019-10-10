from flask_injector import inject
from be.rawdata.providers.provider import ClientProvider


class Client(object):
    @inject
    # (data_provider=cp)
    def read_client(self, data_provider: ClientProvider) -> str:
        return data_provider.read_client()

    def root(self):
        return "Hello world"

client = Client()
