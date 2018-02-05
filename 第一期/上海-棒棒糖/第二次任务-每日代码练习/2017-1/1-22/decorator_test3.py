'''
写出一个@log的decorator，使它既支持：
@log
def f():
pass
又支持：
@log('execute')
def f():
pass
'''
import functools
def log(text):
   if not callable(text):
       def decorator(func):
           @functools.wraps(func)
           def wrapper(*args, **kw):
               print('%s %s:' % (text, func.__name__))
               return func(*args, **kw)
           return wrapper
       return decorator
   else:
       @functools.wraps(text)
       def wrappers(*args, **kw):
           print('call %s()' % text.__name__)
           return text(*args, **kw)
       return wrappers

@log
def now7():
    print('This is output info')

@log("execute")
def now8():
    print('This is output info')

#调用
now7()
now8()
print(now7.__name__)
print(now8.__name__)
