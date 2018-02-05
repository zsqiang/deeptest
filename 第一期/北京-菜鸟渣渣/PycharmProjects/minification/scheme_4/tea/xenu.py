#coding:utf-8
import re
import urllib2

class Xenu:
	def __init__(self):
		self.alllist=[]#记录所有链接
	def request(self,url):
		'''读取每个链接的返回内容，记入文本中'''
		try:
			request = urllib2.urlopen(url)
			html = request.read()
			txt = re.search('https?://(.+?)/',url).groups()[0]+'.txt'
			with open(txt,'w') as f:
				f.write(html)
			return txt	
		except urllib2.HTTPError,e:
			with open('xenu_12.txt','a') as f:
				f.write(url+'    '+str(e.code)+'\n')
			if re.search('https?://(.+?)/',url):
				return re.search('https?://(.+?)/',url).groups()[0]+'.txt'
		except urllib2.URLError,e:
			if re.search('https?://(.+?)/',url):
				return re.search('https?://(.+?)/',url).groups()[0]+'.txt'
	
	def code(self,url):
		'''返回每个链接的返回码'''
		try:
			code = urllib2.urlopen(url).code
			return str(code)
		except:
			pass

	def xenu(self,txt,http):
		'''从每个链接的响应body中，找出下一层链接'''
		with open(txt) as f:
			list = txt.split('.')[0]
			list = []
			for line in f:
				a = re.findall('href="(.+?)"', line)
				if a:
					if not a[0].startswith('http'):
						if a[0].startswith('/'):
							list.append(http+a[0][1:])
						elif a[0].startswith('..'):
							list.append(http+a[0][3:])
						else:
							list.append(http+a[0])
					else:
						if a[0].startswith(http):
							list.append(a[0])
						else:
							pass
				b = re.findall('src="(.+?)"', line)
				if b:
					if not b[0].startswith('http'):
						if b[0].startswith('/'):
							list.append(http+b[0][1:])
						elif b[0].startswith('..'):
							list.append(http+b[0][3:])
						else:
							list.append(http+b[0])
					else:
						if b[0].startswith(http):
							list.append(b[0])
						else:
							pass
						
				c = re.findall('url\((.+?)\)', line)
				if c:
					#print c
					for i in c:
						if i.startswith('http'):
							list.append(i)
						elif i.startswith('..'):
							list.append(http+i[2:])
						elif i.startswith('"'):
							pass
						else:
							list.append(http+'/'+i)
		self.alllist.extend(list)
		return set(list)
	
	def run(self,URl,http):
		txt = self.request(URl)
		Url = self.xenu(txt, http)
		for url in Url:
			CODE = self.code(url)
		
			print url,CODE
			
			with open('xenu_12.txt','a') as f:
				if CODE == None:
					pass
				else:
					f.write(url+'    '+CODE+'\n')
			self.passurl(url, http)
		
	def passurl(self,url,http):
		
		txt = self.request(url)
		if re.search('.css', url):
			http = re.search('(.+?).css',url).groups()[0]
	
		list = self.xenu(txt, http)
		#print list
		if len(list) != 0:
			for li in list:
				if li != http and li != http+'#' and li not in set(self.alllist):
					CODE = self.code(url)
					print li,CODE
					passurl(li, http)
					with open('xenu_12.txt','a') as f:
						if CODE == None:
							pass
						else:
							f.write(li+'    '+CODE+'\n')

if __name__ == '__main__':
	URL = 'http://www.ehaoyao.com/'#入口地址
	http='http://www.ehaoyao.com/'#主地址
	Xenu=Xenu()
	Xenu.run(URL,http)
	#request(http)