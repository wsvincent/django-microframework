# µDjango (Django as a Microframework)

How close can Django get to [Flask's](https://flask.palletsprojects.com/en/2.1.x/quickstart/) five-line "Hello, World!" implementation?

<img src="hello_world.png">

[Carlton Gibson](https://github.com/carltongibson) gave a talk at DjangoCon US 2019, [Using Django as a Micro-Framework](https://www.youtube.com/watch?v=w9cYEovduWI&list=PL2NFhrDSOxgXXUMIGOs8lNe2B-f4pXOX-&index=6&t=0s), where he demonstrated a single file implementation of "Hello, World!" in Django.

This repo demonstrates his original code example and subsequent attempts to display "Hello, World!" in a single file in as few lines of code as possible.

## Set Up

On the command line navigate to a directory, create and activate a new Python virtual environment, and install Django via `pip`.

### Windows _(PowerShell)_

```powershell
> python -m venv .venv
> .venv\Scripts\Activate.ps1
(.venv) ...> python -m pip install django~=4.2.0
```

### macOS _or_ GNU/Linux

```console
$ python3 -m venv .venv
$ source .venv/bin/activate
(.venv) $ python -m pip install django~=4.2.0
```

## Option 1: [Carlton Gibson](https://github.com/carltongibson)

```python
# hello_django.py
from django.conf import settings
from django.core.handlers.wsgi import WSGIHandler
from django.http import HttpResponse
from django.urls import path

settings.configure(
    ROOT_URLCONF=__name__,
)

def hello_world(request):
    return HttpResponse("Hello, Django!")

urlpatterns = [
    path("", hello_world)
]

application = WSGIHandler()
```

Install [Gunicorn](https://gunicorn.org) to run the local server.

```
(.venv) $ python -m pip install gunicorn==21.2.0
```

Start the server.

```
(.venv) $ gunicorn hello_django:application
```

Navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000). To stop the Gunicorn server, use `Ctrl+c` on the command line.

## Option 2: [Peter Baumgartner](https://github.com/ipmb) 

Peter offered an update using `execute_from_command_line` to make `python hello_django.py` the equivalent of running Django's `manage.py` command. It also does not need `Gunicorn` to be installed.

```python
# hello_django1.py
from django.conf import settings
from django.core.handlers.wsgi import WSGIHandler
from django.core.management import execute_from_command_line  # new
from django.http import HttpResponse
from django.urls import path

settings.configure(
    ROOT_URLCONF=__name__,
    DEBUG=True,  # new
)

def hello_world(request):
    return HttpResponse("Hello, Django!")

urlpatterns = [
    path("", hello_world)
]

application = WSGIHandler()

if __name__ == "__main__":  # new
    execute_from_command_line()
```

Then start the server with Django's `runserver` command.

```
(env) $ python hello_django1.py runserver
```

And navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000). 

## Option 3: [Paolo Melchiorre](https://github.com/pauloxnet) 

Paolo further decreased the size of the file using `lambda` instead of the function, reduced the memory usage using `ALLOWED_HOSTS` instead of `DEBUG`, and made it possible to use the code with `runserver` or `gunicorn`.

```python
# hello_django2.py
from django.conf import settings
from django.core.handlers.wsgi import WSGIHandler
from django.core.management import execute_from_command_line
from django.http import HttpResponse
from django.urls import path

settings.configure(
    ALLOWED_HOSTS="*",  # new
    ROOT_URLCONF=__name__,
)

urlpatterns = [path("", lambda request: HttpResponse("Hello, Django!"))]  # new

if __name__ == "__main__":
    execute_from_command_line()
else:  # new
    application = WSGIHandler()
```

### Run

#### `runserver`

Start the server with Django's `runserver` command.

```console
(.venv) $ python hello_django2.py runserver
```

#### `gunicorn`

Install [Gunicorn](https://gunicorn.org) to run the local server.

```
(.venv) $ python -m pip install gunicorn==21.2.0
```

Start the server with the `gunicorn` command.

```console
(.venv) $ gunicorn hello_django2:application
```

### Test

Navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000).

To stop the `runserver` or `gunicorn`, use `Ctrl+c` on the command line.

## Option 3b: [Paolo Melchiorre](https://github.com/pauloxnet/uDjango)

At the DjangoCon US 2023 sprints, Paolo presented a new version of this file that uses ASGI and [uvicorn](https://www.uvicorn.org/) to return the JSON response "Hello World".