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
