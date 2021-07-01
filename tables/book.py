from .table import Table


class Book(Table):
    _table_name = 'Books'
    _table_pk = 'ISBN'

    def __init__(self, data: list):
        assert len(data) == 7, f'in {self._table_name}: expected 7 data, got {len(data)}'
        self.ISBN = data[0]
        self.title = data[1]
        self.category = data[2]
        self.price = data[3]
        self.author = data[4]
        self.publisher = data[5]
        self.status = data[6]
