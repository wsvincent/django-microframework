# Django as a Microframework


A single-page Django website as demoed by Django Fellow Carlton Gibson at DjangoCon US 2019 ([video](https://www.youtube.com/watch?v=w9cYEovduWI&list=PL2NFhrDSOxgXXUMIGOs8lNe2B-f4pXOX-&index=6&t=0s)).


## Set Up

In a directory of your choice install Django.

```
$ pipenv install django==2.2.6
$ pipenv shell
(env) $
```

## Option 1

Create a new file `hello_django.py` and update it as follows:

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
    path('', hello_world)
]

application = WSGIHandler()
```

Install [Gunicorn](https://gunicorn.org) to run the local server.

```
(env) $ pipenv install gunicorn==19.9.0
```

Then start the server:

```
(env) $ gunicorn hello_django:application
```

And navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Option 2

As pointed out by [Peter Baumgartner](https://github.com/ipmb), if we import `execute_from_command_line` then it's possible to make `python hello_django1.py` the equivalent of running Django's `manage.py` command.

To demo with `runserver` rather than Gunicorn we will set `DEBUG` to `TRUE`.

```python
from django.conf import settings
from django.core.handlers.wsgi import WSGIHandler
from django.core.management import execute_from_command_line # new
from django.http import HttpResponse
from django.urls import path

settings.configure(
    ROOT_URLCONF=__name__,
    DEBUG=True, # new
)

def hello_world(request):
    return HttpResponse("Hello, Django!")

urlpatterns = [
    path('', hello_world)
]

application = WSGIHandler()

if __name__ == "__main__": # new
    execute_from_command_line()
```

Then start the server with Django's `runserver` command.

```
(env) $ python hello_django1.py runserver
```

And navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000). 
