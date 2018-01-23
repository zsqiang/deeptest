
import functools

def log(func):
    @functools.wraps(func)   # @functools.wraps意思是wrapper.__name__ = func.__name__
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log     #等于执行了语句：now = log(now)
def now():
    print('2015-3-25')

now()

def logger(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@logger('DEBUG')   # now = log('DEBUG')(now)
def today():
    print('2015-3-25')

today()
print(today.__name__)





