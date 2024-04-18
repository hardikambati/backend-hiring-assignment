from drf_yasg import openapi

# custom
from .generic import GenericResponse


LIST_TASK = {
    'operation_description': """
        GET method on `/tasks/` will return all the available \
        tasks.
    """,
    'manual_parameters': [
        openapi.Parameter(name='id', in_='query', type=openapi.TYPE_INTEGER, required=False),
    ],
    'responses': {
        200: GenericResponse.SUCCESS_RESPONSE,
        400: GenericResponse.BAD_REQUEST_RESPONSE,
        401: GenericResponse.UNAUTHORIZED_RESPONSE,
        403: GenericResponse.FORBIDDEN_RESPONSE,
        404: GenericResponse.NOT_FOUND_RESPONSE,
        500: GenericResponse.INTERNAL_SERVER_ERROR_RESPONSE
    },
    'tags': ['Task']
}


CREATE_TASK = {
    'operation_description': """
        POST method on `/tasks/` will create a new task.
    """,
    'request_body': openapi.Schema(
            title='Task POST request schema',
            type=openapi.TYPE_OBJECT,
            properties={
                'name': openapi.Schema(type=openapi.TYPE_STRING, title='name'),
                'description': openapi.Schema(type=openapi.TYPE_STRING, title='description'),
                'project': openapi.Schema(type=openapi.TYPE_INTEGER, title='project'),
            },
            required=['name', 'project'], 
    ),
    'responses': {
        201: GenericResponse.SUCCESS_RESPONSE,
        400: GenericResponse.BAD_REQUEST_RESPONSE,
        401: GenericResponse.UNAUTHORIZED_RESPONSE,
        403: GenericResponse.FORBIDDEN_RESPONSE,
        404: GenericResponse.NOT_FOUND_RESPONSE,
        500: GenericResponse.INTERNAL_SERVER_ERROR_RESPONSE
    },
    'tags': ['Task']
}


UPDATE_TASK = {
    'operation_description': """
        PATCH method on `/tasks/` will update a tasks status.
    """,
    'manual_parameters': [
        openapi.Parameter(name='id', in_='query', type=openapi.TYPE_INTEGER, required=True),
    ],
    'request_body': openapi.Schema(
            title='Task PATCH request schema',
            type=openapi.TYPE_OBJECT,
            properties={
                'status': openapi.Schema(type=openapi.TYPE_STRING, title='status',
                                         enum=['TODO', 'WIP', 'ONHOLD', 'DONE']),
            },
            required=['status'], 
    ),
    'responses': {
        201: GenericResponse.SUCCESS_RESPONSE,
        400: GenericResponse.BAD_REQUEST_RESPONSE,
        401: GenericResponse.UNAUTHORIZED_RESPONSE,
        403: GenericResponse.FORBIDDEN_RESPONSE,
        404: GenericResponse.NOT_FOUND_RESPONSE,
        500: GenericResponse.INTERNAL_SERVER_ERROR_RESPONSE
    },
    'tags': ['Task']
}


DELETE_TASK = {
    'operation_description': """
        DELETE method on `/tasks/` will permanently delete a task.
    """,
    'manual_parameters': [
        openapi.Parameter(name='id', in_='query', type=openapi.TYPE_INTEGER, required=True),
    ],
    'responses': {
        204: GenericResponse.SUCCESS_RESPONSE,
        400: GenericResponse.BAD_REQUEST_RESPONSE,
        401: GenericResponse.UNAUTHORIZED_RESPONSE,
        403: GenericResponse.FORBIDDEN_RESPONSE,
        404: GenericResponse.NOT_FOUND_RESPONSE,
        500: GenericResponse.INTERNAL_SERVER_ERROR_RESPONSE
    },
    'tags': ['Task']
}