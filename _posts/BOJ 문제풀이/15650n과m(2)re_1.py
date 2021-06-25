n,m = map(int,input().split())
arr=[]
num_list = [i + 1 for i  in range(n)]
num = [False]*n
def dfs(cnt):
    if cnt == m:
        print(*arr)
        return
    for i in range(n):
        #이 코드가 구현하고 싶은 게 i값이 true면 계속 keep going하고, 아니라면(false) true값으로 바꿔가라
        if num[i] == True:
            continue
        num[i] = True
        
        #anyway 그 값이 true면 arrlist에 append한다.
        arr.append(num_list[i])
        dfs(cnt+1)
        #return 해옴
        arr.pop()
        for j in range(i+1,n):
            num[j]=False#list 종류를 아예 잘못 설정함
            

    
dfs(0)