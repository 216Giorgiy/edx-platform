from django.utils.deprecation import MiddlewareMixin

class XForwardedForMiddleware(MiddlewareMixin):

    def process_request(self, request):
        for field,header in [("HTTP_X_FORWARDED_FOR","REMOTE_ADDR"), ("HTTP_HOST","SERVER_NAME"), ("HTTP_X_FORWARDED_PORT","SERVER_PORT")]:
            if field in request.META:
                request.META[header] = request.META[field]
        return None
