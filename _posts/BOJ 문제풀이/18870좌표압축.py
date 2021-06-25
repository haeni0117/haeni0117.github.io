#1st
n = int(input())
num_list = list(map(int,input().split()))
#중복허용아닌걸 알 수 있음 -> example2
num_list2=list(set(num_list)) #중복제거
#문제가 뭔소린지...
#수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.
# Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표의 개수와 같아야 한다.
# X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.
#okay 이해했음
for i in range(len(num_list2)):
    cnt=0
    for j in range(len(num_list2)):
        if num_list2[i]>num_list2[j] :
            cnt+=1
            #문제! 어떻게 다시 원래 리스트에 집어넣을까...?
        for k in range(n):
            if num_list[k]==num_list2[i]:
                num_list[k].append(cnt)

for i in range(n):
    print(num_list[i][1],end=" ")  
        

#2nd
n = int(input())
num_list = map(int,input().split())
num_list3 = []
#중복허용아닌걸 알 수 있음 -> example2
num_list2=list(set(num_list)) #중복제거
#문제가 뭔소린지...
#수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.
# Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표의 개수와 같아야 한다.
# X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.
#okay 이해했음
for i in range(len(num_list2)):
    cnt=0
    for j in range(len(num_list2)):
        if num_list2[i]>num_list2[j] :
            cnt+=1
            #문제! 어떻게 다시 원래 리스트에 집어넣을까...?
        for k in range(n):
            if num_list[k]==num_list2[i]:
                num_list3.append((num_list[k],cnt))

for i in range(n):
    print(num_list3[i][1],end=" ")  

#3rd => 원하는 포맷으로 답이 나오긴 했는데 틀린 답...
n = int(input())
num_list = list(map(int,input().split()))
num_list3 = []
#중복허용아닌걸 알 수 있음 -> example2
num_list2=list(set(num_list)) #중복제거
#문제가 뭔소린지...
#수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.
# Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표의 개수와 같아야 한다.
# X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.
#okay 이해했음
for i in range(len(num_list2)):#중복 제거된 리스트
    #새롭게 i조사할 때마다 cnt값 초기화
    cnt=0
    for j in range(len(num_list2)):
        if num_list2[i]>num_list2[j] :
            cnt+=1
            #문제! 어떻게 다시 원래 리스트에 집어넣을까...?
            #이제 cnt값 조사완료
        for k in range(n):
            if num_list[k]==num_list2[i]:
                num_list3.append((num_list[k],cnt))

for i in range(n):
    print(num_list3[i][1],end=" ")  

#solution
n=int(input())
x=list(map(int,input().split()))
xt=list(sorted(set(x)))#여기까지는 중복제거리스트
#여기까지는 내가 원래 짠 코드에도 있던 내용
#딕셔너리(dictionary)
xt={xt[i]:i for i in range(len(xt))}
#딕셔너리를 만드는 건 상상도 못함 ㄴㅇㄱ => 태그 생성
print(*[xt[i] for i in x])
#예제로 따지면 for i in x => 2 4 -10 4 -9
#key가 2 4 -10 4 -9 얘네일 때의 value출력 !!
#와우 훨씬 효율적이다 -> 항상 중복되는 것들 제거하면 중복되는것리스트 // 중복되지 않는 리스트 두 개 만들어서 if문으로 비교했는데... 
#딕셔너리가 있는데 왜 그렇게 접근했을까....!! 
# ---> 이 문제의 핵심은 "딕셔너리"

#mycode
n = int(input())
nlist = list(map(int,input().split()))
nlist2=list(sorted(set(nlist)))#sorted해주는 이유는? -> 딕셔너리로 쓰려고 + 그리고 지금 집합 아니고 리스트다 !
nlist2= {nlist2[i]:i for i in range(len(nlist2))}
print(*[nlist2[i] for i in nlist])
