n,k=map(int,input().split())
a=[]
num = 0 #num = 동전의 개수
for i in range(n):
    a.append(int(input()))
for i in range(n-1,-1,-1):
    if k==0: #가치의 합이 0이라면 계산중지
        break
    if m[i]>k:
        continue #가장 가치가 큰 값부터 조사했을 때, k보다 크면 그 동전은 사용하지 못하므로 다른 동전(가치가 더 낮은)에 대해 조사해야함
    #이 두 경우에 해당되지 않는다면 -> m[i]인 동전으로 k를 구성할 수 있는 상황
    num += k//m[i]
    k %= m[i]
print(num)