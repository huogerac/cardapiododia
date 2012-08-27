Cardapio do dia
===================

Uma lugar para escolher onde almoçar conforme o dia da semana.

Contribuindo com o projeto
--------------------------
É necessário Python 2.7

PREPARANDO O AMBIENTE (APENAS UMA VEZ):
    
    #instalando pacotes
    sudo apt-get install python-virtualenv    
    sudo apt-get install git-core
    
    #criar uma pasta para o ambiente/projeto
    mkdir workspace-py
    cd workspace-py
    
    #criar um ambiente python 
    virtualenv --no-site-packages django14.env    
    
    #habilitar o ambiente 
    . django14.env/bin/activate
    
    #instalando a biblioteca do django dentro do ambiente
    pip install django
    
    #baixar o código do projeto
    git clone https://github.com/huogerac/cardapiododia.git
    cd cardapiododia/django/
    sudo chmod +x manage.py
    
    #criar base de dados (SQLITE)
    ./manage.py syncdb
    
    #rodar aplicação
    ./manage.py runserver
    



