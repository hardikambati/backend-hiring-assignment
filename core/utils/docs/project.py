from drf_yasg import openapi

# custom
from .generic import GenericResponse


LIST_PROJECT = {
    'operation_description': """
        GET method on `/projects/` will return all the available \
        projects.
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
    'tags': ['Project']
}


CREATE_PROJECT = {
    'operation_description': """
        POST method on `/projects/` will create a new Project.
    """,
    'request_body': openapi.Schema(
            title='Project POST request schema',
            type=openapi.TYPE_OBJECT,
            properties={
                'name': openapi.Schema(type=openapi.TYPE_STRING, title='name'),
                'description': openapi.Schema(type=openapi.TYPE_STRING, title='description'),
                'client': openapi.Schema(type=openapi.TYPE_INTEGER, title='client'),
            },
            required=['name', 'client'], 
    ),
    'responses': {
        201: GenericResponse.SUCCESS_RESPONSE,
        400: GenericResponse.BAD_REQUEST_RESPONSE,
        401: GenericResponse.UNAUTHORIZED_RESPONSE,
        403: GenericResponse.FORBIDDEN_RESPONSE,
        404: GenericResponse.NOT_FOUND_RESPONSE,
        500: GenericResponse.INTERNAL_SERVER_ERROR_RESPONSE
    },
    'tags': ['Project']
}


DELETE_PROJECT = {
    'operation_description': """
        DELETE method on `/projects/` will permanently delete a Project.
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
    'tags': ['Project']
}