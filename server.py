import socket
import json
from unidecode import unidecode
from database import Car, dataBaseCreator, FakeCarData, carSearch

'''
Mantive os dados do servidor diretamente no código para não precisar subir o .dotenv no repositorio
'''
HOST = '127.0.0.1'  
PORT = 5000         



'''
Aplica regras especificas aos campos do carro:
- direcao: deve ser 'manual' ou 'automatico'
- vidros: deve ser 'sim' ou 'nao'
- multimidia: deve ser 'sim' ou 'nao'

Campos que não seguem a regra são removidos do JSON.
'''
def validadeCarData(data):

    processed = {}
    for key, value in data.items():

        if key == 'direcao' and value not in ['Manual' 'Automatico']:
            continue  
        if key in ['vidros', 'multimidia'] and value not in ['Sim', 'Nao']:
            continue  

        processed[key] = value

    return processed

def serverStart():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f'Servidor executando em {HOST}:{PORT}. Aguardando conexões...')

        while True:
            conn, addr = s.accept()
            with conn:
                print(f'Conectado por {addr}')
                data = conn.recv(1024)
                if not data:
                    continue
                
                try:
                    clientData = json.loads(data.decode('utf-8'))
                    validData = validadeCarData(clientData)

                    carSearchData = carSearch(engine,validData)
                    
                    print(carSearchData)


                    if hasattr(carSearchData, 'to_dict'):
                        carSearchData = carSearchData.fillna('').to_dict(orient="records")


                    payloadResponse = {
                    'status': 'ok',
                    'data': carSearchData
                }

                    response = json.dumps(payloadResponse, ensure_ascii=False) + '\n'
                    conn.sendall(response.encode('utf-8'))
                

                except json.JSONDecodeError:
                    conn.sendall('Erro ao processar os dados.'.encode('utf-8'))

if __name__ == '__main__':
    
    engine = dataBaseCreator()
    connection = engine.connect()
    
    FakeCarData(engine)
    serverStart()

    connection.close()
