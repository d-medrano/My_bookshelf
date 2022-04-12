from os import system, name
import bookshelf


welcome = '--- Welcome to your "Home Bookshelf" ---'

menu = """
--- How can I help you??--------------------
============================================
||                                        ||
||   1) Add a new book to the bookshelf   ||
||   2) See all books in the bookshelf    ||
||   3) Search for a book                 ||
||                                        ||
||   4) Add a new reader                  ||
||   5) See all readers                   ||
||                                        ||
||   6) Add a new read log                ||
||   7) Show readlist by reader           ||
||                                        ||
||   8) Exit                              ||
||                                        ||
============================================
Your selection: """


def clear_screen():
    if name == 'nt': _ = system('cls')
    else: _ = system('clear')

def add_book():
    title = input('\nTitle: ')
    author = input('Author: ')
    bookshelf.insert_book(title, author)
    input('\nPress ENTER to continue...')

def see_books():
    clear_screen()
    print('\n--- Books in your bookshelf ------------\n')
    books = bookshelf.select_books()
    for _id, title, author in books:
        print(f"{_id}: {title} - {author}")
    input('\nPress ENTER to continue...')

def search_book():
    word = input('\nInsert a word to search: ')
    books = bookshelf.select_books(word)
    clear_screen()
    print('--- Books containing "{}" ---\n'.format(word))
    for _, title, author in books:
        print(f"* {title} - {author}")
    input('\nPress ENTER to continue...')

def add_reader():
    name = input('\nName: ')
    bookshelf.insert_reader(name)
    input('\nPress ENTER to continue...')

def see_readers():
    clear_screen()
    print('--- Readers -------------\n')
    readers = bookshelf.select_readers()
    for reader in readers:
        print(f"- {reader[0]}")
    input('\nPress ENTER to continue...')

def new_log():
    book_id = input('\nBook ID: ')
    reader = input('Reader name: ')
    date = input('Date (dd-mm-YYYY): ')
    comment = input('Comment: ')
    bookshelf.insert_log(book_id, reader, date, comment)
    input('\nPress ENTER to continue...')

def show_logs():
    name = input('\nReader name: ')
    booklist = bookshelf.select_logs(name)
    clear_screen()
    print('\n--- {}'.format(name)+chr(39)+'s "Read" list -------------\n')
    for record in booklist:
        print(f"({record[2]}): {record[0]} - {record[1]}")
        print(f'Comment: {record[3]}\n')
    input('Press ENTER to continue...')



clear_screen()
print('\n',welcome)

# bookshelf.remove_tables()
bookshelf.create_tables()

while (user_input := input(menu)) != '8':
    if user_input == '1':
        add_book()
    elif user_input == '2':
        see_books()
    elif user_input == '3':
        search_book()
    elif user_input == '4':
        add_reader()
    elif user_input == '5':
        see_readers()
    elif user_input == '6':
        new_log()
    elif user_input == '7':
        show_logs()
    else:
        print('\nInvalid option!\n')
        input('\nPress ENTER to continue...')
    clear_screen()
clear_screen()