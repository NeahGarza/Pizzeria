from django.urls import path 
from . import views
#URLS, then VIEWS, then HTML file

app_name = 'MainApp'

urlpatterns = [
    #Homepage
    path('', views.index, name='index'),

    path('pizzas', views.pizzas, name='pizzas'),
    path('pizzas/<int:pizza_id>/', views.pizza, name='pizza'),
    path('profile/', views.profile, name='profile'),
    path('new_comm/<int:pizza_id>/', views.new_comm, name='new_comm'),
]