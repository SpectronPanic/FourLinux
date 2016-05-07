#!/usr/bin/python


import json


def exibeMenu():
    print '1 - Cadastrar Usuarios'
    print '2 - Listar Usuarios'
    print '3 - Deletar Usuarios'
    print '4 - Autenticar'


def cadastrarUsuario():
    with open('banco.txt', 'r') as f:
        arquivo = json.loads(f.read())
    novo_usuario = {'login':'', 'senha':'4linux'}
    novo_usuario['login'] = raw_input('Digite o login do usuario: ')
    novo_usuario['senha'] = raw_input('Digite a senha do ususario: ')
    arquivo['usuarios'].append(novo_usuario)
    with open('banco.txt', 'w') as f:
        f.write(json.dumps(arquivo))
    print 'usuario cadastrado com sucesso'



def listarUsuarios():
    with open('banco.txt', 'r') as f:
        conteudo = json.loads(f.read())
    print conteudo.get('usuarios')


def deletarUsuario(*args):
    print 'Deletar Usuario'


def autenticar(*args):
    with open('banco.txt', 'r') as f:
        arquivo = json.loads(f.read())
    login = raw_input('Digite o login do usuario: ')
    senha = raw_input('Digite a senha do usuario: ')
    for usuario in arquivo.get['usuarios']:
        if usuario.get('login') == login and usuario.get('senha') == senha:
            print 'Usuario autenticado com sucesso.'
            break
    else:
        print 'Usuario nao cadastrado ou dados invalidos.'


def switch(opcao):
    try:
         dic = {1:cadastrarUsuario,
                2:listarUsuarios,
                3:deletarUsuario,
                4:autenticar}
         dic[opcao]()
    except Exception as e:
        print 'Voce digitou uma opcao invalida', e


while 1 != 0:
    try:
        exibeMenu()
        opcao = input('Digite a opcao desejada: ')
        switch(opcao, usuarios)
    except Exception as e:
        print 'Sao aceitos apenas numeros: ', e