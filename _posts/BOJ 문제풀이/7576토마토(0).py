from collections import deque
def bfs():
    while queue:
        #queue의 모든 요소에 대해 조사->끝날 때까지 멈추지 않는다(while)
        a,b = queue.popleft()
        #사실상 미로탐색문제의 queue[0][0],[0][1]을 꺼내오는 것과 결과적으로 같은 기능이다
        #그러나 미로탐색에서 썼던 방법(배열)보다 시간복잡도가 개선됨 -> 빠르게 코드처리가능하다
        for i in range(4):
            #다 익은 토마토의 인근토마토조사한다.
            x = a + dx[i]
            y = b + dy[i]
            #인근 토마토라고 다 되는게 아니라, 그 인근의 위치가 실제로 존재하는지
            #토마토가 존재하기는 하는지
            #토마토가 덜 익은게(0) 맞는지
            if 0<=x<n and 0<=y<m and s[x][y]==0:
                queue.append([x,y])
                s[x][y]=s[a][b]+1
                #며칠이 걸리는지 카운트하기 위해서 -> max로 최대값구해주면 된다

m,n = map(int, input().split())
s=[]
queue = deque() #데크 -> 처리시간 줄이기 위해서(시간초과방지)
#4가지 방향으로 바뀐다
dx = [-1,1,0,0]
dy = [0,0,1,-1]

for i in range(n):
    s.append(list(map(int,input().split())))
    #토마토 데이터 조사 완료

for i in range(n):
    for j in range(m):
        if s[i][j]==1:#error) n과 m이 아니라 i와 j가 index값으로 들어가야함
            queue.append([i,j])
bfs()


#나머지 조건에 대한 코드
#1. 아무리 기다려도 토마토가 익을 수 없는 조건 =-1
notyet=False
result = -2 #순수하게 비교하려고 만든값 -> 큰 의미 없음
for i in s:
    for j in i:
        if j==0:#그럼에도 덜 익은 토마토가 존재한다면?
            notyet = True
        #덜익은토마토는 존재하지 않는 상황
        result = max(result,j) 
        #익은 토마토가 하나도 없는 상황 = 모든 j가 0인 상황

if notyet == True:
    print(-1)
elif result == -1:
    print(0)
else:
    print(result - 1 )
    #가장 일반적인 케이스임
    #며칠이 걸렸나고 물었기 떄문에 이미 익어있던 토마토는 카운트에서 제외
    #result - 1


