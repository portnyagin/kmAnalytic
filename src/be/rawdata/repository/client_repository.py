from be.rawdata.domain.domain import Client
from be.rawdata.repository.csv_reader import CsvReader


class ClientRepository:
    SRC_FILE_PATH = "CLIENTS.csv"

    def __init__(self):
        reader = CsvReader()
        _, data = reader.process(self.SRC_FILE_PATH, ['ID клиента', 'Тип клиента', 'Признак ИП'])
        # self.clients = [Client.newClient(*row) for row in data]
        self.clients = []
        for row in data:
            self.clients.append(Client(*row))

    def get_by_id(self, _id):
        # TODO: Find more effective decision. Current code is straightforward
        return next(cl for cl in self.clients if cl.id == _id)


    def get_all(self):
        return self.clients
