from django.db import models

class Manager(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=[('Ready', 'Ready to Work'), ('Assigned', 'Assigned Work'), ('Not Available', 'Not Available')])

    def __str__(self):
        return self.name


class Task(models.Model):
    task_name = models.CharField(max_length=255)
    assigned_to = models.ForeignKey(Manager, null=True, blank=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Completed', 'Completed')], default='Pending')

    def __str__(self):
        return self.task_name
