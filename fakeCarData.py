from faker import Faker
from faker_vehicle import VehicleProvider
import pandas as pd
import random

'''
Classe para gerar dados de carros aleatórios
O provider do Faker não gera cores, então criei uma lista chamada carcolor com 4 cores que serão randomizadas
'''
class Car:

    def __init__(self):
        self.fakecar = VehicleProvider(generator=Faker)
        self.carcolor = ['Preto', 'Branco', 'Azul', 'Prata']
    
    #função de criação dos carros
    def carCreator(self):
        
        self.car = self.fakecar.vehicle_object()
        return {
            'marca': self.car['Make'],
            'modelo': self.car['Model'],
            'ano': self.car['Year'],
            'categoria': self.car['Category'],
            'cor': random.choice(self.carcolor),
            'combustivel': random.choice(['Alcool', 'Gasolina', 'Flex']),
            'km': random.randint(0,200000),
            'direcao': random.choice(['Manual', 'Automático']),
            'vidros': random.choice(['Sim', 'Não']),
            'multimidia': random.choice(['Sim', 'Não']),
        }