from unittest import TestCase
from unittest.mock import  patch, mock_open
from be.rawdata.repository.csv_reader import CsvReader


class TestCsvReader_meta(TestCase):
    def setUp(self) -> None:
        self.reader = CsvReader()
        self.header = ["col 1", "col 2", "col 3"]


    def test_make_meta1(self):
        def test_make_meta1(self):
            self.assertDictEqual(self.reader.make_meta(self.header), {"col 1": 0, "col 2": 1, "col 3": 2},
                                 "test_make_meta1 failed")

    def test_make_meta2(self):
        self.assertDictEqual(self.reader.make_meta(self.header, ["col 2"]), {"col 2": 1},
                             "test_make_meta2 failed")

    def test_make_meta3(self):
        self.assertDictEqual(self.reader.make_meta(self.header, ["col 3","col 1"]), {"col 1": 0, "col 3": 2},
                             "test_make_meta3 failed")

    def test_make_meta4(self):
        self.assertDictEqual(self.reader.make_meta(self.header, ["col 4","col 1"]), {"col 1": 0},
                             "test_make_meta4 failed")

    def test_make_meta5(self):
        self.assertDictEqual(self.reader.make_meta(self.header, [1,2]), {},
                             "test_make_meta5 failed")

    def test_make_meta6(self):
        self.assertDictEqual(self.reader.make_meta(self.header, index_list=[1,2]), {"col 2": 1, "col 3": 2},
                             "test_make_meta6 failed")

    def test_make_meta7(self):
        self.assertDictEqual(self.reader.make_meta(['col 1', 'col 2', 'col 3'],
                                                   ['col 1']),
                             {"col 1": 0},
                             "test_make_meta7 failed")


class TestCsvReader_process(TestCase):
    def setUp(self) -> None:
        self.reader = CsvReader()

    @patch('builtins.open', new_callable=mock_open, read_data='"col 1","col 2","col 3"\n' \
                                                              '"1","2","3"\n' \
                                                              '"4","5","6"'
           )
    def test_process1(self, m):
        meta, data = self.reader.process("", column_list=["col 1"])

        self.assertListEqual(data, [['1'], ['4']])

    @patch('builtins.open', new_callable=mock_open, read_data='"col 1","col 2","col 3"\n' \
                                                              '"1","2","3"\n' \
                                                              '"4","5","6"'
           )
    def test_process2(self, m):
        meta, data = self.reader.process("", column_list=["col 1", "col 3"])

        self.assertListEqual(data, [['1', '3'], ['4', '6']])