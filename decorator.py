import time
'''
Benchmark, LimitRequest decorators
'''

def limit_request(seconds):
    def limit_request_decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            time.sleep(seconds)
            return result
        return wrapper
    return limit_request_decorator

def benchmark(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end - start))
    return wrapper


@benchmark
@limit_request(2)
def fetch_webpage(url, _headers=None):
    import requests
    # if _headers is not None:
    #     new_headers = _headers
    # else:
    #     new_headers = _headers
    new_headers = _headers if _headers is None else _headers
    webpage = requests.get(url, headers=new_headers)
    print(f'Status code: {webpage.status_code}\n headers: {webpage.request.headers}')

url = 'https://google.com'
fetch_webpage(url, _headers={'User-agent': 'Mozilla Firefox/50.0'})
