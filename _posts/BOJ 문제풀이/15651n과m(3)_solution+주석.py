#source : https://wlstyql.tistory.com/59
N, M = map(int, input().split())
out = [] #출력시키기 위해서 사용하는 list
def solve(depth, N, M):
    # 해당깊이에 걸릴때만 지나는 조건(not general)
    if depth == M:
        print(' '.join(map(str, out)))
        return
    #general condition
    for i in range(N):
        out.append(i+1)#okok 0을 집어넣을 수는 없으니까
        #어어?? 내가 메커니즘에 대해서 착각한 거 같은디?? 이게 원래 중복 허용?
        #저기 위에 갔다온다고 i가 바뀌는게 아님?
        #아 미친?? 그럼  아예 0부터 다시 시작하는 거임?
        #ㅇㅇ..그럼 [1,1,1]은 그렇다치고...
        #아 한 요소가 끝나서 다시 for문을 돌면 i != i -> i += 1 !!!!
        #그럼 여기서 중요한 건 for문을 다 돌았냐의 여부겠군.. oh..큰 깨달음.
        solve(depth+1, N, M)#깊이를 바꿔본다. +1해서 
        out.pop()#저 위에 if문에서 출력되고나서야 

solve(0, N, M)