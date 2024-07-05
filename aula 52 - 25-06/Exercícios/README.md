# Instruções

para rodar o projeto precisa instalar o python versão 3.12 e XAMPP

No XAMPP ligar apenas apache e mysql

CERTIFICA-SE DE ABRIR O VSCODE NO DIRETÓRIO 'EXERCÍCIOS' POIS SE TENTAR EM DIRETÓRIOS ACIMA DELE O PROGRAMA NÃO RODARÁ 

após isso, no terminal baixar o virtualenv 

    pip install virtualenv

junto com 
    
    python -m venv .venv

para adicionar a pasta .venv no diretório e assim mudar a versão de python para número_versão('.venv': venv)

    pip list

para confirmar que tem apenas a dependência pip instalada, senão feche todas as janelas de vscode e reabra e repita o comando até que venha apenas pip

    pip install flask

para instalar as dependências do flask

    pip instal flask-wtf

para instalar as dependências do flask-WhatTheForms

    pip install flask-wtf[email]

para instalar as dependências de email do flask-WhatTheForms

    pip install mysql-connector

para instalar as dependências de mysql

    flask --app exercicio.py run --debug

para rodar o programa em modo debug