# 문제잘못파악 & 어떻게 접근해야할지모르겠음
# 세로와 가로
m,n = map(int,input().split())
s = [[0]*n for _ in range(m)] #가로 * 세로
for i in range(m):
    k = list(map(int,input()))
    for j in range(n):
        s[i][j] = list[j]
        #미로세팅완료
#세팅된 미로에서 탐색시작
for i in range(m):
    for j in range(n):
        if s[i][j]==1:
            #bfs방식 탐색
            bfs(i,j)
            #i -> m j->n

def bfs(x,y):
    while queue:
        queue = [[x,y]] 
        a = queue[0][0]
        b = queue[0][1]
        #새로운 변수인 a와 b에 파라미터값 저장
        del queue[0]
        for i in range(4):
            #앞뒤좌우 방향설정
           dx = [0,0,-1,1]
           dy = [-1,1,0,0]
           #x와 y가 가로인지 세로인지 헷갈린다.....
           x=a+dx[i]
           y=b+dy[i]
           if 0<=x<m and 0<=x<n and s[m][n]==1:
               queue.append([m,n])
               s[m][n]=0

        #queue리스트 생성
    for i in range(m):
       for j in range(n):
           
           

          if s[i][j]==1:
