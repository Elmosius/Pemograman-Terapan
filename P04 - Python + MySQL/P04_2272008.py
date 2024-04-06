# Penulis : Elmosius Suli - 2272008
import pymysql

def connection():
    return pymysql.connect(
        host='127.0.0.1',
        user='root',
        password=''
 )

def create_db(conn,db_name):
    with conn.cursor() as cursor:
        cursor.execute(f'CREATE DATABASE IF NOT EXISTS {db_name}')
    conn.commit()

def create_tb(conn,db_name,table_name, column):
    with conn.cursor() as cursor:
        cursor.execute(f'USE {db_name}')
        cursor.execute(f'CREATE TABLE IF NOT EXISTS {table_name}({column})')

def insert(conn,isbn,title,author,year_published):
    with conn.cursor() as cursor:
      cursor.execute('USE books_db')
      cursor.execute(f"INSERT INTO books VALUES \
      ('{isbn}', '{title}', '{author}', '{year_published}')")
    conn.commit()

def update(conn,isbn,title,author,year_published):
    with conn.cursor() as cursor:
      cursor.execute('USE books_db')
      cursor.execute(f'UPDATE books \
      SET title = "{title}", author = "{author}",\
      year_published = "{year_published}" \
      WHERE isbn = "{isbn}"')

def delete(conn, isbn):
    with conn.cursor() as cursor:
        cursor.execute('USE books_db')
        cursor.execute(f'DELETE FROM books WHERE isbn = "{isbn}"')
        
def select(conn):
    with conn.cursor() as cursor:
      cursor.execute('USE books_db')
      cursor.execute(f'SELECT * from books')
      result = cursor.fetchall()
    return result


def main():
    c = connection()
    create_db(c, 'books_db')
    create_tb(c, 'books_db','books', \
    'isbn VARCHAR(25) PRIMARY KEY, title VARCHAR(30), \
    author VARCHAR(30), year_published VARCHAR(4)')

    print('======Books=======')
    print('Option: ')
    print('1. Insert Book ')
    print('2. Update Book')
    print('3. Delete Book')
    print('4. View All Book')
    print('5. Exit')

    option = int(input('Which Option? : '))
    while(option != 5 ):
      if(option == 1):
        isbn = str(input('Masukkan ISBN: '))
        title = str(input('Masukkan Judul: '))
        author = str(input('Masukkan Pengarang: '))
        year_published = str(input('Tahun dibuat: '))

        insert(c,isbn, title, author, year_published)
      elif(option == 2):
        isbn = str(input('Masukkan ISBN: '))
        title = str(input('Masukkan Judul: '))
        author = str(input('Masukkan Pengarang: '))
        year_published = str(input('Tahun dibuat: '))

        update(c, isbn, title, author, year_published)

      elif(option == 3):
        isbn = str(input('Masukkan ISBN: '))
        delete(c, isbn)
      elif(option == 4):
        print(select(c))
      else:
        print('The option number only 1,2,3,4 ')
      option = int(input('Which Option? : '))


if __name__ == "__main__":
    main()