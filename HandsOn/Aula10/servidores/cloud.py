#!/usr/bin/python


from servidor import Servidor


class Cloud(Servidor):
    pass

    def acesso(self):
        print 'O acesso foi feito por SSH.'

    def contratarcpu(self):
        self.cpu += 1
        print 'Total de CPUs: ', self.cpu

if __name__ == '__main__':
    c = Cloud()
    print 'CPU: ', c.cpu
    print 'MEMORIA: ', c.memoria
    print 'DISCO: ', c.disco
    c.acesso()
    print '========================'
    c.contratarcpu()
    c.contratarcpu()
    c.contratarcpu()
