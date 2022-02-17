import collections

d = collections.deque()

d.appendleft(1)
d.appendleft(2)
d.popleft()
d.append(2)
d.pop()

print(d)
