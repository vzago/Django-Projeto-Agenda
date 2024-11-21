# Django-Projeto-Agenda

Iniciar o projeto Django

# Cria o Ambiente Virtual
- python -m venv venv 
# Ativa o Ambiente Virtual
- . venv/bin/activate 
# Instala o django
- pip install django 
# Cria o Projeto
- django-admin startproject project .
# Cria o APP Contato 
- python manage.py startapp contact 


Migrando a base de dados do Django

- python manage.py makemigrations # Já está criada, não precisa executar
- python manage.py migrate

Criar um Super Usuário 

- python manage.py createsuperuser
- python manage.py changepassword [Nome do Usuário] # Alterar a senha do seu usuário


# Importe o módulo
from contact.models import Contact
# Cria um contato (Lazy)
# Retorna o contato
contact = Contact(**fields)
contact.save()
# Cria um contato (Não lazy)
# Retorna o contato
contact = Contact.objects.create(**fields)
# Seleciona um contato com id 10
# Retorna o contato
contact = Contact.objects.get(pk=10)
# Edita um contato
# Retorna o contato
contact.field_name1 = 'Novo valor 1'
contact.field_name2 = 'Novo valor 2'
contact.save()
# Apaga um contato
# Depende da base de dados, geralmente retorna o número
# de valores manipulados na base de dados
contact.delete()
# Seleciona todos os contatos ordenando por id DESC
# Retorna QuerySet[]
contacts = Contact.objects.all().order_by('-id')
# Seleciona contatos usando filtros
# Retorna QuerySet[]
contacts = Contact.objects.filter(**filters).order_by('-id')
