num=input().split('-')
for i in range(len(num)):
    if i==0:
        a = map(int,num[i].split('+'))
        cnt=sum(a)
       
            
            
    else:
        b = map(int,num[i].split('+'))
        cnt -=sum(b)

print(cnt)