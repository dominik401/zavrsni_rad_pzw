from django.shortcuts import render, redirect
from . import urls
from main.forms import ProjectForm, TaskForm, ReminderForm, TimeLogForm, CategoryForm
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from main.models import Project, Task, Category, TimeLog, Reminder

############################PROJECT#################################

class ProjectList(ListView):
    model = Project

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')  
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) | Q(description__icontains=query)
            )
        return queryset

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'main/project_detail.html'

class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'project_delete.html'
    success_url = reverse_lazy('project_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = self.get_object()
        return context

class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'project_create.html'
    success_url = reverse_lazy('project_list')    
    
class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'project_update.html'
    success_url = reverse_lazy('project_list') 

###########################TASK#################################

class TaskList(ListView):
    model = Task

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | Q(description__icontains=query)
            )
        return queryset

class TaskDetailView(DetailView):
    model = Task
    template_name = 'main/task_detail.html'
    context_object_name = 'task'

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_delete.html'
    success_url = reverse_lazy('task_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = self.get_object()
        return context

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_create.html'
    success_url = reverse_lazy('task_list')    
    
class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_update.html'
    success_url = reverse_lazy('task_list') 

###########################CATEGORY#################################

class CategoryList(ListView):
    model = Category

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')  
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) | Q(description__icontains=query)
            )
        return queryset

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'main/category_detail.html'
    context_object_name = 'category'

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category_delete.html'
    success_url = reverse_lazy('category_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.get_object()
        return context

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_create.html'
    success_url = reverse_lazy('category_list')    
    
class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_update.html'
    success_url = reverse_lazy('category_list') 

###########################CATEGORY#################################

class TimeLogList(ListView):
    model = TimeLog

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')  
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) | Q(description__icontains=query)
            )
        return queryset

class TimeLogDetailView(DetailView):
    model = TimeLog
    template_name = 'main/timelog_detail.html'
    context_object_name = 'timelog'

class TimeLogDeleteView(DeleteView):
    model = TimeLog
    template_name = 'timelog_delete.html'
    success_url = reverse_lazy('timelog_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['timelog'] = self.get_object()
        return context

class TimeLogCreateView(CreateView):
    model = TimeLog
    form_class = TimeLogForm
    template_name = 'timelog_create.html'
    success_url = reverse_lazy('timelog_list')    
    
class TimeLogUpdateView(UpdateView):
    model = TimeLog
    form_class = TimeLogForm
    template_name = 'timelog_update.html'
    success_url = reverse_lazy('timelog_list') 

###########################REMINDER#################################

class ReminderList(ListView):
    model = Reminder
    
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')  
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) | Q(description__icontains=query)
            )
        return queryset

class ReminderDetailView(DetailView):
    model = Reminder
    template_name = 'main/reminder_detail.html'
    context_object_name = 'reminder'

class ReminderDeleteView(DeleteView):
    model = Reminder
    template_name = 'reminder_delete.html'
    success_url = reverse_lazy('reminder_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.get_object()
        return context

class ReminderCreateView(CreateView):
    model = Reminder
    form_class = ReminderForm
    template_name = 'reminder_create.html'
    success_url = reverse_lazy('reminder_list')    
    
class ReminderUpdateView(UpdateView):
    model = Reminder
    form_class = ReminderForm
    template_name = 'reminder_update.html'
    success_url = reverse_lazy('reminder_list') 

###########################HOME#################################

def index(request):
    return render(request, 'main/index.html')

###########################REGISTER#################################

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'registration/register.html', context)
