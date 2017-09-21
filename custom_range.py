#python2
'''
  Custom range() function which can be used in for loop to iterate throgh specific range
'''
class CustomRange:

    def __init__(self,limit):
        self.limit = limit

    def __iter__(self):
        self.counter = 0
        return self

    def next(self):
        index = self.counter
        if self.counter >= self.limit:
            raise StopIteration
        self.counter = self.counter + 1

        return index


for index in CustomRange(10):
    print index
