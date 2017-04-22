'''
Using Python3
'''
def qubes(nums):
	for i in nums:
		t = i + i +i;
		yield (t)

result = qubes([1,2,3,4])

print (next(result)) # Get first value
print ("-----------")
for i in result: # Gets remaing 3 as we provide the list of size 4
	print (i)

print("---Another way to declare generator---")
result = (x*x for x in [1,2,3,4])
print (result)
print (list(result)) # Convert into list

for i in result: # This will not iterate as we already generate the value using above list convertion
	print (i)


print ("--- Fibonacci Series using Generator---")

def fibonacci_series(series_range):
	a = 0 
	b = 1
	for i in range(series_range):
		yield a
		a , b = b, a+b

fibo = fibonacci_series(10)
print(list(fibo))
