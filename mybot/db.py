from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()
print('DATABASE_URL')
engine = create_engine('DATABASE_URL', echo=True)

SessionLocal = sessionmaker(autoflush=False, bind=engine)

Base = declarative_base()
