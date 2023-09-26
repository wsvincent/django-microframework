# Django as a Microframework


A single-page Django website as demoed by Django Fellow Carlton Gibson at DjangoCon US 2019 ([video](https://www.youtube.com/watch?v=w9cYEovduWI&list=PL2NFhrDSOxgXXUMIGOs8lNe2B-f4pXOX-&index=6&t=0s)). Special thanks to [Peter Baumgartner](https://github.com/ipmb) for his tip on using `execute_from_command_line` to make `python hello_django.py` the equivalent of running Django's `manage.py` command.


## Set Up

On the command line navigate to a new directory, create and activate a new virtual environment, then install Django via `pip`.

```
# Windows
$ python -m venv .venv
$ .venv\Scripts\Activate.ps1
(.venv) $ python -m pip install django

# macOS
$ python3 -m venv .venv
$ source .venv/bin/activate
(.venv) $ python -m pip install django
```

## hello_django.py

Create a new file called `hello_django.py` and update it as follows:

```python
from django.conf import settings
from django.core.handlers.wsgi import WSGIHandler
from django.core.management import execute_from_command_line 
from django.http import HttpResponse
from django.urls import path

settings.configure(
    ROOT_URLCONF=__name__,
    DEBUG=True, 
)

def hello_world(request):
    return HttpResponse("Hello, Django!")

urlpatterns = [
    path("", hello_world)
]

application = WSGIHandler()

if __name__ == "__main__": # new
    execute_from_command_line()
```

Then start the server with Django's `runserver` command.

```
(env) $ python hello_django.py runserver
```

And navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000). 
