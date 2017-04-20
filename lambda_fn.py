'''Using Python3'''
# lambda argument: manipulate(argument)

square = lambda x : x*x
print (square(5.5))

add2val = lambda x,y : x+y
print (add2val(10,5))

lst = [x for x in range(20)]
even_number = list(filter(lambda x : x%2==0, lst))
print (even_number)

lst = [(1,3),(-5,10),(77,-3)]
lst.sort(key = lambda x:x[1])
print (lst)
