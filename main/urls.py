from django.urls import path
from . import views
from main.views import ProjectList, TaskList, CategoryList, ReminderList, TimelogList
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    path('project/', ProjectList.as_view()),
    path('task/', TaskList.as_view()),
    path('category/', CategoryList.as_view()),
    path('reminder/', ReminderList.as_view()),
    path('timelog/', TimelogList.as_view())

]

