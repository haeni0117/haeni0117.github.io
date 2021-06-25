#source ; https://wlstyql.tistory.com/61
#solution01
# 전형적인 N과 M 문제인데,
# 1. 같은 수를 여러 번 골라도 되고,
# 2. 비내림차순(순열의 오른쪽 요소가 크거나 같음)
# 1.을 해결하기 위해 재귀 시 i+1이 아닌 i를 넘겨주어 같은 수도 고를 수 있게 함
# 2.를 해결하기 위해 idx 적용(N과 M(2))에서 썼던 방법 사용
N, M = map(int, input().split())
out = []
#여기까지는 다른 n과 m 문제랑 일치
def solve(depth, idx, N, M): #idx 요소가 하나 더 들어옴
    if depth == M:#목표했던 깊이(depth)와 같아지면
        print(' '.join(map(str, out)))#문자열로 바꿔서 -> 요소를 하나로 뭉친다(join) -> " "로 띄운다-> 출력!
        return #원래 위치로 돌아간다 = out.pop()
        #true/false값 대신에 idx라는 변수를 사용한듯
    for i in range(idx, N):#이 방식이 나한테는 boolean값 쓰는 것 보다 
        out.append(i+1)
        solve(depth+1, i, N, M)
        out.pop()#아까 print로 출력한 것의 가장 오른쪽 요소 삭제(pop)
solve(0, 0, N, M)