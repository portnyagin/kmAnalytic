from be.rawdata.domain.domain import Client






class ClientRepository:
    SRC_FILE_PATH="CLIENTS.csv"
    def __init__(self):
        self.clients = []

    def add(self, Client):
        self.clients.append(Client)

    def get_by_id (self, _id):
        # TODO: Find more effective decision. Current code is straightforward
        return next(cl for cl in self.clients if cl.id == _id)

    def get_all(self):
        return  self.clients