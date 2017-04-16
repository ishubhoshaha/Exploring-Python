"""using Python3"""
from collections import deque
dq = deque("123")
print (dq)

print("--------------------")
dq.append(4)
print (dq)

print("--------------------")
dq.appendleft('0')
print (dq)

print("--------------------")
dq.pop()
print (dq)

print("--------------------")
dq.popleft()
print (dq)

print("--------------------")
dq.extend([4,5])
print (dq)

print("--------------------")
dq.extendleft([0,-1])
print (dq)

print("--------------------")
dq.rotate(1) # rotate left
print (dq)

print("--------------------")
dq.rotate(-1) # rotate right
print (dq)
