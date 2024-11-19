# Django-Projeto-Agenda

Iniciar o projeto Django

- python -m venv venv #Cria o Ambiente Virtual
- . venv/bin/activate # Ativa o Ambiente Virtual
- pip install django #Instala o django
- django-admin startproject project . #Cria o Projeto
- python manage.py startapp contact  #Cria o APP Contato


Migrando a base de dados do Django

- python manage.py makemigrations # Já está criada, não precisa executar
- python manage.py migrate

Criar um Super Usuário 

- python manage.py createsuperuser
- python manage.py changepassword [Nome do Usuário] # Alterar a senha do seu usuário


