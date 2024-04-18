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
from utils.pagination import (
    BasicPagination,
    PaginationHandlerMixin,
)
from utils import helpers


class ProjectAPIView(views.APIView, PaginationHandlerMixin):
    """
    API view for project management
    """

    model_class        = models.Project
    serializer_class   = serializers.ProjectSerializer
    permission_classes = [permissions.AllowAny,]
    pagination_class   = BasicPagination


    @swagger_auto_schema(**project_docs.LIST_PROJECT)
    def get(self, request, *args, **kwargs):
        """
        Retrieve projects in paginated format
        """
        limit_val = request.query_params.get("limit", None)

        query = self.model_class.objects.filter(
            end_date__isnull=True
        )
        id = request.query_params.get('id')
        
        context = {}
        
        if id:
            query = query.filter(id=id)
            context.update({'deep': True})

        pagination = self.get_pagination_data(
            query, limit_val, self.serializer_class, context=context
        )
        return Response(pagination, status=status.HTTP_200_OK)


    @swagger_auto_schema(**project_docs.CREATE_PROJECT)
    def post(self, request, *args, **kwargs):
        """
        Create a project
        """
        data = request.data

        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(**project_docs.DELETE_PROJECT)
    @app_decorators.validate_project(lookup_key='id')
    def delete(self, request, *args, **kwargs):
        """
        Delete a project
        """
        instance = kwargs['project_instance']
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class TaskAPIView(views.APIView, PaginationHandlerMixin):
    """
    API view for task management
    """

    model_class        = models.Task
    serializer_class   = serializers.TaskSerializer
    permission_classes = [permissions.AllowAny,]
    pagination_class   = BasicPagination


    @swagger_auto_schema(**task_docs.LIST_TASK)
    def get(self, request, *args, **kwargs):
        """
        Retrieve tasks in paginated format
        """
        id = request.query_params.get('id')
        limit_val = request.query_params.get("limit", None)

        query = self.model_class.objects.all()

        if id:
            query = query.filter(id=id)

        pagination = self.get_pagination_data(
            query, limit_val, self.serializer_class
        )
        return Response(pagination, status=status.HTTP_200_OK)
    
    
    @swagger_auto_schema(**task_docs.CREATE_TASK)
    def post(self, request, *args, **kwargs):
        """
        Create a task
        """
        data = request.data

        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(**task_docs.UPDATE_TASK)
    @app_decorators.validate_task(lookup_key='id')
    def patch(self, request, *args, **kwargs):
        """
        Update the status of a task
        """
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
        """
        Delete a task
        """
        instance = kwargs['task_instance']
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)