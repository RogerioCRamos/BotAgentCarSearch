# BotAgentCarSearch
Desafio Prático de criação de bot que responde lista de carros com base em filtros

#Dependencies
-Python
-Instalar as dependencias através do comando "pip install -r requirements.txt"

#RUN
Para executar esta aplicação, inicie o servidor com o comando "python server.py" no terminal.
Após isso, execute o agente virtual no terminal com o comando "python clientSide.py"

#RUN-Explanation
A aplicação consiste em um agente vitual, que se apresenta para você e solicita algumas perguntas.
As perguntas podem ser respondidas ou puladas apertando ENTER.
Ao final das perguntas, o agente solicita ao servidor que busque no banco de dados uma lista de carros com base nos filtros enviados e retorna com uma tabela.

OBS: A aplicação foi desenvolvida para gerar uma tabela por vez, podendo ser melhorado para receber mais solicitações na mesma conversa.
OBS: Ao executar a aplicação, o banco será sempre criado/sobrescrito

#ServerKill
Optei por não implementar uma função para encerrar o servidor, sendo assim, necessário encerrar o terminal
