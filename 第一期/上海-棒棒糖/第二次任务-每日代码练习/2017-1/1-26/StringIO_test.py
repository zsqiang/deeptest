from io import StringIO
f=StringIO()
f.write('hello')
f.write(' ')
f.write('word!')
print(f.getvalue())#getvalue()方法用于获得写入后的str


from io import StringIO
f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())

from io import StringIO
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
f.read()