"""using Python3"""
from collections import deque
dq = deque("123")
print (dq)

print("--------------------")
dq.append(4) # append to end
print (dq)

print("--------------------")
dq.appendleft('0') # append on 0th postion
print (dq)

print("--------------------")
dq.pop() # Pop from end
print (dq)

print("--------------------")
dq.popleft() # pop from 0th postion
print (dq)

print("--------------------")
dq.extend([4,5]) # append a list to end of dq
print (dq)

print("--------------------")
dq.extendleft([0,-1]) # append a list at begining
print (dq)

print("--------------------")
dq.rotate(1) # rotate left
print (dq)

print("--------------------")
dq.rotate(-1) # rotate right
print (dq)
