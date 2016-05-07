#!/usr/bin/python
#
# alchemy
#................

from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey, Table, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime
import random


engine = create_engine('postgresql://python:4linux@localhost/loja')
Base   = declarative_base()
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()


usuarios_grupos = Table('usuarios_grupos',
                        Base.metadata,
                        Column('users_id', Integer, ForeignKey('users.id')),
                        Column('groups_id', Integer, ForeignKey('groups.id')),
)


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    descricao = Column(Text)
    senha = Column(String)
    servers = relationship('Servers')
    groups = relationship('Groups', secondary=usuarios_grupos)
    tokens = relationship('Tokens')

class Servers(Base):
    __tablename__ = 'servers'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    descricao = Column(Text)
    user_id = Column(Integer, ForeignKey('users.id'))


class Groups(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    nome = Column(String)


class Tokens(Base):
    __tablename__ = 'tokens'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    server_id = Column(Integer, ForeignKey("servers.id"))
    token = Column(String)
    date_request = Column(DateTime, default=datetime.now())
    server = relationship('Servers')
    user = relationship('Users')

if __name__ == '__main__':
    try:
        Base.metadata.create_all(engine)
        acessos = session.query(Users, Tokens, Servers) \
                                .join(Tokens) \
                                .join(Servers) \
                                .all()
        for a in acessos:
            print a.Users.nome, 'acessa' ,a.Servers.nome, 'token' ,a.Tokens.token
        '''
        token = Tokens()
        token.token = str(random.randint(10000,99999))
        servidor = session.query(Servers).filter(Servers.id==1).first()
        token.server = servidor
        usuario = session.query(Users).filter(Users.id==1).first()
        usuario.tokens.append(token)
        session.add(token)
        session.commit()
        grupo = session.query(Groups).filter(Groups.id==2).first()
        edmar = session.query(Users).filter(Users.id==2).first()
        edmar.groups.append(grupo)
        session.commit()
        edmar = session.query(Users).filter(Users.id==2).first()
        print 'Edmar esta nos grupos: '
        for g in edmar.groups:
            print g.nome
        devops = Groups()
        devops.nome = 'DevOps'
        session.add(devops)
        infra = Groups()
        infra.nome = 'Infraestrutura'
        session.add(infra)
        dev = Groups()
        dev.nome = 'Desenvolvimento'
        session.add(dev)
        session.commit()
        todos = session.query(Servers).all()
        for s in todos:
            print s.id, ' - ' ,s.nome, ' - ' ,s.user_id
        adms = session.query(Users).all()
        for a in adms:
            print  a.id, ' - ' ,a.nome
        edmar = session.query(Users).filter(Users.id==2).first()
        apache = session.query(Servers).filter(Servers.id==3).first()
        #edmar.servers.append(apache)
        #session.commit()
        adms = session.query(Users, Servers).join(Servers).all()
        for a in adms:
            print a.Users.nome, ' adinistra ' ,a.Servers.nome
        dns = Servers()
        dns.nome = 'DNS Master'
        dns.descricao = 'Descricao de DNS Master'
        session.add(dns)
        session.commit()
        print 'Servidor cadastrado com sucesso.'
        todos = session.query(Servers).all()
        for s in todos:
            print s.id, ' - ' ,s.nome
        user = Users()
        user.nome = 'Roger'
        user.descricao = 'Aluno do curso de python'
        user.senha = '123456'
        #session.add(user)
        #session.commit()
        all_users = session.query(Users).all()
        for user in all_users:
            print user.id, ' - ' ,user.nome
        edmar = session.query(Users).filter(Users.id==2).first()
        edmar.nome = 'Edmar'
        session.commit()
        usuario = session.query(Users).filter(Users.id==4).first()
        if not usuario:
            print 'Usuario nao existe.'
        else:
            session.delete(usuario)
            session.commit()
        '''
    except Exception as e:
        session.rollback()
        print 'Falhou ao criar banco: ', e
