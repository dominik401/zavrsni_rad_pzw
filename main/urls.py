from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import *
from .views import ProjectViewSet
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', include(router.urls)),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', register, name='register'),
    

    path('project/', ProjectList.as_view(), name='project_list'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('project_create/', ProjectCreateView.as_view(), name='project_create'),
    path('project_delete/<int:pk>', ProjectDeleteView.as_view(), name='project_delete'),
    path('project_update/<int:pk>', ProjectUpdateView.as_view(), name='project_update'),


    path('task/', TaskList.as_view(), name='task_list'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('task_create/', TaskCreateView.as_view(), name='task_create'),
    path('task_delete/<int:pk>', TaskDeleteView.as_view(), name='task_delete'),
    path('task_update/<int:pk>', TaskUpdateView.as_view(), name='task_update'),

    path('category/', CategoryList.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('category_create/', CategoryCreateView.as_view(), name='category_create'),
    path('category_delete/<int:pk>', CategoryDeleteView.as_view(), name='category_delete'),
    path('category_update/<int:pk>', CategoryUpdateView.as_view(), name='category_update'),

    path('timelog/', TimeLogList.as_view(), name='timelog_list'),
    path('timelog/<int:pk>/', TimeLogDetailView.as_view(), name='timelog_detail'),
    path('timelog_create/', TimeLogCreateView.as_view(), name='timelog_create'),
    path('timelog_delete/<int:pk>', TimeLogDeleteView.as_view(), name='timelog_delete'),
    path('timelog_update/<int:pk>', TimeLogUpdateView.as_view(), name='timelog_update'),

    path('reminder/', ReminderList.as_view(), name='reminder_list'),
    path('reminder/<int:pk>/', ReminderDetailView.as_view(), name='reminder_detail'),
    path('reminder_create/', ReminderCreateView.as_view(), name='reminder_create'),
    path('reminder_delete/<int:pk>', ReminderDeleteView.as_view(), name='reminder_delete'),
    path('reminder_update/<int:pk>', ReminderUpdateView.as_view(), name='reminder_update'),

]
