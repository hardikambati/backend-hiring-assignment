from rest_framework import (
    status,
    response,
)

# custom
from utils.helpers import (
    request_from_args,
    id_from_query_params_or_body,
)
from . import models


def validate_project(*f_args, **f_kwargs):
    """
    decorator: used for validation of a project based on `lookup_key`
    """
    def wrapper(func):
        def check(*args, **kwargs):
            request = request_from_args(args)
            lookup_key = f_kwargs.get('lookup_key')
            id = id_from_query_params_or_body(request, lookup_key)

            if not id:
                return response.Response(
                    {'detail': 'id not passed'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            projects = models.Project.objects.filter(
                id=id
            )

            if not projects.exists():
                return response.Response(
                    {'detail': 'Invalid id'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            kwargs.update({'project_instance': projects.first()})
            return func(*args, **kwargs)
        return check
    return wrapper


def validate_task(*f_args, **f_kwargs):
    """
    decorator: used for validation of a task based on `lookup_key`
    """
    def wrapper(func):
        def check(*args, **kwargs):
            request = request_from_args(args)
            lookup_key = f_kwargs.get('lookup_key')
            id = id_from_query_params_or_body(request, lookup_key)

            if not id:
                if not id:
                    return response.Response(
                        {'detail': 'id not passed'},
                        status=status.HTTP_400_BAD_REQUEST
                    )
            
            tasks = models.Task.objects.filter(
                id=id
            )

            if not tasks.exists():
                return response.Response(
                    {'detail': 'Invalid id'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            kwargs.update({'task_instance': tasks.first()})
            return func(*args, **kwargs)
        return check
    return wrapper