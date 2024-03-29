# Vamos começar
Primeira coisa é que você deve ter uma versão do python que suporta o django, estarei usando neste tutorial a versão 3.8

# 1 Etapa
Agora com o python instalado precisamos de um lugar para trabalhar, usaremos o VS code para isso, então, vamos começar.
Abrindo o terminal na sua pasta do projeto vamos rodar os seguintes comandos:
- Criar nosso ambiente virtual:
```
python -m venv venv
```
- Acessar o script (caso não esteja ativado scripts, veja como ativar aqui Windows: https://www.youtube.com/watch?v=mmXzYxR7s9c)
```
./venv/bin/Activate.ps1
```
- Instalar o Django RestFrameWork
```
pip install django djangorestframework
```
- Iniciar nosso projeto django
```
django-admin startproject Seu_Projeto .
```
- A partir daqui iremos utilizar o manage.py para tudo, começando criando nossos apps
```
python manage.py startapp Seu_App
```
- ... O resto será dado nos tutorias, mas caso faça o pull do repositorio, deve rodar os seguintes comandos
- Criar seu banco de dados
```
python manage.py makemigrations
```
```
python manage.py migrate
```
- Criar seu super usuário
```
python manage.py createsuperuser
```
- Partir pro abraço!
```
python manage.py runserver
```
