from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


TASK_STATUS = (
    ('TODO', 'TODO'),
    ('WIP', 'WIP'),
    ('ONHOLD', 'ONHOLD'),
    ('DONE', 'DONE'),
)


class Project(models.Model):

    name        = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    client      = models.ForeignKey(to=User, on_delete=models.CASCADE)
    start_date  = models.DateField(auto_now_add=True)
    end_date    = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name
    

class Task(models.Model):

    name        = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    project     = models.ForeignKey(to=Project, on_delete=models.CASCADE)
    status      = models.CharField(max_length=250, choices=TASK_STATUS, default='TODO')

    def __str__(self):
        return self.name