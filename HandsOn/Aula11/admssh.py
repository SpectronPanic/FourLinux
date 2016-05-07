#!/usr/bin/python


from classes.user import User
from classes.server import Server


class Admssh:
    def __init__(self):
        pass

    def exibemenu(self):
        print '1 - Cadastrar Usuarios'
        print '2 - Listar Usuarios'
        print '3 - Deletar Usuarios'
        print '4 - Autenticar'
        print '5 - Criar servidor'
        print '6 - Listar servidor'
        print '7 - Remover servidor'

    def cadastrarusuario(self):
        login = raw_input('Digite o login do usuario: ')
        senha = raw_input('Digite a senha do usuario: ')
        novo_usuario = User(login, senha)
        novo_usuario.save()

    def listarusuarios(self):
        all_users = User()
        all_users = all_users.listall()
        for user in all_users:
            print user.id, ' - ' , user.nome

    def deletarusuario(self):
        login = raw_input('Digite o login do usuario que deseja deletar: ')
        user = User()
        user = user.get(login)
        if user:
            user.remove()
        else:
            print 'Usuario nao encontrado.'

    def autenticar(self):
        login = raw_input('Digite o seu login: ')
        senha = raw_input('Digite a sua senha: ')
        user = User()
        user = user.get(login)
        if user:
            if user.nome == login and user.senha == senha:
                print 'Seja bem vindo %s!' % user.nome
            else:
                print 'Senha incorreta.'
        else:
            print 'Usuario nao encontrado.'

    def criarservidor(self):
        nome = raw_input('Digite o nome do servidor: ')
        novo = Server(nome)
        novo.instalar()

    def listarservidor(self):
        s = Server()
        s.listar()

    def removeservidor(self):
        nome = raw_input('Digite o nome do servidor: ')
        s = Server()
        s.remove(nome)

    def switch(self, opcao):
        try:
            dic = {1:self.cadastrarusuario,
                   2:self.listarusuarios,
                   3:self.deletarusuario,
                   4:self.autenticar,
                   5:self.criarservidor,
                   6:self.listarservidor,
                   7:self.removeservidor}
            dic[opcao]()
        except Exception as e:
            print 'Voce digitou uma opcao invalida', e


while 1 != 0:
    try:
        admssh = Admssh()
        admssh.exibemenu()
        opcao = input('Digite a opcao desejada: ')
        admssh.switch(opcao)
    except Exception as e:
        print 'Sao aceitos apenas numeros: ', e