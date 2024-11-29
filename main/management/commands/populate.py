import random
from faker import Faker
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from main.models import Project, Task, Category, TimeLog, Reminder

fake = Faker()

class Command(BaseCommand):
    help = 'Generate fake data for the app'

    def handle(self, *args, **kwargs):
        self.create_users(5)
        self.create_projects(3)
        self.create_categories(5)
        self.create_tasks(10)
        self.create_time_logs(20)
        self.create_reminders(10)
        print("Fake data generated successfully!")

    def create_users(self, count):
        for _ in range(count):
            username = fake.unique.user_name()
            email = fake.email()
            password = "testpassword"
            user = User.objects.create_user(username=username, email=email, password=password)
            print(f"Created user: {username}")

    def create_projects(self, count):
        users = list(User.objects.all())
        for _ in range(count):
            project = Project.objects.create(
                name=fake.catch_phrase(),
                description=fake.text(),
                owner=random.choice(users)
            )
            print(f"Created project: {project.name}")

    def create_categories(self, count):
        users = list(User.objects.all())
        for _ in range(count):
            category = Category.objects.create(
                name=fake.word(),
                color=fake.color(),
                owner=random.choice(users)
            )
            print(f"Created category: {category.name}")

    def create_tasks(self, count):
        projects = list(Project.objects.all())
        users = list(User.objects.all())
        for _ in range(count):
            task = Task.objects.create(
                title=fake.sentence(nb_words=6),
                description=fake.text(),
                due_date=fake.future_datetime(),
                priority=random.choice(['L', 'M', 'H']),
                status=random.choice(['P', 'IP', 'C']),
                project=random.choice(projects) if projects else None,
                assigned_to=random.choice(users) if users else None
            )
            print(f"Created task: {task.title}")

    def create_time_logs(self, count):
        tasks = list(Task.objects.all())
        for _ in range(count):
            start_time = fake.date_time_this_year()
            end_time = fake.date_time_between(start_date=start_time)  # Zamijenjeno s 'start_date'
            time_log = TimeLog.objects.create(
                task=random.choice(tasks),
                start_time=start_time,
                end_time=end_time,
                notes=fake.sentence()
            )
            print(f"Created time log for task: {time_log.task.title}")


    def create_reminders(self, count):
        tasks = list(Task.objects.all())
        for _ in range(count):
            reminder_time = fake.future_datetime()
            reminder = Reminder.objects.create(
                task=random.choice(tasks),
                reminder_time=reminder_time
            )
            print(f"Created reminder for task: {reminder.task.title} at {reminder.reminder_time}")
