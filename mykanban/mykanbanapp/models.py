from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=[('ToDo', 'To Do'), ('InProgress', 'In Progress'), ('Done', 'Done')])

    def __str__(self):
        return self.title