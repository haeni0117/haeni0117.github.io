n = int(input())
cnt = 0
nums = 0
numslist = []
s = [[0]*n for _ in range(n)] #아파트존재여부
visit =  [[0]*n for _ in range(n)] #탐색여부
for i in range(1,n+1):
    for j in range(1,n+1):
        if visit[i][j]==0 and s[i][j]==1: #좌측 상단부터 탐색은 되지 않았으면서 ; 0 + 존재는 하는 ; 1 아파트구함
            visit[i][j]=1
            nums+=1
            dfs(i,j,cnt)
        
def dfs(i,j,cnt):
#방향에 대해서
#위 아래 좌 우
    for i in range(4):
        dx = [0,0,-1,1]
        dy = [1,-1,0,0]
        dx = dx[i]+i
        dy = dy[i]+1 
        if 0<=dx<=n and 0<=dy<=n:
            if s[dx][dy]==1 and visit[dx][dy]==0:
                visit[dx][dy]=1
                cnt+=1
                global numslist
                numslist.append(nums)
                nums=0 #저장했으니 초기화!
                dfs(dx,dy,cnt)

    
print(len(numslist))
for i in range(len(numslist)):
    print(numslist[i])







        
