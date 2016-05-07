#!/usr/bin/python


from ssh import SSH
import json
from log import Logs


class Docker(SSH, Logs):
    def __init__(self):
        SSH.__init__(self)
        self.log_file = 'docker.log'
        self.image = 'ubuntu'

    def createcontainer(self, name):
        self.writelog('Iniciado criacao do container.')
        cmd = 'docker run -tdi --name %s %s /bin/bash' % (name, self.image)
        print self.exec_command(cmd)
        self.writelog('Cricao finalizada.')

    def removecontainer(self, name):
        self.writelog('Removendo container %s.' % name)
        cmd = 'docker stop %s && docker rm %s' % (name, name)
        print self.exec_command(cmd)
        self.writelog('Remocao finalizada.')

    def getcontaineraddress(self, name):
        self.writelog('Buscando container.')
        cmd = 'docker inspect %s' % name
        endereco = self.exec_command(cmd)
        endereco = json.loads(endereco)
        endereco = endereco[0].get('NetworkSettings') \
            .get('Networks') \
            .get('bridge') \
            .get('IPAddress')
        print 'Endereco: ', endereco
        self.writelog('Busca finalizada.')

    def listcontainers(self):
        cmd = 'docker ps -a'
        print self.exec_command(cmd)

    def execcommand(self, name, com):
        self.writelog('Executando comando %s.' % com)
        cmd = 'docker exec %s %s' % (name, com)
        print self.exec_command(cmd)
        self.writelog('Comando finalizado.')
