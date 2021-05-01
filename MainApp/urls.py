from django.urls import path 
from . import views
#URLS, then VIEWS, then HTML file

app_name = 'MainApp'

urlpatterns = [
    #Homepage
    path('', views.index, name='index'),

    path('pizzas', views.pizzas, name='pizzas'),
    path('pizzas/<int:pizza_id>/', views.pizza, name='pizza'),
    path('comments/<int:pizza_id>/', views.comments, name='comments'),
    path('profile/', views.profile, name='profile'),
    #path('new_topic/', views.new_topic, name='new_topic'),
    #path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    #path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]