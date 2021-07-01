import sqlite3

from config import DB_PATH


def create_database():
    with open('schema.sql') as fp:
        queries = fp.read().strip().strip(';').split(';')
    for query in queries:
        exe_query(query)


def exe_query(query, args=()):
    con_obj = sqlite3.connect(DB_PATH)
    courser = con_obj.execute(query, args)
    result = courser.fetchall()
    con_obj.commit()
    con_obj.close()
    return result


if __name__ == '__main__':
    create_database()
