from django.urls import path
from . import views
from main.views import (
    ProjectList, TaskList, CategoryList, ReminderList, TimelogList,
    ProjectDetailView, TaskDetailView, CategoryDetailView, TimeLogDetailView, ReminderDetailView
)

urlpatterns = [
    path('', views.index, name='index'),
    path('project/', ProjectList.as_view(), name='project_list'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('task/', TaskList.as_view(), name='task_list'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('category/', CategoryList.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('timelog/', TimelogList.as_view(), name='timelog_list'),
    path('timelog/<int:pk>/', TimeLogDetailView.as_view(), name='timelog_detail'),
    path('reminder/', ReminderList.as_view(), name='reminder_list'),
    path('reminder/<int:pk>/', ReminderDetailView.as_view(), name='reminder_detail'),
]
