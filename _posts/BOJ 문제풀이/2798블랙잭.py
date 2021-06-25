#solution
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = len(a)
sum = 0
for i in range(0, b - 2):
        for j in range(i + 1, b - 1):
                for k in range(j + 1, b):
                        if a[i] + a[j] + a[k] > m:
                                continue
                        else:
                                sum = max(sum, a[i] + a[j] + a[k])
print(sum)
#구조는 정말 단순한데 세 개를 고르려면 
# for i in range(0, b - 2): for j in range(i + 1, b - 1): for k in range(j + 1, b):
# 이 아이디어를 알고 있느냐 아니냐가 중요할 듯

#mycode
n,m=map(int,input().split())
cards = list(map(int,input().split()))
k = len(cards)
for i in range(0,k-2):
    for j in range(1,k-1):
        for l in range(2,k):
            if cards[i]+cards[j]+cards[l] > m:
                continue#pass -> 반복문으로 돌악나
            else:
                answer = max(answer,cards[i]+cards[j]+cards[l])#계속 업데이트되면서 비교
                
print(answer)