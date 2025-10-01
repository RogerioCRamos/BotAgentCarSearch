from faker import Faker
import json
import socket
import random
from unidecode import unidecode
from tabulate import tabulate
from agentQuestionsDict import questions, response



'''
    Normaliza a resposta do usuário:
    - Remove espaços extras
    - Remove acentos
    - Coloca em minúsculas
    '''
def normalizeAnswers(filters):

    if not filters:
        return filters  # mantém vazio se o usuário apertar enter
    filters = filters.strip()
    filters = unidecode(filters)
    filters = filters.title()
    return filters


'''
Faz perguntas baseadas no dicionário questions de agentQuestionDict para criar o JSON que será enviado ao servidor
'''
def askClient(filters):
    
    for key, value in questions.items():
        if key not in filters or not filters[key]:
            if isinstance(questions[key], list):
                answer = input('\n'+ random.choice(questions[key]) + ' ')
            else:
                answer = input('\n' + questions[key] + ' ')


            normalized = normalizeAnswers(answer)
            if normalized:
                filters[key] = normalized

    filters = {k: v for k, v in filters.items() if v and str(v).strip()}

    return filters


'''
Envia os filtros para o servidor
'''
def sendToServer(data, host='127.0.0.1', port=5000):

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))

            json_data = json.dumps(data)

            # Envia os dados dos carros
            s.sendall(json_data.encode('utf-8'))

            buffer = ""
            while True:
                part = s.recv(4096).decode('utf-8')
                if not part:
                    break
                buffer += part
                if '\n' in buffer:
                    buffer = buffer.strip()
                    break

            return json.loads(buffer)

    except ConnectionRefusedError:
        print('\nNão foi possível conectar ao servidor. Verifique se ele está executando.')



'''
Execução do agente virtual
'''
if __name__ == '__main__':

    fake = Faker(locale='PT-BR')
    clientFilters = {}

    print(f'Olá! Eu sou {fake.first_name()}. Vamos encontrar o carro ideal para você!')
    print(f'Vou te fazer algumas perguntas para chegarmos no seu carro.\nSe não tiver uma resposta é só apertar enter\n')

    clientFilters = askClient(clientFilters)

    print('\nAgora estou com as suas respostas.\nEstou consultando na nossa lista')

    data = sendToServer(clientFilters)
    if data:
        if data['status'] == 'ok' and data['data']:

            print(random.choice(response['positiva']))

            table_data = [{k: v for k, v in carro.items() if k != 'ID'} for carro in data['data']]
            print(tabulate(table_data, headers='keys', tablefmt='fancy_grid'))

        else:
            print(random.choice(response['negativa']))
    