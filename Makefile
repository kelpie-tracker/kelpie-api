help:
	@echo "---------------- HELP ---------------------"
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/\://'| sed -e 's/##//'

up:                    ## Sobe o ambiente via compose localmente
	docker-compose up --force-recreate --build

run:                   ## Executa a aplicação localmente
	cd ./src && python app.py

setup-python:          ## Instala todas as dependências necessárias para rodar o projeto
	pip install -r requirements.txt

db_local:              ## Realiza o setup do banco local ( Necessário rodar: docker-compose up db)
	mysql -u root -h db -e "CREATE DATABASE IF NOT EXISTS kelpie" -pteste123
	cd ./src && python  -c "from app import app; from models.base import db; db.create_all(app=app)"

db-migrate:            ## Realiza o migrate do banco
	cd ./src && flask db migrate

app_clear_cache:       ## Realiza a limpeza de pré-compilados locais
	rm -rf ./*.pyc