#coding =utf -8
__author__ = 'Aimee'
import requests
#basic
r = requests.get('https://httpbin.org/basic-auth/user/passwd',auth=('user','passwd'))
print(r.text)
#方法2
from requests.auth import HTTPBasicAuth
r1 = requests.get('https://httpbin.org/basic-auth/user/passwd',auth=HTTPBasicAuth('user','passwd'))
print(r1.text)

#digest
from  requests.auth import HTTPDigestAuth
r2 = requests.get('https://httpbin.org/digest-auth/auth/user/passwd/MD5',auth = HTTPDigestAuth('user','passwd'))
print(r2.text)



