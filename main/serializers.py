from rest_framework import serializers

# custom
from . import models


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model  = models.Task
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model  = models.Project
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)

        if self.context.get('deep', False):
            # attach tasks to a particular project
            task_instances = instance.task_set.all()
            data.update({
                'tasks': TaskSerializer(task_instances, many=True).data
            })
        return data
