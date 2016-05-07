#!/usr/bin/python


from paramiko.client import SSHClient
import paramiko


def executar_comando(usuario, senha):
    ssh = SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())


    try:
        ssh.connect('localhost', username =usuario, password=senha)
        stdin, stdout, stderr = ssh.exec_command('ls -la')
        if stderr.channel.recv_exit_status() != 0:
            print stderr.read()
        else:
            print stdout.read()


    except Exception as e:
        print 'Falhou ao conectar: ', e

if __name__ == '__main__':
    print __name__