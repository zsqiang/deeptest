import time, threading
# 新线程执行的代码:
def loop():
    print('thread %s is running...' % threading.current_thread().name) #current_thread()函数，它永远返回当前线程的实例
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
        print('thread %s ended.' % threading.current_thread().name)
print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread') #创建子线程的名字,主线程实例的名字叫MainThread
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)