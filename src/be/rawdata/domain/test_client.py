from unittest import TestCase
from be.rawdata.domain.domain import Client

class TestClient(TestCase):
    def setUp(self) -> None:
        pass

    def test_client(self):
        print ("sds")
        cl = Client()

        cl.id = 1
        # self.assertEquals(cl.id, 1)


    pass
