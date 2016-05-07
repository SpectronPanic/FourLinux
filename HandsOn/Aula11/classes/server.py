#!/usr/bin/python


from modulos.docker import Docker
from models.model import session, Servers as servermodel


class Server:
    def __init__(self, nome=''):
        self.nome = nome

    def instalar(self):
        try:
            d = Docker()
            d.createcontainer(self.nome)
            endereco = d.getcontaineraddress(self.nome)
            s = servermodel()
            s.nome = self.nome
            s.descricao = endereco
            session.add(s)
            session.commit()
        except Exception as e:
            session.rollback()
            print 'Falhou ao instalar o servidor: ', e

    def listar(self):
        try:
            servidores = session.query(servermodel).all()
            for s in servidores:
                print s.id, ' - ', s.nome, ' - ' , s.descricao
        except Exception as e:
            print 'Falhou ao listar: ', e

    def remove(self, nome):
        try:
            servidor = session.query(servermodel) \
                                .filter(servermodel.nome==nome) \
                                .first()
            if servidor:
                d = Docker()
                d.removecontainer(nome)
                session.delete(servidor)
                session.commit()
                print 'Servidor removido com sucesso.'
            else:
                print 'Servidor nao encontrado.'
        except Exception as e:
            session.rollback()
            print 'Falhou ao remover: ', e