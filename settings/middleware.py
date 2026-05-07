import time

__all__ = (
    'ProcessTimeMiddleware',
)

class ProcessTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if hasattr(request, 'start_time'):
            elapsed = time.time() - request.start_time.timestamp()
            response['X-Process-Time'] = f'{elapsed * 1000:.2f}ms'
        return response
