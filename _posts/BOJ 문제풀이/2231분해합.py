n = int(input())
sum=999+27
for i in range(9):
    for j in range(9):
        for k in range(9):
            min(sum,i + j + k + 100*i + 10*k + k)
print(min)

#solution
# 브루트포스 문제는 단순 무식하게 접근한다.
N = int(input())
print_num = 0
for i in range(1, N+1):
    div_num = list(map(int, str(i)))
    sum_num = i + sum(div_num)
    if(sum_num == N):
        print_num = i
        break
print(print_num)