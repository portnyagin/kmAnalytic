class Client:
    def __init__(self):
        self._id = None
        self._type = None
        self._is_ip = None
        pass

    def get_id(self): return self._id
    def get_type(self): return self._type
    def get_is_ip(self): return self._is_ip

    def set_id(self, val):  self._id = val
    def set_type(self, val): self._type = val
    def set_is_ip(self, val): self._is_ip = val

    id = property(get_id, set_id)
    type = property(get_type, set_type)
    is_ip = property(get_is_ip, set_is_ip)