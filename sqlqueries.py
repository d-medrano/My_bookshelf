CREATE_BOOKS_TABLE = """
    CREATE TABLE IF NOT EXISTS books (
        id SERIAL PRIMARY KEY,
        title TEXT,
        author TEXT
    );
"""
CREATE_READERS_TABLE ="""
    CREATE TABLE IF NOT EXISTS readers (
        name TEXT PRIMARY KEY
    );
"""
CREATE_READ_LOGS_TABLE = """
    CREATE TABLE IF NOT EXISTS read_logs (
        log_id SERIAL PRIMARY KEY,
        book_id INTEGER,
        reader_id TEXT,
        log_date TEXT,
        comment TEXT,
        FOREIGN KEY(book_id) REFERENCES books(id),
        FOREIGN KEY(reader_id) REFERENCES readers(name)
    );
"""
DROP_TABLES = "DROP TABLE IF EXISTS read_logs, books, readers;"
INSERT_BOOK = "INSERT INTO books (title, author) VALUES (%s, %s);"
SELECT_ALL_BOOKS = "SELECT * FROM books;"
SELECT_BOOKS = "SELECT * FROM books WHERE (title ILIKE %s OR author ILIKE %s);"
INSERT_READER = "INSERT INTO readers (name) VALUES (%s);"
SELECT_READERS = "SELECT * FROM readers;"
INSERT_LOG = "INSERT INTO read_logs (book_id, reader_id, log_date, comment) VALUES (%s, %s, %s, %s);"
SELECT_LOGS = """
    SELECT books.title, books.author, log_date, comment
    FROM read_logs JOIN books ON read_logs.book_id = books.id
    WHERE reader_id = %s;
"""