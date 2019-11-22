from be.rawdata.service.domain.domain import clientInit
from be.rawdata.service.repository.csv_reader import CsvReader


class ClientRepository:
    SRC_FILE_PATH = "CLIENTS.csv"

    def __init__(self):
        reader = CsvReader()
        _, data = reader.process(self.SRC_FILE_PATH, ['ID клиента', 'Тип клиента', 'Признак ИП'])
        # self.clients = [Client.newClient(*row) for row in data]
        self.clients = []
        for row in data:
            cl = clientInit()
            cl["id"] = row[0]
            cl["is_ip"] = row[1]
            cl["is_ip"] = row[2]
            self.clients.append(cl)

    def get_by_id(self, _id):
        # TODO: Find more effective decision. Current code is straightforward
        return next(cl for cl in self.clients if cl.id == _id)


    def get_all(self):
        return self.clients

