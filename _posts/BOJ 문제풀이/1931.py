n = int(input()) #회의실개수

array = [[0]*2]*n
for i in range(n):
    start, end = map(int,input().split())
    array[i][0]=start
    array[i][1]=end
   #각 case(i)에 따른 start,end값을 2차원배열에 저장
array.sorted(key=lambda x:(x[1],x[0]))
#(key=lambda 주의하기) 2번째 인자 -> 1번째 인자 순서로 오름차순배열
end_time = array[0][1]
cnt=1#cnt는 0이 아니라 1이다 !!!
for i in range(1,n):
    if array[i][0]>=end_time:
        cnt +=1
        end_time=array[i][1]
print(cnt)



    





