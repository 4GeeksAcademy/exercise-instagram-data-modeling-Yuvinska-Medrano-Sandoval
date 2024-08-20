import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


#                NOTAS A TOMAR EN CUENTA 
# IMPORTANTE que cada class(una tabla) SIEMPRE lleve una llave primaria (PK)
# el nombre de la tabla siempre en minuscula 
# nullable = True ( se acepta que pase ) 
# nullable = False (es obligatorio que ponga algo ) 
# para crear una relacion necesitamos dos lineas 
#  / la primera se pone el nombre de la  tabla.el nombre de la linea 
#  /y la segunda se encarga de llamar a la tabla nombrada 
# String = Varchar 
# tener cuidado a la hora de escribir el codigo , tiene un orden, arriba hacia abajo 
# asegurate de que lo que quieras llamar esta escrito primero para despues poder llamarlo  

class User(Base):
    __tablename__ = 'user'
    user_id= Column(Integer, primary_key = True)
    username = Column(String(20), unique = True)
    firstname = Column(String(25), nullable = False)
    lastname = Column(String(30), nullable = False)
    email = Column(String(50), nullable = False)

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    user_idRelationship = relationship(User)
    user_to_id = Column(Integer, ForeignKey('user.user_id'))
    user_to_idRelationship = relationship(User)


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    user_idRelationship = relationship(User)

class Comment(Base):
    __tablename__ = 'comment'
    comment_id = Column(Integer, primary_key = True)
    comment_text = Column(String(180), nullable = False)
    author_id = Column(Integer, ForeignKey('user.user_id'))
    author_idRelationship = relationship(User)
    post_id = Column(Integer, ForeignKey('post.id'))
    post_idRelationship = relationship(Post)


class Media(Base):
    __tablename__ = 'media'
    media_id = Column(Integer, primary_key = True)
    type = Column('enum')
    url = Column(String, nullable = False)
    post_id = Column(Integer, ForeignKey('post.id'))
    post_idRelationship = relationship(Post)








    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
