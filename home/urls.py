
from django.urls import path
from . views import *
urlpatterns = [
    path('', loginn, name='login'),
    path('signup/', signup, name='signup'),
    path('main/', home, name='home'),
    # path('add-todo/', add_todo, name='add_todo'),
    # path('delete-todo/<int:id>/', delete_todo, name='delete_todo'),
    # path('change-status/<int:id>/<str:status>/', change_todo),
    path('logout/', signout, name='signout'),
    # path('addevent/', addevent, name='addevent'),
    # path('change/<int:id>/', change, name='change'),
    # path('comments/<int:id>/', coments, name='coments'),
]
