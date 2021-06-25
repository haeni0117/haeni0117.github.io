n = int(input())
xlist=[]
for i in range(n):
    x,y=map(int,input().split())
    xlist.append([x,y])
    xlist[i].append(y/x)
xlist.sort(key=lambda x :(x[2]),reverse=True)
for i in range(n):
    if i != 0:
        if(xlist[i][2]==xlist[i-1][2]):
            print(i-1,end=" ")
        else:
            print(i,end=" ")
#코드 잘못짬
n = int(input())
xlist=[]
for i in range(n):
    x,y=map(int,input().split())
    xlist.append([x,y])
xlist.sort(key=lambda x :(x[2]),reverse=True)
for i in range(len(xlist)):
    for j in range(len(xlist)):
        cnt=0
        if xlist[i][1]>xlist[j][1]:
            cnt+=1
        xlist[i].append(int(cnt))
xlist.sort(key=lambda x : (x[2]))
for i in range(len(xlist)):
   # if


 