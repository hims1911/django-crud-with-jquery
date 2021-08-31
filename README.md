# django-crud-with-jquery
It contains the Django Application to perform CRUD Operation on Product Publishment


Task for Product CRUD based in Django3 and Python3.8


## Installation

- Clone

```bash
git clone 
```

- Move into directory

```bash
cd django-crud-with-jquery
```

- Initialize virtual environment

```bash
virtualenv -p python3.8 venv
source venv/bin/activate
```

- Install requirements
```bash
pip install -r requirements.txt
```

Migratons

```bash
python manage.py makemigrations
python manage.py migrate
```

- Run server

```bash
python manage.py runserver
```

- Public API
```bash
http://localhost:8000/products/
```
- Create User 

```bash
http://localhost:8000/register/

Email : anything@anything.com
password should contain: Captial,letter Small letter, Character and Minimum 8  -
password example : Password@123
```

- Note 

By double clicking on the table row you can edit the product details,
Editing of Image is not Allowed


