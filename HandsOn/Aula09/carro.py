#!/usr/bin/python


class Carro:
    def __init__(self):
        self.cor = 'Vermelho'
        self.placa = 'AAA-5555'
        self.modelo = 'Hatch'
        self. ano = '2014'
        self.fabricacao = '2013'
        self.velocidade = 0
        self.velocidade_max = 200
        print 'Instanciou objeto carro'

    def acelerar(self):
        if self.velocidade < self.velocidade_max:
            self.velocidade += 100
            print self.velocidade, ' km/h'
        else:
            print 'Voce atingiu o limite de velocidade!'


if __name__ == '__main__':
    celta = Carro()
    celta.acelerar()
    celta.acelerar()
    celta.acelerar()