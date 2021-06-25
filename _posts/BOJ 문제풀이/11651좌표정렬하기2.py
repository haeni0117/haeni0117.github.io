#11650 코드를 정렬우선순위만 변경하면 될듯

#1st
import sys 
n = int(sys.stdin.readline())
a=[]
for i in range(n):
    x,y=map(int,sys.stdin.readline().split())
    a.append([x,y])
a.sort(key=lambda x : (x[1],x[0]))

for i in range(len(a)):
    print(a[i][0],a[i][1],sep=" ")
