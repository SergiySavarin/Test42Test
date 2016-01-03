from datetime import datetime
from .models import UsersRequest


class UserRequestMiddleware(object):
    """Save all http requests to database."""

    def process_request(self, request):
        """ All requests will be save to database in this format:
                Date       Time     Remote IP  Method Path Protocol
            [01/Jan/2016 13:01:27] [127.0.0.1]  "GET   /   HTTP/1.1"
        """
        if not request.is_ajax():
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
