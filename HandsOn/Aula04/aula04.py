#!/urs/bin/python


from modulos.SSHModulo import executar_comando as executar_ssh
from modulos.ValidacaoModulo import validar_token as validar_user


if validar_user():
    usuario = raw_input('Digite o usuario: ')
    senha = raw_input('Digite a senha: ')
    executar_ssh(usuario, senha)
else:
    print 'Seu token expirou'





