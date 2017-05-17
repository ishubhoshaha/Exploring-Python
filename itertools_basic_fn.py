#python2

from itertools import *
iterator = chain([1,2,3],['a','b'],[.1,.9],['x'])
print iterator
for i in iterator:
    print i
print "--izip--"
for i in izip([1,2,3],['a','b']):
    print i
print "--Cycle--"
count = 0
for i in cycle(['a','b','c']):
    if count==10:
        break
    print (count,i)
    count+=1

print "--islice(sequence,start,end,step)--"
for i in islice("ABCDEFGHIJKL",4): 
    print i
    
print "--imap(function,sequence/iterable)--"
for i in imap(lambda x:x**2,range(5)):
    print i

# unlike imap, starmap can takes input from touple
values = [(0, 5), (1, 6), (2, 7), (3, 8), (4, 9)]
for i in starmap(lambda x,y:x*y,values):
    print i


print "--dropwhile--"
values = [ -1, 0, 1, 2, 3, 4, 1, -2 ]
for i in dropwhile(lambda x: x<1, values):
    print i

print "--takewhile--"
for i in takewhile(lambda x: x<1, values):
    print i

print "--ifilter--"
for i in ifilter(lambda x: x<1, values):
    print i

print "--ifilterfalse--"
for i in ifilterfalse(lambda x: x<1, values):
    print i
