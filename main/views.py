from django.shortcuts import render, redirect
from . import urls
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.views.generic import ListView, DetailView
from main.models import Project, Task, Category, TimeLog, Reminder

# Postojeće ListView klase (bez promjena)

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

# DetailView za prikaz detalja modela
class ProjectDetailView(DetailView):
    model = Project
    template_name = 'main/project_detail.html'  # Kreirati odgovarajuću šablonu


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

# Ostale klase za ListView ostaju nepromijenjene
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

class TimelogList(ListView):
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

# Ostali funkcionalni prikazi (bez promjena)
def index(request):
    return render(request, 'main/index.html')

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
