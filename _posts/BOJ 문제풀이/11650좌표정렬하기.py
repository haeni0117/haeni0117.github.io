n = int(input())
a=[]
for i in range(n):
    x,y=map(int,input().split())
    a.append([x,y])
a.sort()
for i in a:
    print(a[i][0],a[i][1],end=" ")


##최종코드 -> 시간초과 에러
import sys 
n = int(sys.stdin.readline())
a=[]
for i in range(n):
    x,y=map(int,sys.stdin.readline().split())
    a.append([x,y])
a.sort()

for i in range(len(a)):
    print(a[i][0],a[i][1],end=" ")
    print("\n")

#solution1
import sys
n = int(sys.stdin.readline())
so = []
for i in range(n):
    so.append(list(map(int,sys.stdin.readline().split())))
    #map(int,sys.stdin.readline().split())하고난 다음에
    #so.append([x,y])는 안되나?
so.sort(key=lambda x : (x[0],x[1]))
for i in so:
    print(i[0],i[1])

#정답코드
import sys 
n = int(sys.stdin.readline())
a=[]
for i in range(n):
    x,y=map(int,sys.stdin.readline().split())
    a.append([x,y])
a.sort()

for i in range(len(a)):
    print(a[i][0],a[i][1],sep=" ")
