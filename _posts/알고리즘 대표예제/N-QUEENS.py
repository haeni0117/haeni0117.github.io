
def DFS(N,current_row,current_candidate,final_result):#다음행을 재귀적으로 호출하기 위해서
    if current_row==N#조사가 완료되었을 경우 -> 종료조건
    #current_row : 재귀적호출을 위한 목적
    #current_candidate : 이미 결정된 위치에 관한 데이터
    #N*N의 정사각형에서 퀸이 어떻게 움직이는지에 대한 내용
    #한 줄에 하나의 퀸 ex) 4*4에서는 4개의 퀸 -> 그리고 각각 한 줄에 1개의 퀸 현재 마지막줄까지(nth line)조사가 완료되었다면 문제풀이가 끝난 것
        final_result.append(current_candidate)#끝까지 왔으니까 결과값에 current_candidate값 저장
        return
    #조사가 완료되지 않았을 경우
    for candidate_col in range(N):#N개의 열이있고 그걸 index 0부터 체크하겠다.
        if is_available(current_candidate,candidate_col):#pruning ! #수직체크 & 대각선체크를 위해서
            current_candidate.append(candidate_col)
            DFS(N, current_row+1, current_candidate, final_result)#current_row+1=재귀적 탐색을 위해
        #current_candidate : 이미 배치된 퀸의 정보


def solve_n_queens(N):
    final_result = []#결과값 저장
    DFS(N,0,[],final_result)#0 -> 0번째 열부터 조사시작
    return final_result#결과값(final_result)를 리턴한다.

    # 1. 정답을 어떻게 체크해서 저장할 것인가?
    # 2. 어떻게 경우의 수를 체크하느냐?
