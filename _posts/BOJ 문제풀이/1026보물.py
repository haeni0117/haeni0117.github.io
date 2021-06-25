#20210625FRI
sum = 0 #최솟값 저장하는 변수(누적)
num = int(input())#정수배열의 길이
A = list(map(int,input().split()))
B = list(map(int,input().split()))
for i in range(num):
  sum += min(A)*max(B)
  A.pop(A.index(min(A)))
  B.pop(B.index(max(B)))
print(sum)
