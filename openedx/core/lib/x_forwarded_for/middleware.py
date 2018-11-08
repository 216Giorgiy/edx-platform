from django.utils.deprecation import MiddlewareMixin

class XForwardedForMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if 'HTTP_X_FORWARDED_FOR' in request.META:
            request.META['REMOTE_ADDR'] = request.META['HTTP_X_FORWARDED_FOR'].split(",")[0].strip()
            request.META['SERVER_NAME'] = request.META['HTTP_HOST']
            request.META['SERVER_PORT'] = request.META['HTTP_X_FORWARDED_PORT']
        return None
