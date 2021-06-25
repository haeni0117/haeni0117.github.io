#시간초과에러
import
x = int(input())
queue = []
for i in range(x):
    a = int(input())
    if a == 0:
        queue.sort()
        print(queue[0])
        del queue[0]
    else:
        queue.append(a)

