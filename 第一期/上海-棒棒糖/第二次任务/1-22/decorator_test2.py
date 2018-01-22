def log(func):
    def wrapper():
        print('begin call')
        func()
        print('end call')
    return wrapper

@log
def myage():
    print(36)

myage()
