from django.contrib import admin
from . import models

admin.site.register([
    models.Project,
    models.Task,
])

