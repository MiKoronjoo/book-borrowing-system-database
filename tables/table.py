import sqlite3
from config import DB_PATH


class Table:
    _table_name = ''
    _table_pk = ''

    @classmethod
    def insert(cls, document: dict) -> None:
        con_obj = sqlite3.connect(DB_PATH)
        columns = ', '.join(f'"{c}"' for c in document.keys())
        val_str = ', '.join('?' for _ in document.values())
        query = f'INSERT INTO {cls._table_name}({columns}) VALUES({val_str})'
        con_obj.execute(query, list(document.values()))
        con_obj.commit()
        con_obj.close()

    @classmethod
    def find_via_pk(cls, pk: str) -> 'Table':
        con_obj = sqlite3.connect(DB_PATH)
        query = f'SELECT * FROM {cls._table_name} WHERE "{cls._table_pk}" = ?'
        courser = con_obj.execute(query, (pk,))
        result = courser.fetchall()
        con_obj.commit()
        con_obj.close()
        if result:
            return cls(result[0])

    @classmethod
    def update_via_pk(cls, update: dict, pk: str) -> None:
        con_obj = sqlite3.connect(DB_PATH)
        columns = ', '.join(f'"{c}" = ?' for c in update.keys())
        query = f'UPDATE {cls._table_name} SET {columns} WHERE "{cls._table_pk}" = {pk}'
        con_obj.execute(query, list(update.values()))
        con_obj.commit()
        con_obj.close()

    @classmethod
    def delete_via_pk(cls, pk: str) -> None:
        con_obj = sqlite3.connect(DB_PATH)
        query = f'DELETE FROM {cls._table_name} WHERE "{cls._table_pk}" = ?'
        con_obj.execute(query, (pk,))
        con_obj.commit()
        con_obj.close()

    @classmethod
    def find(cls, _filter: dict):
        con_obj = sqlite3.connect(DB_PATH)
        if not _filter:
            condition = '1 = 1'
        else:
            condition = ' AND '.join(f'"{col}" = ?' for col in _filter.keys())
        cursor = con_obj.execute(f'SELECT * FROM {cls._table_name} WHERE {condition}', list(_filter.values()))
        selected_table = cursor.fetchall()
        con_obj.close()
        return [cls(data) for data in selected_table]
