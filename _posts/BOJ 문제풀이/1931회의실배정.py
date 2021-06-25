#20210625FRI
num = int(input())
last=0
cnt=0
#last,cnt변수 만들어주는 걸 잊어버림 -> 선언해주지도 않았는데 어떻게 사용하나!
conference_data = []
for i in range(num):
  start, end = map(int, input().split())
  conference_data.append([start,end])
#conference_data 정렬하기
conference_data = sorted(conference_data,key = lambda x:x[0])
conference_data = sorted(conference_data,key = lambda x:x[1])
for i,j in conference_data:
  if i >= last:#바로 전 회의종료시간과 같거나 그 이후라면?(조건문)
    cnt += 1 #cnt를 1만큼 증가시킨다.
    last = j
print(cnt)
