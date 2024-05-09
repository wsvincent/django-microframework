# µDjango (Django as a Microframework)

How close can Django get to [Flask's](https://flask.palletsprojects.com/en/3.0.x/quickstart/) five-line "Hello, World!" implementation?

<img src="hello_world.png">

[Carlton Gibson](https://github.com/carltongibson) gave a talk at DjangoCon US 2019, [Using Django as a Micro-Framework](https://www.youtube.com/watch?v=w9cYEovduWI&list=PL2NFhrDSOxgXXUMIGOs8lNe2B-f4pXOX-&index=6&t=0s), where he demonstrated a single file implementation of "Hello, World!" in Django.

This repo demonstrates his original code example and subsequent attempts to display "Hello, World!" in a single file in as few lines of code as possible.

## Set Up

On the command line navigate to a directory, create and activate a new Python virtual environment, and install Django via `pip`.

```
# Windows
$ python -m venv .venv
$ .venv\Scripts\Activate.ps1
(.venv) $ python -m pip install django~=5.0.0

# macOS
$ python3 -m venv .venv
$ source .venv/bin/activate
(.venv) $ python -m pip install django~=5.0.0
```

## Option 1: [Carlton Gibson](https://github.com/carltongibson)

```python
# hello_django1.py
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
(.venv) $ python -m pip install gunicorn==22.0.0
```

Start the server.

```
(.venv) $ gunicorn hello_django:application
```

Navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000). To stop the Gunicorn server, use `Ctrl+c` on the command line.

## Option 2: [Peter Baumgartner](https://github.com/ipmb) 

Peter offered an update using `execute_from_command_line` to make `python hello_django.py` the equivalent of running Django's `manage.py` command. It also does not need `Gunicorn` to be installed.

```python
# hello_django2.py
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
(.venv) $ python hello_django1.py runserver
```

And navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000). 

## Option 3: [Paolo Melchiorre](https://github.com/pauloxnet/uDjango) 

At the DjangoCon US 2023 sprints, Paolo presented a new version of this file that uses ASGI and [uvicorn](https://www.uvicorn.org/) to return the JSON response "Hello World".

Install `uvicorn` along with the existing Django installation.

```
(.venv) $ python -m pip install uvicorn
```

Create a new file called `hello_django3.py` and update it as follows:

```python
# hello_django3.py
from django import conf, http, urls
from django.core.handlers.asgi import ASGIHandler

conf.settings.configure(ALLOWED_HOSTS="*", ROOT_URLCONF=__name__)

app = ASGIHandler()


async def root(request):
    return http.JsonResponse({"message": "Hello World"})


urlpatterns = [urls.path("", root)]
```

Start the server with the `uvicorn` command:

```
(.venv) $ uvicorn hello_django3:app --reload
```

Open your browser at `http://127.0.0.1:8000` and the JSON response is:

```
{ "message": "Hello World" }
```


## Option 4: [Andrew Godwin](https://github.com/andrewgodwin/django-singlefile) 

In March 2024, Andrew Godwin released a small library that makes it easier to write single-file Django applications in a similar way to how you'd write Flask applications. First, install the library.

```
(.venv) $ python -m pip install django-singlefile
```

Then create a file called `hello_django4.py` with the following code:

```python
# hello_django4.py
from django.http import HttpResponse
from django.singlefile import SingleFileApp

app = SingleFileApp()


@app.path("")
def index(request):
    name = request.GET.get("name", "World")
    return HttpResponse(f"Hello, {name}!")


if __name__ == "__main__":
    app.main()
```

To run the app you can call it from the command line:

```
(.venv) $ python hello_django4.py runserver
```
