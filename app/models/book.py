from sqlalchemy import Column, String, Integer, orm

from app.models.base import Base



class Book(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    author = Column(String(30), default='未名')
    binding = Column(String(20))
    publisher = Column(String(50))
    price = Column(String(20))
    pages = Column(Integer)
    pubdate = Column(String(20))
    isbn = Column(String(15), nullable=False, unique=True)
    summary = Column(String(1000))
    image = Column(String(50))

    '''
    不能将fields写成类变量，因为一旦修改fields，会影响其他的book对象，但是
    默认通过Book.query使用sqlalchemy的时候不会触发每个模型的__init__方法。打上装饰器才会执行__init__方法
    '''
    @orm.reconstructor
    def __init__(self):
        self.fields = ['id', 'title', 'author', 'binding',
                       'publisher',
                       'price','pages', 'pubdate', 'isbn',
                       'summary',
                       'image']


