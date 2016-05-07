#!/usr/bin/python

usuario    = "alisson.machado"
password   = "4linux"

print "\t\tDigite 1 para cadastrar usuarios\n \
       Digite 2 para listar todos os usuarios\n \
       Digite 3 para deletar um usuario\n \
       Digite 4 para autenticar usuarios"


opcao = input("Digite a opcao desejada:")
if (opcao == 1):
    print "Cadastrar usuarios selecionado"
elif (opcao == 2):
    print "Listar usuarios selecionado"
elif (opcao == 3):
    print "Deletar usuarios selecionado"
elif (opcao == 4):
    nome = raw_input("Digite o login:")
    senha = raw_input("Digite sua senha:")
    if (nome == usuario and senha == password):
        print "Seja bem vindo %s" %(nome)
    else:
        print "Acesso negado"
else:
    print "Opcao Invalida"