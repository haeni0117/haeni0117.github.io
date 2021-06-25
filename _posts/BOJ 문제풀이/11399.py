n = int(input())
num = sorted(map(int,input().split()))

cnt=0
for i in range(n-1,-1,-1):
    while(True):  #true아니고 True!
        cnt +=num[i]
        if i != 0:
            i -=1
        else : break

print(cnt)

