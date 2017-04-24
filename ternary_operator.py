'''
Using Python3
Syntax: value_when_true if condition else value_when_false
'''
x = 5
y = 10
z = 30
print("---Max Between 2 Number---")
mx_value = x if x>y else y
print(mx_value)
print("---Max Between 3 Number---")
mx_value = (x if x>z else z) if x>y else (y if y>z else z)
print(mx_value)
