n,m,v=map(int,input().split())
s = [[0]*(n+1) for _ in range(n+1)]
visit = [0]*(n+1)
for i in range(m):
    a,b = map(int,input().split())
    s[a][b]=1
    s[b][a]=1

def dfs(v):
    print(v,end=' ')
    visit[v]=1
    for i in range(1,n+1):
        if visit[i]==0 and s[v][i]==1:
            dfs(i)

def bfs(v):
    queue = [v]
    visit[v]=0 #v는 탐색되었다.
    while(queue):
        v = queue[0]
        print(v,end=' ')
        del queue[0]
        for i in range(1,n+1):
            if visit[i]==1 and s[v][i]==1:
                queue.append(i)
                visit[i]=0 #i도 탐색완료
        
            
dfs(v)
print()
bfs(v)



