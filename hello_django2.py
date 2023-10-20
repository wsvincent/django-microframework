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
