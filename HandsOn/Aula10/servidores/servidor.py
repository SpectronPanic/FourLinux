#!/usr/bin/python


class Servidor:
    def __init__(self):
        self.cpu = 4
        self.memoria = 2048
        self.disco = 1024

    def acesso(self):
        print 'O acesso e feito por IPMI.'

    def contratardisco(self):
        self.disco += 1024
        print 'Tamanho atual: ', self.disco