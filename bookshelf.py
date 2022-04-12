import os
import psycopg2
from dotenv import load_dotenv

import sqlqueries as qq


load_dotenv()


connection = psycopg2.connect(os.environ['DATABASE_URL'])


def create_tables():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(qq.CREATE_BOOKS_TABLE)
            cursor.execute(qq.CREATE_READERS_TABLE)
            cursor.execute(qq.CREATE_READ_LOGS_TABLE)

def remove_tables():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(qq.DROP_TABLES)

def insert_book(title, author):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(qq.INSERT_BOOK, (title, author))

def select_books(term=''):
    with connection:
        with connection.cursor() as cursor:
            if len(term) == 0: cursor.execute(qq.SELECT_ALL_BOOKS)
            else:
                condition = '%'+term+'%'
                cursor.execute(qq.SELECT_BOOKS, (condition, condition))
            return cursor.fetchall()

def insert_reader(name):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(qq.INSERT_READER, (name,))

def select_readers():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(qq.SELECT_READERS)
            return cursor.fetchall()

def insert_log(book_id, reader, date, comment):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(qq.INSERT_LOG, (book_id, reader, date, comment))

def select_logs(reader):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(qq.SELECT_LOGS, (reader,))
            return cursor.fetchall()