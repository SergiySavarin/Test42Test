from django.http import HttpResponse
from datetime import datetime

from .models import UsersRequest

class UserRequestMiddleware(object):
    """Save all http requests to database."""

    def process_request(self, request):
        request_str = '[%s] [%s] "%s %s %s"' % (
            datetime.now().strftime('%d/%b/%Y %H:%M:%S'),
            request.META['REMOTE_ADDR'],
            request.method,
            request.path,
            request.META['SERVER_PROTOCOL']
        )
        user_request = UsersRequest(request_str=request_str)
        user_request.save()
        return None
