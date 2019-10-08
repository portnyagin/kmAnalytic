from flask_injector import inject
from be.rawdata.providers.provider import ClientProvider


@inject(data_provider=ClientProvider)
def read_client(data_provider) -> str:
    return data_provider.read_product()