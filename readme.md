Steps to start this project
1. Create "school" name database in your mysql server.
2. Provide correct Mysql Url according to your system in config.cfg file.
3. Then run commands
___________________________________________________________
SETUP VIRTUAL ENV

a. "python3 -m venv venv"
   
b. "source venv/bin/activate"
   
c. pip3 install -r requirements.txt

________________________________________________________________

INTIALISE DB

a. python3 manage.py db init

b. python3 manage.py db migrate

c. python3 manage.py db upgrade

________________________________________________________________

To runserver

a. python3 manage.py runserver

b. Base url - localhost:8000/admin