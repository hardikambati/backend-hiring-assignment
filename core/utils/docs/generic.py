from drf_yasg import openapi


def base_error():
    return openapi.Schema(
        title=None,
        description=None,
        type=openapi.TYPE_OBJECT,
        properties={
            'details': openapi.Schema(type=openapi.TYPE_STRING, description="error detail"),
        }
    )


class GenericResponse:


    BASE_ERROR = base_error()

    SUCCESS_RESPONSE = openapi.Response(
        description='''
            **[Successful Request]** Indicates request was successful. 
        '''
    )

    BAD_REQUEST_RESPONSE = openapi.Response(
        description='''
            **[Bad Request]** Occurs when request data is invalid. 
        ''',
        schema=BASE_ERROR
    )

    UNAUTHORIZED_RESPONSE = openapi.Response(
        description='''
            **[Unathorized]** Occurs when the user is not authorized to perform \
            certain actions.
        ''',
        schema=BASE_ERROR
    )

    FORBIDDEN_RESPONSE = openapi.Response(
        description='''
            **[Forbidden]** Occurs when the client is not allowed to perform \
            certain actions.
        ''',
        schema=BASE_ERROR
    )

    NOT_FOUND_RESPONSE = openapi.Response(
        description='''
            **[Not found]** Occurs when a required object is not present in \
            the database.
        ''',
        schema=BASE_ERROR
    )

    INTERNAL_SERVER_ERROR_RESPONSE = openapi.Response(
        description='''
            **[Internal Server Error]** Occurs when something wrong has been \
            ocured at the server end.
        ''',
        schema=BASE_ERROR
    )

    UNSUPPORTED_MEDIA_TYPE = openapi.Response(
        description='''
            **[Unsupported Media Type]** Occurs when the payload format is an \
            unsupported format.
        ''',
        schema=BASE_ERROR
    )