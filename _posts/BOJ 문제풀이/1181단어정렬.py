n = int(input())
words=[]
word={}
for i in range(n):
    word.add(i)
for j in range(len):
    w = list(input())#문자열(단어)그 자체를 리스트로
    w.append(len(w))#글자길이를 [i][1]에 넣는다.
    words.append(w)
words.sort(key=lambda x :(x[1],x[0]))#이러면 알파벳 순?
for i in range(len(words)):
    print(words[i][0])
#문제점
#1집합은 어떻게 모든 요소를 조사하는가 cf 리스트를 for i in range사용
#2문자열의 길이에 따라 나열하는 것은 할 수 있음 but 사전순정렬은 how?

#solution1 
words_num = int(input()) #제일 첫번째 라인
words_list = [] #미리 빈 리스트 생성해서 words_list정의

for _ in range(words_num):#제일 첫 줄에서 입력받을 수로 for문 돌려 조사
    word = str(input())#입력받은 문자열 -> word
    word_count = len(word)#그 입력받은 문자열의 문자수를 word_count에 넣어준다.
    words_list.append((word, word_count))#아까 정의해뒀던 words_list에 append해준다.
    #append의 파라미터가 여러개이면 그 여러개들을 하나의 리스트의 요소에 넣는다. -> 이차원배열
#중복 삭제
words_list = list(set(words_list))
#list -> set -> list set(집합)으로 list설정

#단어 숫자 정렬 > 단어 알파벳 정렬
words_list.sort(key = lambda word: (word[1], word[0]))#lambda 뒤의 word가 의미있는 변수인가봄
#조건에 맞게 정렬
#일반적으로 그냥 sort()를 사용하면 사전순으로 정렬되나봄
for word in words_list:
    print(word[0])
#re-code
n = int(input())
words=[]
for i in range():
    word = str(input())
    length = len(word)
    words.append(word,length)
WORDS = list(set(words))
WORDS.sort(key=lambda:(x[1],x[0]))
for i in range(len(WORDS)):
    print(WORDS[i][0])
#최종코드
n = int(input())
words=[]
for i in range(n):
    word = str(input())
    length = len(word)
    words.append((word,length))
WORDS = list(set(words))
WORDS.sort(key=lambda x: (x[1],x[0]))
for i in range(len(WORDS)):
    print(WORDS[i][0])
