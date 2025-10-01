import pytest
import random
import json
from unittest.mock import patch, MagicMock
from clientSide import normalizeAnswers, askClient, sendToServer


'''
Filtros base para teste
'''
filters = {
            'marca': 'ford',
            'modelo': 'focus',
            'ano': '2010',
            'categoria': 'hatchback',
            'cor': random.choice(['Preto', 'Branco', 'Azul', 'Prata']),
            'combustivel': random.choice(['Alcool', 'Gasolina', 'Flex']),
            'km': random.randint(0,200000),
            'direcao': random.choice(['Manual', 'Automático']),
            'vidros': random.choice(['Sim', 'Não']),
            'multimidia': random.choice(['Sim', 'Não']),
        }


'''
Teste das normalizações
Verificando com meu nome e espaços no inicio e no final
Verificando com meu nome + acentos + espaços ao final
Verificando resposta com String de espaços
Verificando resposta vazia
'''
def testNormalizeAnswers():

    assert normalizeAnswers(' rogerio Cavalcanti rAmos ') == 'Rogerio Cavalcanti Ramos'
    
    assert normalizeAnswers('rogério   ') == 'Rogerio'

    assert normalizeAnswers('   ') == ''

    assert normalizeAnswers(None) == None

'''
Teste das perguntas ao cliente
retirei 3 dados dos filtros iniciais para testar possibilidades 
'''
def testAskClient():

    with patch('builtins.input', side_effect=['ford', 'focus', '2010']):
        
        filter = filters.copy()
        filter.pop('marca')
        filter.pop('modelo')
        filter.pop('ano')

        result = askClient(filter)

        assert result['marca'] == 'Ford'
        assert result['modelo'] == 'Focus'
        assert result['ano'] == '2010'

@patch('socket.socket')
def test_sendToServer(mockSocketClass):
    mockSocket = MagicMock()
    mockSocketClass.return_value.__enter__.return_value = mockSocket

    fakeResponse = {
        'status' : 'ok',
        'data' : [filters]
    }

    fakeResponse = json.dumps(fakeResponse) + '\n'

    mockSocket.recv.return_value = fakeResponse.encode('utf-8')

    result = sendToServer(filters)

    assert result["status"] == "ok"
    assert isinstance(result["data"], list)
    assert result["data"][0]["marca"] == "ford"