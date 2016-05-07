#!/usr/bin/python


from pymongo import MongoClient


def conectabanco():
    client = MongoClient('127.0.0.1')
    db = client["teste"]
    return db


def listarservidores():
    db = conectabanco()
    for s in db.servers.find():
        print s.get('nome'), ' - ' ,s.get('endereco'), ' administradores: ' ,s.get('administradores')


def cadastrarservidor():
    novo_servidor = {'nome': '', 'endereco': '','administradores':[]}
    novo_servidor['nome'] = raw_input('Digite o nome do servidor: ')
    novo_servidor['endereco'] = raw_input('Digite o endereco IP do servidor: ')
    db = conectabanco()
    db.servers.insert(novo_servidor)
    print 'Servidor cadastrado com sucesso!'


def definiradministrador(endereco):
    db = conectabanco()
    login = raw_input('Digite o login do administrador: ')
    busca = {'endereco': endereco}
    administradores = {'administradores': {'login': login}}
    valores = {'$addToSet': administradores}
    db.servers.update(busca, valores)
    print 'Dados atualizados!'


def deletarServidor(endereco):
    db = conectabanco()
    busca = {'endereco': endereco}
    db.servers.remove(busca)
    print 'Servidor deletado com sucesso.'


def deletaradministrador(endereco):
    db = conectabanco()
    login = raw_input('Digite o login do administrador: ')
    busca = {'endereco': endereco, 'administradores.login': login}
    valores = {'administradores': {'login': login}}
    db.servers.update(busca, {'$pull': valores})
    print 'Administrador removido!'

if __name__ == '__main__':
    #cadastrarservidor()
    listarservidores()
    endereco = raw_input('Digite o endereco IP do servidor: ')
    #definiradministrador(endereco)
    #deletarServidor(endereco)
    deletaradministrador(endereco)
