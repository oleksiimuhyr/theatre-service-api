from django.urls import path
from theatre.views import plays_list, plays_detail

app_name = 'theatre'

urlpatterns = [
    path('/plays/', plays_list, name='plays-list'),
    path('/plays/<pk>/', plays_detail, name='plays-detail'),
]
