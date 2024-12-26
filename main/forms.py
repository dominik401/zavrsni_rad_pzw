from django import forms
from .models import Project, Task, Reminder, TimeLog, Category

class ProjectForm(forms.ModelForm):
    created_at = forms.DateTimeField(disabled=True, required=False)
    updated_at = forms.DateTimeField(disabled=True, required=False)

    class Meta:
        model = Project
        fields = '__all__' 
        exclude = ['created_at']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['created_at'].initial = self.instance.created_at
            self.fields['updated_at'].initial = self.instance.updated_at


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'priority': forms.Select(attrs={'type': 'string'}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'color', 'owner']
        widgets = {
            'color': forms.TextInput(attrs={'type': 'string'}),
            'owner': forms.TextInput(attrs={'type': 'string'})
        }

class TimeLogForm(forms.ModelForm):
    class Meta:
        model = TimeLog
        fields = ['task', 'start_time', 'end_time', 'notes']
        widgets = {
            'start_time': forms.DateInput(attrs={'type': 'date'}),
            'end_time': forms.DateInput(attrs={'type': 'date'}),
            'notes' : forms.Textarea(attrs={'type': 'string'})
        }

class ReminderForm(forms.ModelForm):
    created_at_display = forms.DateTimeField(
        label='Created At',
        required=False,
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )
    class Meta:
        model = Reminder
        fields = ['task']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['created_at_display'].initial = self.instance.created_at


    


