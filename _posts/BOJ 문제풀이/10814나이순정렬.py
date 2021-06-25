#1st code
n = int(input())
pp=[]
for i in range(n):
    age,name = map(input().split())
    age=int(age)
    #나이가 같으면 가입한 순으로 -> 가입한 순으로 이미 정렬되어 있으므로 추가적 코드조작 필요없음
    pp.append([age,name])
pp.sort(key=lambda x : x[0])
for i in range(len(pp)):
    print(pp[i][0],pp[i][0],sep=" ")

#2nd code 
# int가 없어서 map이 의미가 없음 -> 런타임에러
# print(pp[i][0],pp[i][0],sep=" ") -> print(pp[i][0],pp[i][1],sep=" ")
n = int(input())
pp=[]
for i in range(n):
    age,name = input().split()
    age = int(age)
    #나이가 같으면 가입한 순으로 -> 가입한 순으로 이미 정렬되어 있으므로 추가적 코드조작 필요없음
    pp.append((age,name))
pp.sort(key=lambda x : x[0])
for i in range(len(pp)):
    print(pp[i][0],pp[i][1],sep=" ")