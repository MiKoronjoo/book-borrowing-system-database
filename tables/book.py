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

    def update_database(self):
        self.update_via_pk(dict(
            title=self.title,
            category=self.category,
            price=self.price,
            author=self.author,
            publisher=self.publisher,
            status=self.status
        ), self.ISBN)

    @classmethod
    def delete_via_pk(cls, pk: str) -> None:
        from .issue_status import IssueStatus
        from .return_status import ReturnStatus
        super().delete_via_pk(pk)
        for status in IssueStatus.find(dict(book_ISBN=pk)):
            status: IssueStatus
            status.delete()
        for returned in ReturnStatus.find(dict(book_ISBN=pk)):
            returned: ReturnStatus
            returned.delete()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.update_database()
