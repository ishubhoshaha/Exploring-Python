'''Using Python3'''

from collections import Counter
print ("---Initialization---")
lst = ['a','b','d','a','a','a','c','b','c']
counter_from_list = Counter(lst) # Can Initialize list to count unique value
print(counter_from_list)

dictionary = {'a':4,'b':2,'c':3,'d':1}
counter_from_dict = Counter(dictionary) # Can Initialize with dictionary value
print(counter_from_dict)

print(Counter(a=5,b=12)) # Can Initialize with keyword argument

print ("---Update---")
counter_from_list.update(['a'])
print (counter_from_list)

counter_from_dict.update({'b':4})
print (counter_from_dict)

print ("---Access---")
for ch in counter_from_list:
	print(ch,counter_from_list[ch])

print(list(counter_from_list.elements())) # Get back original list

# Extract all element in ascending order from counter that was actually made from dictionary
print(list(counter_from_dict.elements())) 

