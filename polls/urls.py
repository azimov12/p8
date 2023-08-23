from django.urls import path
from .views import function1, function2

urlpatterns = [
    path('path1/', function1),
    path('path2/', function2),
]