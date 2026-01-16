from sqlalchemy import create_engine  #connects Python to the database
from sqlalchemy.orm import sessionmaker,declarative_base  #sessionmaker == used to talk to the database (insert, select, update)  & #declarative_base == used to create database tables (models)


DATABASE_URL = "sqlite:///./todo.db"    #./todo.db → database file will be created in your project folder   & #does not exist, SQLite will create it automatically

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}  #check_same_thread=False → allows FastAPI to work with SQLite
)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bing=engine)   #Creates a database session

Base= declarative_base()  #ALl the Database models are inhirit from here ex , todo , user

