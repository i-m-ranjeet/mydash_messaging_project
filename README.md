# mydash_messaging_project
### Introduction to Project:
        >> In this Django Project I have created an app named as "msg_api"
        >> inwhich I have designed an api for genrate the token by using username and password :   http://localhost:8000/api/usertoken/
        >> an another api for add a new message to database. : http://localhost:8000/api/messages/
        
### Requirments:
        >> Postman or any other http request tester
        >> django
        
### commands:
        ____install all requirements and additional packages
                >> pip install django     //if you don't have
                >> pip install django-rest-framework
        >> $ python manage.py runserver   //for run server
        
        ____create new user 
                >> python manage.py createsuperuser
                >> Username (leave blank to use 'ranjeet'): root
                >> Email address: root123@gmail.com
                >> Password: ******
                >> Password (again): ******
        
# Authantication and New message Process:
        >> By using Postman send a post request and username and password in body, send your request to this api 'http://localhost:8000/api/usertoken/
        >> if you got the token use that token with every request to authanticate your account: send this token from headers as > 'Authantication' 'token <your token>'
        >> New Message: after genrating the token send your message as 'message' '<your message>' from body, with your token at : 'http://localhost:8000/api/messages/'
        
        
