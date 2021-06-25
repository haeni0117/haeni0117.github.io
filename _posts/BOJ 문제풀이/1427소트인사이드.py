n = input()#처음부터 int형으로 받으면 2134가 이천백삼십사라고 인식함 
num = [int(i) for i in n]#문자열 하나씩 가져오기 -> 숫자분리
answer = num.sorted(num,reverse=True) #1234-> 4321 역순으로 순서설정
#출력
print(int(i) for i in answer