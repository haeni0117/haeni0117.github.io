#1012유기농배추 : 첫시도
#아파트단지와 비슷한 매커니즘인 것 같다
#몇 마리의 배추흰지렁이가 필요한지 => 아파트 단지가 몇 개인지(cnt)
# 0 : 배추가 심어져 있지 않은 땅 / 1 : 배추가 심어져 있는 땅
t = int(input())
for i in range(t):
    m,n,k = map(int,input().split())
    # 해당 배추위치가 카운팅되었는지?
    visited = [[0]*m for _ in range(n)]
    # 가로 : m & 세로 : n 인 배추밭배열
    matrix = [[0]*m for _ in range(n)]
    # 배추가 심어져 있는 위치의 개수 입력받기
    for j in range(k):
        cnt=0
        x,y = map(int,input().split())
        visited[x][y]=1
        matrix[x][y]=1
        matrix[y][x]=1

#방향에 대해서 -> 좌 우 상 하
dx = [-1,1,0,0] #x축
dy = [0,0,1,-2] #y축

#cnt를 어디에 0으로 선언해야할지 모르겠다.

def couting(x,y,cnt):
    for k in range(m):
        for l in range(n):
            



