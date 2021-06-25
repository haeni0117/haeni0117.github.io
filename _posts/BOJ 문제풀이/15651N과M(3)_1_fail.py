# 같은 수를 여러 번 골라도 된다. -> 전문제랑 차이점 !
# 입력 : 첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 7)
# 출력 : 한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.
# 수열은 사전 순으로 증가하는 순서로 출력해야 한다. "사전순 !!!!"

n,m=map(int,input().split())
arr=[]
num_list=[i+1 for i in range(n)]
exploration=[False]*n
def dfs(cnt):
    if cnt==m:
        print(*arr)
        return
    for i in range(n):
        if (exploration[i]) :
            continue
        exploration[i]==True
        arr.append(num_list[i])#중복되는 거 어떻게 푸는지 모르겠음...
        dfs(cnt+1)
        #굳이 num_list 안쓰고 i+1해도 되지 않나?
        #아 중복도 가능하다고 했는데,,,
        #for문을 하나 더 써야하지 않나?? 하나 더 써서 될 게 아님...


