'''Using Python3'''

class Love(object):
	def __init__(self, first,last):
		super(Love, self).__init__()
		self.first = first
		self.last = last
	@property
	def email(self):
		return '{}_{}@mail.com'.format(self.first.lower(),self.last.lower())
	@property
	def fullname(self):
		return '{} {}'.format(self.first,self.last)

	@fullname.setter
	def fullname(self,name):
		first,last = name.split()
		self.first = first
		self.last = last

	@fullname.deleter
	def fulllname(self):
		self.first = None
		self.last = None
		print("deleted!!!")

c = Love("Real","Madrid")
print (c.fullname)
c.first = "Royal"
print (c.fullname)
print (c.email)

c.fullname = "Cristiano Ronaldo"
print (c.fullname)
print (c.email)

del c.fulllname
print (c.fullname)
