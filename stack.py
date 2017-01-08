class stack():
    def __init__(self):
        self.item = []
    def push(self,value):
        self.item.append(value)
    def pop(self):
        return self.item.pop()
    def top(self):
        return self.item[len(self.item)-1]
    def isEmpty(self):
        return len(self.item)==0
    def size(self):
        return len(self.item)


s=stack()

print s.isEmpty()
s.push(4)
s.push('dog')
# print(s.peek())
s.push(True)
print s.size()
print s.isEmpty()
s.push(8.4)
print s.pop()
print s.pop()
print s.size()
