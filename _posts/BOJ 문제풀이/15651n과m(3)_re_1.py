n,m=map(int,input().split())
arr=[]
def dfs(depth,n,m):
    if depth==m:
        print(map(str,arr),end=" ")#아아 end는 문자열에서만 사용할 수 있써!!!
        return
    for i in range(n):
        arr.append(i+1)
        dfs(depth+1,n,m)
        arr.pop()
        #이렇게 끝 아님? 
        # ->  오오오오ㅗ오 맞아 ㅋㅋㅋㅋㅋㅋㅋ 굿굿
    
dfs(0,n,m)
#백준에서 돌렸더니 틀림... 어디가 틀린거지..?
#다시수정 
#정답처리까지 완료
