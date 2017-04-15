'''Using Python3'''

num = [1, 10, 48, 30, -7, 6, 75, 3, 0]
copy_of_num = num

sorted_list = sorted(num)  # sorted function a new sorted list
print('Sorted List:\t', sorted_list)
print("----------------------------\n")

# sort original list inplace
num.sort()
print('Sorting Original List using sort function:\t', num)
print("----------------------------\n")

num = copy_of_num
# Sort list in deascending orde
sorted_list = sorted(num, reverse=True)
print('Sorted List in deascending order:\t', sorted_list)
print("----------------------------\n")

# Unlike "Sort" function "Sorted" function can sort tuples or dictionary but return a sorted list
tup = (1, 10, 48, 30, -7, 6, 75, 3, 0)
sorted_tuples = sorted(tup)
print('Sorted Tuples:\t', tuple(sorted_tuples))
print("----------------------------\n")

# Sorted Function can sort all the keys of dictionary and list of sorted keys
info = {'name': "Shubho", 'university': "DUET", 'works_at': "BS-23", "in_love_with": "Pyhton"}
sort_dictionary = sorted(info)
print('Sorting keys of Dictionary:\t', sort_dictionary)
print("----------------------------\n")

# Sort list on basis of absolute value
num = [-7, -78, 18, -2, 0, 1, 7]
sorted_list = sorted(num, key=abs)
print("Sort list on basis of absolute value \t", sorted_list)
