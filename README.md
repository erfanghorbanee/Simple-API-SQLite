# Simple-API-SQLite

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

 A simple Restful API on Django using the following tech stack: Python - Django - SQLite


## How run the project?


#### Clone the repository :
```bash
$ git clone https://github.com/erfanghorbanee/Simple-API-SQLite.git
$ cd Simple-API-SQLite
```

#### Create a virtualenv and activate it :
 ```bash
$ python -m venv venv
$ . venv/bin/activate
```

#### Or on Windows cmd : 
 ```bash
python -m venv venv
venv\Scripts\activate.bat
```

#### Install the requirements :
```bash
cd simple_api/

pip install -r requirements.txt
```


#### Config your secret variables!
As you might know, it's not secure to put important variables such as SECRET_KEY directly in the code,\
so instead in the Simple-API/simple_api/ directory create a .env file,\
this will be where we put our variables and fetch it in settings.py using  Python Decouple

```
SECRET_KEY='MYSECRETKEY'
DEBUG=True
```

to learn more, you can check this [article](https://dontrepeatyourself.org/post/how-to-use-python-decouple-with-django/).

####  Run makemigrations and migrate :
```bash
python manage.py makemigrations
python manage.py migrate
```

#### Run the tests :
```bash
python manage.py test
```

#### Run the development server :
```bash
python manage.py runserver
```


