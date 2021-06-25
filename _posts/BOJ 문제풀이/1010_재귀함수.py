#팩토리얼 함수(재귀함수 사용)
num = int(input())
def factorial2(n):
    if n==1:
         return 1
    else: 
        return n*(factorial2(n-1))
    
for i in range(num):
    a,b = map(int, input().split())
    c=factorial2(a)//(factorial2(b)*factorial2(b-a))
    print(c)