n = int(input())
c0=[1,0,1]#0의 개수
c1=[0,1,1]#1의 개수

def fibonicci(n):
    #원래 리스트(c0,c1)에서 새로운 값을 업데이트 할 수 있을 떄
    if n>=len(c0):
        #리스트업데이트과정
        for i in range(len(c0),n+1):
            c0.append(c0[i-1]+c0[i-2])
            c1.append(c0[i-1]+c0[i-2])
    print(c0[n],c1[n])
for i in range(n):
    a = int(input())
    fibonacci(n)
        