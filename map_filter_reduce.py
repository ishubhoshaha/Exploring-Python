''' python3'''

# map apply same function to each element in a list and return modified list
# map(function_that_apply_for_all_item(),list_or_iterable)

lst = [2,3,5]
x = map(lambda x: x**2,lst)
print (list(x))

# Filtering out from the sequence
# filter(function_that_apply_for_all_item(),list_or_iterable)
def check(x):
	if x<=3:
		return x
x = filter(check,lst)
print(list(x))

# Reduce function applies same operation to each items of a sequence and 
# uses the result as a first parameter of next operation. f(f(m,n),o)
# Reduce depreciated in Python3. But it can be available on 
import functools
def getsum(x,y): 
	return x+y
ans = functools.reduce(getsum, lst) 
print (ans)
filtering = functools.reduce(lambda x,y: x if x>y else y, [47,11,42,102,13]) # Getting Maximum value from list
print (filtering)
