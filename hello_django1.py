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


urlpatterns = [path("", hello_world)]

application = WSGIHandler()

if __name__ == "__main__":  # new
    execute_from_command_line()
