'''using Python 3'''

lst = [00,10,20,30,40,50,60]
#index[0, 1, 2, 3, 4, 5, 6]
#inRev[-7,-6,-5,-4,-3,-2,-1]

print (lst[0])
print (lst[-1])

# list [start:end:step]
# Here end is exclusive index
print("------------------")
print (lst[-3:-1])
print (lst[4:6])
print (lst[4:-1])
#Start from 0th index to 4 index
print (lst[:5])
#Start from 4th to the end of list
print (lst[4:])

# Reverse List
print("------------------")
print (lst[::-1]) 
# Slice List from index 1 to 5 and reverse it together
print("------------------")
print (lst[-2:-6:-1])
print (lst[2:6:1])
print (lst[-2:1:-1])
#print every 2nd value of list
print("------------------")
print (lst[::2])
