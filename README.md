# Farmblr
Official Farmblr Website

## How to run
Install python <br>
clone the repository <br>
open Terminal/ powershell on the root of the project <br>
install virtualenv package - `pip install virtualenv` <br>
create a virtual environment - `virtualenv env` <br>
activate the virtual env `env\Scripts\activate` (for windows) <br>
install dependencies - run `pip install -r requirements.txt` <br>
change directory to farmblr  `cd farmblr`  <br>
make migrations - `python manage.py makemigrations`  <br>
migrate - `python manage.py migrate`  <br>
create superuser - `python manage.py createsuperuser`  <br>
start server - `python manage.py runserver`  <br>
open browser at `localhost:8000`  <br>
access admin panel at `localhost:8000/admin`  <br>
