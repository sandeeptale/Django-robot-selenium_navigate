from django.urls import path
from .views import execute_tests

urlpatterns = [
    path('tests/v1/execute', execute_tests, name='execute_tests'),
]



