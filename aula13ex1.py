from sqlalchemy import create_engine, Column
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from getpass import getpass

eng = create_engine(f"mssql+pymssql://salas\\1900726:{getpass()}@sql.salas.aulas/fit_alunos")

Base = declarative_base(eng)

class Author(Base):
    __tablename__ = 'Authors'
    author_id = Column('AuthorId', Integer, autoincrement=True, primary_key=True)
    name = Column('Name', String(30))

Session = sessionmaker(eng)
ses = Session()

autor = ses.query(Author).get(2)
print(autor.name)

autores = ses.query(Author).all()
for i in autores:
    print(i.author_id, i.name)

newAutor = Author(name = 'nome do autor')
ses.add(newAutor)
ses.commit()

q = ses.query(Author)
q = q.filter(Author.author_id==1)
autor = q.one()
autor.name = 'Pabllo Vittar'
ses.commit()

class Book(Base):
    __tablename__ = 'Books'
    book_id = Column('BookId', Integer, autoincrement=True, primary_key=True)
    title = Column('Title', String(30))
    authorid = Column('AuthorId', Integer)

Session = sessionmaker(eng)
ses = Session()



livros = ses.query(Book).all()
for i in livros:
    print("ID:", i.book_id)
    print("Titulo:", i.title)

    print("Autor:", ses.query(Author).get(i.authorid).name)
    print('-'*20)

newLivro = Book(title = 'Title do autor')
ses.add(newLivro)
ses.commit()

q = ses.query(Book)
q = q.filter(Book.book_id==1)
livro = q.one()
livro.name = 'Novo livro'
ses.commit()


