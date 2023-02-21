import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(BigInteger, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)

class Profile(Base):
    __tablename__ = 'profile'
    id = Column(BigInteger, primary_key=True)
    user_id = Column(BigInteger, ForeignKey('user.id'))
    nickname = Column(String(250), nullable=False)
    status = Column(Boolean, unique=False, default=False)
    number_post = Column(Integer, nullable=False)
    followers = Column(Integer, nullable=False)

class Posts(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    profile_id = Column(BigInteger, ForeignKey('profile.id'))
    url = Column(String(250), nullable=False)
    likes = Column(Integer, nullable=False)

class Stories(Base):
    __tablename__ = 'stories'
    id = Column(Integer, primary_key=True)
    profile_id = Column(BigInteger, ForeignKey('profile.id'))
    likes = Column(Integer, nullable=False)
    views = Column(Integer, nullable=False)

class Comments(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    comments_user = Column(BigInteger, ForeignKey('profile.id'))
    stories_id = Column(BigInteger, ForeignKey('stories.id'))
    posts_id = Column(BigInteger, ForeignKey('posts.id'))
    comments_content = Column(String(250), nullable=False)
    comments_likes = Column(Integer, nullable=False)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
