import pytest
from server import validateCarData

'''
Sem a necessidade de mockar, o unico teste possível no servidor é a função validateCarData
'''


'''
Validando com dados
'''
def testValidateCarData():
    input = {
        'direcao': 'Manual',
        'vidros': 'Sim',
        'multimidia': 'Nao',
        'cor': 'vermelho'
    }
    outputExpected = input.copy()
    assert validateCarData(input) == outputExpected

def testValidateCarDataInvalid():
    input = {
        'direcao': 'Semi-automatico',
        'vidros': 'Talvez',
        'multimidia': 'Claro',
        'cor': 'azul'
    }
    outputExpected = {
        'cor': 'azul'
    }
    assert validateCarData(input) == outputExpected

def test_validade_car_data_misto():
    input = {
        'direcao': 'Automatico',
        'vidros': 'Sim',
        'multimidia': 'Não Sei',
        'modelo': 'Civic'
    }
    outputExpected = {
        'direcao': 'Automatico',
        'vidros': 'Sim',
        'modelo': 'Civic'
    }

    print(validateCarData(input))
    assert validateCarData(input) == outputExpected
