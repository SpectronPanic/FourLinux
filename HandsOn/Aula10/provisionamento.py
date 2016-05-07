#!/usr/bin/python


from docker import Docker
import sys, json


class Provisionamento:
    def __init__(self):
        pass

    def contratar(self, name, template):
        d = Docker()
        d.createcontainer(name)
        self.instalar(name, template)
        d.getcontaineraddress(name)

    def instalar(self, name, template):
        with open('templates/%s.json' % template, 'r') as f:
            comando = json.loads(f.read())
        d = Docker()
        for c in comando.get('comandos'):
            d.execcommand(name, c)

    def cancelar(self, name):
        d = Docker()
        d.removecontainer(name)

    def listar_servicos(self):
        d = Docker()
        d.listcontainers()


if __name__ == '__main__':
    prov = Provisionamento()
    prov.listar_servicos()
    if sys.argv[1] == 'contratar':
        servico = sys.argv[2]
        template = sys.argv[3]
        prov.contratar(servico, template)
    elif sys.argv[1] == 'cancelar':
        servico = sys.argv[2]
        prov.cancelar(servico)
    else:
        print 'Opcao invalida.'
