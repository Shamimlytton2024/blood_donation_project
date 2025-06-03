from sqlalchemy import Column, Integer, String
from lib.database import Base

class Donor(Base):
    __tablename__ = 'donor'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)  #  Add this line
