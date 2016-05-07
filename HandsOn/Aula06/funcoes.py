#!/usr/bin/python


import json
import banco


def exibeMenu():
    print '1 - Cadastrar Usuarios'
    print '2 - Listar Usuarios'
    print '3 - Deletar Usuarios'
    print '4 - Autenticar'


def cadastrarUsuario():
    login = raw_input('Digite o login do usuario: ')
    senha = raw_input('Digite a senha do usuario: ')
    banco.cadastrarusuario(login, senha)
    print 'Usuario cadastrado com sucesso.'


def listarUsuarios():
    banco.listarusuarios()

def deletarUsuario():
    banco.listarusuarios()
    id = input('Digite o ID do usuario que deseja deletar: ')
    banco.deletarusuario(id)


def autenticar():
    login = raw_input('Digite o seu login: ')
    senha = raw_input('Digite a sua senha: ')
    usuario = banco.buscarusuario(login)
    for u in usuario:
        if u[1] == login and u[2] == senha:
            print 'Seja bem vindo: ',u[1]
            break
    else:
        print 'Senha incorreta'


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
        switch(opcao)
    except Exception as e:
        print 'Sao aceitos apenas numeros: ', e