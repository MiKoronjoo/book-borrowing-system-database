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

    def update_database(self):
        self.update_via_pk(dict(
            name=self.name,
            age=self.age,
            address=self.address,
            registration_date=self.registration_date,
            max_credit=self.max_credit
        ), self.ID)

    @classmethod
    def delete_via_pk(cls, pk: str) -> None:
        from .issue_status import IssueStatus
        from .return_status import ReturnStatus
        super().delete_via_pk(pk)
        for status in IssueStatus.find(dict(member_id=pk)):
            status: IssueStatus
            status.delete()
        for returned in ReturnStatus.find(dict(member_id=pk)):
            returned: ReturnStatus
            returned.delete()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.update_database()
