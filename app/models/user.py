from sqlalchemy import column , Integer, String  #column are represent to column in database and int and str also
from app.core.database import Base  #Prent class required to SQLAlchemy to create a tabel

class User(Base):
    __tabelname__ = "users"

    id = column(Integer,primary_key=True,index=True)
    email=column(String,unique=True,index=True)
    password=column(String)
    
