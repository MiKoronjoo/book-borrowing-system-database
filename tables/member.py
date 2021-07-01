from .table import Table


class Member(Table):
    _table_name = 'Members'
    _table_pk = 'ID'

    def __init__(self, data: list):
        assert len(data) == 6, f'in {self._table_name}: expected 6 data, got {len(data)}'
        self.ID = data[0]
        self.name = data[1]
        self.age = data[2]
        self.address = data[3]
        self.registration_date = data[4]
        self.max_credit = data[5]
