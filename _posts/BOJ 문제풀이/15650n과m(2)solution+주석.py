#solution
#대학원생이 쉽게 설명해보기
N, M = map(int, input().split())
#map으로 입력받기
num_list = [i + 1 for i in range(N)]#사실상 for i in range(1,N)과 같음
check_list = [False] * N #입력받은 숫자만큼 false리스트 개수 만들기

arr = []
# 출력시키기 위한 리스트 선언

def dfs(cnt):#dfs 알고리즘 사용
    if(cnt == M):
        #[1,2,3]
        print(*arr)# 저 *은 뭐임..?
        return#arr.pop()으로 돌아가라
    #처음부터 해당되는 조건 아니고, cnt==M일떄만 해당
    #위의 조건보다 일반적인 조건(아래)
    for i in range(0, N):
        #0,1,2,3,4,...(N-1)의 i값에 대해서 
        if(check_list[i]):#해당 i값의 check_list(boolean list)가 true일때 -> 원래는 false가 default
            continue #계속 진행한다
        
        check_list[i] = True#설사 true가 아니었다고 하더라도 ok 왜냐면 여기서 값이 뭐였든 간에 true로 만들어줄거임
        arr.append(num_list[i])#그 후 arr라는 빈 리스트에 집어넣는다 이 과정을 m이 될때까지 반복
        # dfs(cnt)에서 cnt값만 올려서 재귀(recursion)
        # 만약 M = 3이었다면 [1,2,3] -> [0,1,2]아닌 것 주의! 
        # 왜냐하면 i를 append하는 것이 아니라 num_list[i]를 append 하기 때문.
        dfs(cnt + 1)#[1,2,3]
        arr.pop()#if문 지나서 다시 왔다. 출력했으니 더 이상 필요없다. 그래서 pop() 근데 다 지우는 건 또 아님
        # 가장 오른쪽 요소만 지워준다.
        # 이 부분이 순열하고의 차이점이다.
        # 큰 나무에서 전에 봤던 것만
        # 닫아주면 된다.
        for j in range(i + 1, N):
            check_list[j] = False
            # i = 2이었기 떄문에 3부터 탐색해야함
            # 그래서 check_list[2] = false로 정의하여 더 이상 탐색할 필요가 없게 한 것임.
            # check_list[3]은 아직 true이기 때문에 for i in range(0,N)의 조사 대상이다. 
            # [1,2,3]->[1,2,4]->[1,2,5]->이 다음 과정을 모르겠다..... 
            # 결과는 n=5라면 당연히 [1,3,4]이겠지만, How!!!!!!!!???????
            # 그냥 this i는 끝났으니까 다음 index로 넘어가는건가? 일단 이렇게만 이해하고 넘어가자
        
dfs(0)