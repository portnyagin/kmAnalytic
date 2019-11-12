import csv
from operator import itemgetter


class CsvReader:
    # TODO logger
    # TODO move to relative path

    BASE_PATH = "/home/portnyagin/sources/portnyagin/kmAnalytic/src/be/rawdata/data/"

    def __init__(self):
        pass

    def make_meta(self, header, column_list=None, index_list=None):
        meta = {}
        if column_list is None and index_list is None:
            meta = {v: k for k, v in enumerate(header)}
        elif column_list is not None:
            for c in column_list:
                try:
                    ind = header.index(c)
                    meta[c] = ind
                except ValueError:
                    continue
        elif index_list is not None:
            meta = {header[ind]: ind for ind in index_list}
        return meta

    def process(self, file_name, column_list=None, index_list=None):
        # TODO check file exist
        # TODO tests
        meta = {}
        data = []
        with open(self.BASE_PATH + file_name) as f:
            reader = csv.reader(f)
            meta = self.make_meta(next(reader), column_list, index_list)

            for row in reader:
                data.append(list(itemgetter(*meta.values())(row)))
        return meta, data