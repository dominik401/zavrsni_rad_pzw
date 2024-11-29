from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    """Model za upravljanje projektima."""
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projects")

    def __str__(self):
        return self.name


class Task(models.Model):
    """Model za upravljanje zadacima."""
    PRIORITY_CHOICES = [
        ('L', 'Low'),
        ('M', 'Medium'),
        ('H', 'High'),
    ]

    STATUS_CHOICES = [
        ('P', 'Pending'),
        ('IP', 'In Progress'),
        ('C', 'Completed'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateTimeField(null=True, blank=True)
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default='M')
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='P')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="tasks", null=True, blank=True)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="tasks")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    """Model za organiziranje zadataka po kategorijama."""
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=7, default="#FFFFFF")  # HEX kod boje
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="categories")

    def __str__(self):
        return self.name


class TimeLog(models.Model):
    """Model za praćenje vremena provedenog na zadacima."""
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="time_logs")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.task.title} - {self.start_time} to {self.end_time or 'In Progress'}"


class Reminder(models.Model):
    """Model za podsjetnike vezane uz zadatke."""
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="reminders")
    reminder_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reminder for {self.task.title} at {self.reminder_time}"
