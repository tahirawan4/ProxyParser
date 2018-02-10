# ProxyParser

Setup:


First install requirements
    
    pip install -r requirements.txt
    
After installing requirements we can do makemigrations and migrate

    python manage.py makemigrations
    python manage.py migrate
    
Create a super user

    python manage.py createsuperuser
    
Start parser:

    python manange.py parse_zip # this will start a process which will start populating database with the data 
    
To View data, we can simply go to admin panel after starting the server 

    python manage.py runserver # Starts the server

    username: admin # You can use the user created by above commands
    password: 1234567a
    
