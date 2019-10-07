# Django as a Microframework

Code to accompany Django Fellow Carlton Gibson's talk at DjangoCon US 2019. Link to video will be added when available (soon).

## Instructions

In directory of your choice...

```
$ pipenv install django==2.2.6 gunicorn==19.9.0
$ pipenv shell
(env) $ django-admin startproject micro_project .
(env) $ touch hello_django.py
```

Update `hello_django.py` as follows:

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

And then...check out [http://127.0.0.1:8000](http://127.0.0.1:8000).
