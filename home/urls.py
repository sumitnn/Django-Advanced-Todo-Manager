
from django.urls import path
from . views import *
urlpatterns = [
    path('login/', loginn, name='login'),
    path('signup/', signup, name='signup'),
    path('', home, name='home'),
    # path('add-todo/', add_todo, name='add_todo'),
    path('delete-todo/<int:id>/', delete_todo, name='deletetodo'),
    path('change-status/<int:id>/<str:status>/',
         change_todo, name='changetodo'),
    path('logout/', signout, name='signout'),
    # path('addevent/', addevent, name='addevent'),
    # path('change/<int:id>/', change, name='change'),
    # path('comments/<int:id>/', coments, name='coments'),
]
