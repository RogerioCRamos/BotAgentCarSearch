'''
Criei estes dicionários parar "vida" ao agente
'''

questions = {
        'marca': ['Já tem alguma marca em mente?',
                  'Tem alguma marca em vista?',
                  'Você tem alguma marca preferida?'],
       
        'modelo' : ['E curte algum modelo específico?',
                    'Gosta de algum modelo?',
                    'Busca algum modelo?'],
        
        'ano': 'De algum ano especifico?',
       
        'categoria': 'Algum tipo de categoria? SUV, Sedan, Hatch?',
       
        'cor': 'Temos as opções Preto, Prata, Branco e Azul, alguma preferência?',
       
        'combustivel': 'Prefere carro a Gasolina, Álcool ou Flex?',
      
        'km': 'Qual valor de quilometragem?',
       
        'direcao': ['Prefere seu carro manual ou automático?',
                    'Cambio manual ou automático?'],
        
        'vidros': 'Vidros elétricos ou prefere a boa e velha manivela?',
        
        'multimidia': ['Multimidia?',
                       'Som multimidia no carro?',
                       'Prefere ter multimidia, ou é indiferente?'],
    }

response = {
    'positiva': ['Encontrei estas opções:',
                'Tenho essas opções:'],
    'negativa': ['Infelizmente não encontrei nenhum carro com esses filtros',
                 'Não encontrei nenhum carro nas suas preferencias completas']
 }