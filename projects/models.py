from django.db import models
import uuid

# Create your models here.

TASK_STATUS = (('not_started', 'Not Started'),
               ('in_progress', 'In Progress'),
               ('completed', 'Completed'))


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    unique_id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.title


class Task(models.Model):
    summary = models.CharField(max_length=100)
    content = models.TextField(max_length=500)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.CharField(choices=TASK_STATUS, max_length=20)

    # position of the task on the board
    positionX = models.IntegerField(default=0)
    positionY = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.summary} : {self.project.title}'


class Note(models.Model):
    content = models.TextField(max_length=500)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    # position of the note on the board
    positionX = models.IntegerField(default=0)
    positionY = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title} : {self.project.title}'

class Text(models.Model):
    content = models.TextField(max_length=500)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    # position of the text on the board
    positionX = models.IntegerField(default=0)
    positionY = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.content} : {self.project.title}'