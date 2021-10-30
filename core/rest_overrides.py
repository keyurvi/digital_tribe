from rest_framework.response import Response
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response:
        if hasattr(response, 'data'):
            code = response.status_code
            if 'detail' in response.data:
                response = response.data['detail']
            else:
                response = response.data
        elif hasattr(response, 'detail'):
            response = response.detail
            code = response.status_code
        return Response({'error': {'msg': response, 'code': code}, 'success': False}, status=code)
    return response


def return_success(data=None, extra_key=None, extra_value=None):
    """
    Override rest-framework's default return success response
    :param data: data that needs to return
    """
    if data or data==[]:
        if extra_key:
            return Response({'success': True, 'response': data, extra_key: extra_value})
        return Response({'success': True, 'response': data})
    return Response({'success': True})


def return_error(msg, code):
    """
    Override rest-framework's default return error response
    :param msg: data needs to return for error
    :param code: error status code
    """
    return Response({'success': False, 'error': {'message': msg, 'code': code}}, status=code)
