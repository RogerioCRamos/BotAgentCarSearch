import pandas as pd
import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fakeCarData import Car


'''
Como o teste necessita de dados aleatórios,
optei por toda execução criar e/ou sobrescrever os dados já existentes.

O enunciado do teste não solicita nenhum banco específico, então para este teste
vou utilizar o SQLite
'''
def dataBaseCreator():

    engine = create_engine('sqlite:///cardatabase.db')

    return engine


'''
Cria o dataframe para popular o banco de dados
'''
def FakeCarData(engine):
    
    carList=[]
    
    for _ in range(100):
        carList.append(Car().carCreator())

    
    dfCars = pd.DataFrame(carList)
    dfCars.insert(0, 'ID', range(len(dfCars)))

    #if_exists = 'replace' para substituir os dados a cada execução termos novos carros
    dfCars.to_sql('cars', con=engine, if_exists='replace', index=False)


'''
Consulta que retorna os carros baseado nos filtros
'''
def carSearch(engine, filters: dict):

    query = 'SELECT * FROM CARS WHERE 1=1'

    carFilters = []
    for key, value in filters.items():
        carFilters.append(f'{key} = "{value}"')

    if carFilters:
        query += " AND " + " AND ".join(carFilters)
    
    return pd.read_sql(query, engine, params=filters)



