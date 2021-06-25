n,m=map(int,input().split())
visited = [False]*n
out = []

def func(depth,n,m):
    if depth == m : #지정한 depth값과 같아진다면?
        print(' '.join(map(str,out)))#2조건이맞아서(depth==m)일단 한 번 출력되기 작하면 (print) pop으롷
        #가장 오른쪽 요소 없애고 새로운 것들을 append한다. 1이 끝나면 2로 2가 끝나면 3으로 ...
        #처음 코드에서 정해준 대로 for문이 돌 것이다. 지금 코드 상에서 for문은 하나밖에 없지만, 
        #조건을 만족시키지 못할 경우 depth!=m 다시 for문을 돌리기 때문에 실질적으로 for문이 m개 라고 생각하면 된다. 
        return #코드가 중단되었던 그 자리로 다시 돌아간다
    for i in range(len(visited)):
        if visited[i]==False:
            visited[i]=True
            out.append[i+1]
            func(depth+1,n,m)
            visited=False#return되면 다시 이 라인으로 온다. 출력하면 더 이상 쓸 일 없으니 pop!
            out.pop()#list out을 초기화시키는 것이 아니라 가장 오른쪽 요소를 없애주는 pop을 하는 이유?
func(0,n,m)