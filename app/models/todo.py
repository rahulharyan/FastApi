from sqlalchemy import Column, Integer,String,Boolean,ForeignKey
from app.core.database import Base

class Todo(Base):
    __tabelname__ = "todos"

    id = Column(Integer,primary_key=True,index=True)
    title = Column(String)
    complete=Column(Boolean,default=False)
    owner_id = Column(Integer,ForeignKey('users.id'))
    