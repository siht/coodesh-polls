import time

__all__ = (
    'ProcessTimeMiddleware',
)


class ProcessTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time.perf_counter()
        response = self.get_response(request)
        elapsed = time.perf_counter() - start
        response['X-Process-Time'] = f'{elapsed * 1000:.2f}ms'
        return response
