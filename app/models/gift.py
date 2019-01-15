from sqlalchemy import Column, String, Boolean, Integer, ForeignKey, orm
from sqlalchemy.orm import relationship

from app.models.base import Base



class Gift(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    isbn = Column(String(15), nullable=False)
    launched = Column(Boolean, default=False)

    @orm.reconstructor
    def __init__(self):
        self.fields = ['id', 'user', 'uid', 'isbn',
                       'launched']
