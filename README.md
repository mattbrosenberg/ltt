# ltt
Web Platform for Auctioning Restructured Assets

### Setup:

     $ virtualenv venv
     $ source venv/bin/activate
     $ pip3 install -r requirements.txt
     
     $ python3 manage.py makemigrations
     $ python3 manage.py migrate
     $ python3 manage.py setupgroups
     $ python3 manage.py seed scenario1
     $ python3 manage.py seed scenario2
     $ python3 manage.py createsuperuser
     
     
