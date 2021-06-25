#solution
#n과 m 입력받기 
N, M = map(int, input().split())
visited = [False] * N  # 탐사 여부 check
out = []  # 출력 내용 -> 미리 리스트 초기화

def solve(depth, N, M):#함수선언
    if depth == M:  # 탈출 조건을 만족했을 경우
        print(' '.join(map(str, out)))  # list를 str으로 합쳐 출력 int는 join불가하기 때문
        return #여기서 return의 역할이 정확히 뭔지??? - > 공부하기 ! 

    for i in range(len(visited)):  # 탐사 check 하면서
        if not visited[i]:  # 탐사 안했다면 ex 1탐색시작한다 -> depth가 1인 것
            visited[i] = True  # 탐사 시작(중복 제거) -> 1 조사했으면 더 조사할 필요 없음 -> false값만 조사대상이기 때문에 true로 바꿔주기 
            out.append(i+1)  # 탐사 내용 out(list)에 저장하기
            solve(d  , N, M)  # 깊이 우선 탐색 저장이 끝났다는 건??? 오잉?
            visited[i] = False  # 깊이 탐사 완료
            out.pop()  # 탐사 내용 제거

solve(0, N, M)