from django.urls import path
from .views import MenuList

urlpatterns = [
    path('', MenuList.as_view(), name='home'),
]