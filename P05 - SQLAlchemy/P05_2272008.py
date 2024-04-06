# Penulis : Elmosius Suli - 2272008
from sqlalchemy import create_engine, Column, Integer, String, select, delete
from sqlalchemy.orm import declarative_base, Session

Base = declarative_base()

class Book(Base):
  __tablename__ = 'books'
  
  isbn = Column(String(25), primary_key=True)
  title = Column(String(50))
  author = Column(String(30))
  year_published = Column(String(4))
  
  def __repr__(self):
    return f'ISBN : {self.isbn} | Title: {self.title} |\
Author: {self.author} | Year_published: {self.year_published}'
  
def main():
  books_db = ('mysql+pymysql://root:@127.0.0.1/books_db')  
  engine = create_engine(books_db, echo=False)
  Base.metadata.create_all(engine)
  session = Session(engine)


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
      
      book = Book(isbn=isbn, title=title, author=author, year_published=year_published)
      session.add(book)
      session.commit()
      print()

    elif(option == 2):
      isbn = str(input('Masukkan ISBN: '))
      title = str(input('Masukkan Judul: '))
      author = str(input('Masukkan Pengarang: '))
      year_published = str(input('Tahun dibuat: '))
      
      book= session.query(Book).filter(Book.isbn == isbn).first()
      if book:
        book.title = title
        book.author = author
        book.year_published = year_published
        session.commit()
      print()
      
    elif(option == 3):
      isbn = str(input('Masukkan ISBN: '))
      
      book= session.query(Book).filter(Book.isbn == isbn).first()
      if book:
        session.delete(book)
        session.commit()
      print()
          
    elif(option == 4):
      books = session.query(Book).all()
      print(books)
      print()
      
    else:
      print('The option number only 1,2,3,4 ')
      print()
      
    option = int(input('Which Option? : '))
    session.close()
    
if __name__ == "__main__":
    main()