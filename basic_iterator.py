#python2

'''
    Any class can be defined as iterator if it has __iter__ and __next__ ( next() in python2 )method in order to implement
    iterator protocol inside class
'''

class Fibonacci:

    number_showed = 1
    def __init__(self,max_limit):
        self.max_limit = max_limit

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def next(self):
        fib = self.a
        if Fibonacci.number_showed>self.max_limit:
            raise StopIteration
        self.a, self.b = self.b, self.a+self.b
        Fibonacci.number_showed = self.number_showed+1
        return fib

counter = 0
for i in Fibonacci(10):
    counter  = counter+1
    print '{}-> {}'.format(counter,i)
