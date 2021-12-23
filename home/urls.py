
from django.urls import path
from . views import *


urlpatterns = [
    path('login/', loginn, name='login'),
    path('signup/', signup, name='signup'),
    path('', home, name='home'),
    path('alltodo/', alltodo, name='alltodo'),
    path('delete-todo/', delete_todo, name='deletetodo'),
    path('change-status/',
         change_todo, name='changetodo'),
    path('logout/', signout, name='signout'),
    path('graph-info/', graph, name='graph'),

]
