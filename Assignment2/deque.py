from collections import deque

dq = deque()

dq.append(10)
dq.append(20)
dq.append(30)
print("Deque after appending to right: ",dq)

dq.appendleft(5)
dq.appendleft(1)
print("Deque after appending to left: ",dq)

dq.pop()
print("Deque after popping to right: ",dq)

dq.popleft()
print("Deque after popping to left: ",dq)

dq.reverse()
print("Reversed Deque: ",dq)



# Deque after appending to right:  deque([10, 20, 30])
# Deque after appending to left:  deque([1, 5, 10, 20, 30])
# Deque after popping to right:  deque([1, 5, 10, 20])
# Deque after popping to left:  deque([5, 10, 20])
# Reversed Deque:  deque([20, 10, 5])