from .table import Table
from .member import Member
from .book import Book


class IssueStatus(Table):
    _table_name = 'IssueStatus'
    _table_pk = 'issue_id'

    def __init__(self, data: list):
        assert len(data) == 4, f'in {self._table_name}: expected 4 data, got {len(data)}'
        self.issue_id = data[0]
        self.date = data[1]
        self.member_id = data[2]
        self.book_ISBN = data[3]

        self.member = Member.find_via_pk(self.member_id)
        self.book = Book.find_via_pk(self.book_ISBN)

    @classmethod
    def borrowed_books(cls, member_id):
        return [issue_status.book for issue_status in cls.find(dict(member_id=member_id))]

    def update_database(self):
        self.update_via_pk(dict(
            date=self.date,
            member_id=self.member_id,
            book_ISBN=self.book_ISBN
        ), self.issue_id)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.update_database()
