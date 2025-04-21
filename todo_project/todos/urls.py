from django.urls import path
from . import views

urlpatterns = [
    path('todo/', views.todo_list, name='todo_list'),
    path('signup/', views.signup_view, name='signup'),
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('add/', views.add_todo, name='add_todo'),
    path('delete/<int:todo_id>/', views.delete_todo, name='delete_todo'),
    path('update/<int:todo_id>/', views.update_todo, name='update_todo'),
]
