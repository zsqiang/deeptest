#!/usr/bin/env python
# encoding: utf-8
import requests
from HTMLParser import HTMLParser
import re

def _attr(attrs,attrname):
	for attr in attrs:
		if attr[0] == attrname:
			return attr[1]
	return None

#解析诗的标题，作者，url
class PoemParser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.tangshi_list = []
		self.in_div = False
		self.in_a = False
		'''行宫(元稹)'''
		self.pattern = re.compile(r'''(.+)#标题 group1
									  \( #匹配作者左边的括号
									  (.+)#匹配作者group(2)
									  \) #匹配作者右边的括号
									''',re.VERBOSE)
		self.current_poem = {}

	def handle_starttag(self, tag, attrs):
		'''找到数据所在的<div>标签'''
		if tag == 'div' and _attr(attrs,'class') == 'guwencont2':
			self.in_div = True
		'''找到<div>标签下的<a>便签'''
		if self.in_div and tag == 'a':
			self.in_a = True
			self.current_poem['url'] = _attr(attrs,'href')

	def handle_endtag(self, tag):
		if tag == 'div':
			self.in_div = False

		if tag == 'a':
			self.in_a = False

	def handle_data(self,data):
		'''找到查找的数据'''
		if self.in_a:
			print data
			m = self.pattern.match(data)
			if m:
				self.current_poem['title'] = m.group(1)
				self.current_poem['author'] = m.group(2)
				self.tangshi_list.append(self.current_poem)
		self.current_poem = {}

'''解析诗的正文'''
class PoemContentParser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.content = []
		self.in_p = False

	def handle_starttag(self, tag, attrs):
		if tag == 'p' and _attr(attrs,'align') == 'center':
			self.in_p = True

	def handle_endtag(self, tag):
		if tag == 'p':
			self.in_p = False

	def handle_data(self, data):
		if self.in_p:
			self.content.append(data)


def retrive_tangshi_300():
	url = 'http://www.gushiwen.org/gushi/tangshi.aspx'
	r = requests.get(url)
	p = PoemParser()
	p.feed(r.content)
	print r.content
	return p.tangshi_list

'''根据poem的url并把诗的正文爬取出来'''
def down_poem(poem):
	url = poem['url']
	r = requests.get(url)
	p = PoemContentParser()
	p.feed(r.content)
	poem['content'] = '\n'.join(p.content)

if __name__ == '__main__':
	l = retrive_tangshi_300()
	print 'total %d poems.' % len(l)
	# download all poem
	for i in range(len(l)):
		print '%d downloading poem from: %s' % (i, l[i]['url'])
		down_poem(l[i])
		print ('标题:%(title)s\t作者:%(author)s\tURL:%(url)s\n%(content)s' % (l[i]))



