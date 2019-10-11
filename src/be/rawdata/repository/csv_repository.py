from be.rawdata.domain.domain import Client


class csvReader:

    def __init__(self, file_name):
        self._file_name = file_name

    def process(self):
        pass

    def


class ClientRepository:
    SRC_FILE_PATH="./be/rawdata/data/CLIENTS.csv"
    def __init__(self):
        self.clients = []

    def add(self, Client):
        self.clients.append(Client)

    def get_by_id (self, _id):
        # TODO: Find more effective decision. Current code is straightforward
        return next(cl for cl in self.clients if cl.id == _id)

    def get_all(self):
        return  self.clients