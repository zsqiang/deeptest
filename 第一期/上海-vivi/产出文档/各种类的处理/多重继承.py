###类

##既能检查参数，又可以用类似属性这样简单的方式来访问类的变量
     @property:
	 
###多重继承：
  class Animal(object):
  	pass

#哺乳类与鸟类继承动物类	
  class Mammal(Animal):
  	pass
  
  class Bird(Animal):
  	pass
  	
  class Runnable(object):
  	def run(self):
  		print('Running…………')
  		
  class Flyable(object):
  	def fly(self):
  		print('Flying…………')

#狗狗跟蝙蝠既属于哺乳类	，也属能跑类：
  class Dog(Mammal, Runnable):
  	pass
  	
  class Bat(Mammal, Runnable):
  	pass

#鹦鹉跟鸵鸟既属于鸟类，也属能飞类：	
  class Parrot(Bird, Flyable):
  	pass
  	
  class Ostrich(Bird, Flyable):
  	pass
	
	
	