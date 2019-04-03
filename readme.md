# Python Flask
This has MVC boilterplate for Flask.

Structure
>tree -I "venv|*.pyc|__pycache__"

.
├── app
│   ├── __init__.py
│   ├── controllers
│   │   ├── ActionController.py
│   │   └── __init__.py
│   ├── models
│   │   └── __init__.py
│   ├── routing.py
│   ├── static
│   │   ├── css
│   │   │   └── sticky-footer.css
│   │   ├── img
│   │   └── js
│   └── templates
│       ├── error
│       │   ├── 403.html
│       │   ├── 404.html
│       │   └── 500.html
│       ├── index.html
│       ├── layout
│       │   ├── base.html
│       │   └── partials
│       │       ├── footer.html
│       │       └── header.html
│       ├── macros
│       │   └── _render_field.html
│       └── security
│           ├── login.html
│           └── register.html
├── config.py
├── logs
├── readme.md
├── requirements.txt
├── run.py
└── tests
    ├── __init__.py
    ├── test_back_end.py
    └── test_front_end.py

## Guidelines
Install a venv with Python version preferably > 3.5 (https://medium.freecodecamp.org/manage-multiple-python-versions-and-virtual-environments-venv-pyenv-pyvenv-a29fb00c296f) 
> (venv) pip install --upgrade pip


## Example

* Checkout code


       git clone https://github.com/darshanpyadav/Flask_MVC.git   
       cd Flask_MVC  

* Install dependencies, (use sudo if required)    

       pip install -r requirements.txt 

* start server    

       python run.py  
       
       or
       
       python run.py -h     # to see all options

* In browser go to,

       http://localhost:8000/?name=<your_name>
