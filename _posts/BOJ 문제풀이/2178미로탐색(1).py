n,m = map(int,input().split())
s=[]
queue=[]
#4방향 탐색
dx = [0,0,-1,+1]
dy = [-1,+1,0,0]
for i in range(n):
    s.append(list(input()))
    #1010101 -> 이런 값을 각각 리스트의 요소화하기
    #주의할것: int화를 따로 하지 않았기 때문에 자료형이 string!
queue = [[0,0]] #array의 index가 0부터 시작해서 그런거임 -> 좌표 : (1,1)
s[0][0]=1 # 이건 int(1)일까? string(1)일까?
#anyway,,,, queue의 모든 요소에 대해 조사해보자 by while문
while queue:
    a = queue[0][0]
    b = queue[0][1]
        #각각 a와 b라는 변수에 값을 대입해준다.
        #a,b에 저장되었기 때문에 queue에서 삭제 by del -> 여기에 대해 조사할 필요 X
    del queue[0] 
        #queue[0][0]와 queue[0][1] 삭제
        #이제 4개의 방향에 대해 조사 : 상 하 좌 우
    for i in range(4): #4 = 방향의 개수
        x = a + dx[i] # a -> x ; updated
        y = b + dy[i] # b -> y ; updated
        if 0<=x<n and 0<=y<m and s[x][y]=="1":
            #업데이트 된 값 모두 사용하는 게 아니라 조건에 맞아야만 사용할 수 있음
            queue.append([x,y])
                #조사해야하는 것들을 모아놓은 큐값에 저장 -> 다음사이클에 탐색하게 될 것임
            s[x][y] = s[a][b]+1 
                #아마 자료형은 int? -> 확인하기
                #왜 1을 더해줘야하는지에 대해 처음에는 이해가 안갔는데 값이 업데이트됨에 따라 (경로1 > 다음경로 > 다다음경로 ... etc)
                #1을 더해주면 마지막 좌표(n,m)에서의 값 = s[n-1][m-1]
print(s[n-1][m-1])
        
        