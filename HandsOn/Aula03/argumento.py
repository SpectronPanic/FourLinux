#!/usr/bin/python


def func1(*args):
    print 'foram passados',len(args),'parametros'
    print args


def func2(**kwargs):
    print kwargs


quadrado = lambda x: x*x


func1('teste1', 'teste2', 'teste3')
func2(name = 'kwargs', idade= 25)
print quadrado(2)