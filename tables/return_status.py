from .table import Table
from .issue_status import IssueStatus
from .member import Member
from .book import Book


class ReturnStatus(Table):
    _table_name = 'ReturnStatus'
    _table_pk = 'return_id'

    def __init__(self, data: list):
        assert len(data) == 5, f'in {self._table_name}: expected 5 data, got {len(data)}'
        self.return_id = data[0]
        self.issue_id = data[1]
        self.date = data[2]
        self.member_id = data[3]
        self.book_ISBN = data[4]

        self.issue_status = IssueStatus.find_via_pk(self.issue_id)
        self.member = Member.find_via_pk(self.member_id)
        self.book = Book.find_via_pk(self.book_ISBN)

    @classmethod
    def returned_books(cls, member_id):
        return [return_status.book for return_status in cls.find(dict(member_id=member_id))]

    def update_database(self):
        self.update_via_pk(dict(
            issue_id=self.issue_id,
            date=self.date,
            member_id=self.member_id,
            book_ISBN=self.book_ISBN
        ), self.return_id)

    def delete(self):
        self.delete_via_pk(self.return_id)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.update_database()
