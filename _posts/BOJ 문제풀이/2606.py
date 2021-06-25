com = int(input())
network = int(input())
s=[[0]*(com+1)]*(com+1)
visit = [0]*(com+1)
for i in range(network):
    a,b= map(int, input().split())
    s[a][b]=1
    s[b][a]=1
v=1
cnt = 0
#dfs함수
def dfs(v):
    visit[v]=1
    for i in range(1,com+1):
        if visit[i]==0 and s[v][i]==1:
            cnt+=1
            dfs(i)

print(cnt)

ㄸㄸㄸㄸㄸㄸㄸㄸㄸㄸㄸㄸㄸ