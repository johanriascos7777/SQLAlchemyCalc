from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///calculator.db', echo=True)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer(), primary_key=True)
    username = Column(String(50), nullable=False, unique=True) 
    email = Column(String(50), nullable=False, unique=True)
    created_at = Column(DateTime(), default=datetime.now)  

    def __str__(self):
        return self.username

Session = sessionmaker(engine)
session = Session()

if __name__ == '__main__':
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    
    user1 = User(username = "User1", email= "user1@example.com")
    user2 = User(username = "User2", email= "user2@example.com")
    user3 = User(username = "User3", email= "user3@example.com")

    session.add(user1)
    session.add(user2)
    session.add(user3)
    session.commit()
    
    
    #SELECT  * FROM users;
    users = session.query(User).all()
    
    for user in users:
        print(user)