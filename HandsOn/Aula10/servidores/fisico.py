#!/usr/bin/python


from servidor import Servidor


class Fisico(Servidor):
    def __init__(self):
        Servidor.__init__(self)
        self.slots = 4
        self.slots_ocupados = 2
        self.memorias = 4
        self.memorias_ocupadas = 2

    def contratardisco(self):
        if self.slots_ocupados < self.slots:
            self.slots_ocupados += 1
            self.disco += 1024
        else:
            print 'Voce ja atingiu o limite de slots!'

    def contratarmemoria(self):
        if self.memorias_ocupadas < self.memorias:
            self.memorias_ocupadas += 1
            self.memoria += 1024
        else:
            print 'Voce ja atingiu o limite de slots de memoria!'

if __name__ == '__main__':
    f = Fisico()
    print 'CPU: ', f.cpu
    print 'MEMORIA: ', f.memoria
    print 'DISCO: ', f.disco
    f.acesso()
    print '=========================================='
    print f.memoria
    f.contratarmemoria()
    print f.memoria
    f.contratarmemoria()
    print f.memoria
    f.contratarmemoria()
    print f.memoria
