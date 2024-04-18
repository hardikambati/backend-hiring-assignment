from rest_framework import (
    views,
    status,
    permissions,
)
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

# custom
from . import (
    models,
    serializers,
)
from . import decorators as app_decorators
from utils.docs import (
    project as project_docs,
    task as task_docs,
)
from utils import helpers


class ProjectAPIView(views.APIView):
    """
    API view for project management
    """

    model_class        = models.Project
    serializer_class   = serializers.ProjectSerialier
    permission_classes = [permissions.AllowAny,]


    @swagger_auto_schema(**project_docs.LIST_PROJECT)
    def get(self, request, *args, **kwargs):
        query = self.model_class.objects.filter(
            end_date__isnull=True
        )
        id = request.query_params.get('id')
        
        context = {}
        
        if id:
            query = query.filter(id=id)
            context.update({'deep': True})

        serializer = self.serializer_class(
            query, many=True, context=context
        )
        return Response(serializer.data, status=status.HTTP_200_OK)


    @swagger_auto_schema(**project_docs.CREATE_PROJECT)
    def post(self, request, *args, **kwargs):
        data = request.data

        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(**project_docs.DELETE_PROJECT)
    @app_decorators.validate_project(lookup_key='id')
    def delete(self, request, *args, **kwargs):
        instance = kwargs['project_instance']
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class TaskAPIView(views.APIView):
    """
    API view for task management
    """

    model_class        = models.Task
    serializer_class   = serializers.TaskSerializer
    permission_classes = [permissions.AllowAny,]


    @swagger_auto_schema(**task_docs.LIST_TASK)
    def get(self, request, *args, **kwargs):
        query = self.model_class.objects.all()
        id = request.query_params.get('id')

        if id:
            query = query.filter(id=id)

        serializer = self.serializer_class(
            query, many=True
        )
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    @swagger_auto_schema(**task_docs.CREATE_TASK)
    def post(self, request, *args, **kwargs):
        data = request.data

        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(**task_docs.UPDATE_TASK)
    @app_decorators.validate_task(lookup_key='id')
    def patch(self, request, *args, **kwargs):
        instance = kwargs['task_instance']
        data = request.data
        
        helpers.pop_from_data(
            ['project', 'description', 'project'],
            data
        )

        serializer = self.serializer_class(
            instance=instance,
            data=data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(**task_docs.DELETE_TASK)
    @app_decorators.validate_task(lookup_key='id')
    def delete(self, request, *args, **kwargs):
        instance = kwargs['task_instance']
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)