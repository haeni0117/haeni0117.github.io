---
title:  "#14888 연산자 끼워넣기(Backtracking)"

categories:
  - Algorithm
tags:
  - [BOJ, Github, CodeTest]

toc: true
toc_sticky: true
 
date: 2021-06-25
last_modified_at: 2021-06-25

---

### 문제
N개의 수로 이루어진 수열 A1, A2, ..., AN이 주어진다. 또, 수와 수 사이에 끼워넣을 수 있는 N-1개의 연산자가 주어진다. 연산자는 덧셈(+), 뺄셈(-), 곱셈(×), 나눗셈(÷)으로만 이루어져 있다.

우리는 수와 수 사이에 연산자를 하나씩 넣어서, 수식을 하나 만들 수 있다. 이때, 주어진 수의 순서를 바꾸면 안 된다.

예를 들어, 6개의 수로 이루어진 수열이 1, 2, 3, 4, 5, 6이고, 주어진 연산자가 덧셈(+) 2개, 뺄셈(-) 1개, 곱셈(×) 1개, 나눗셈(÷) 1개인 경우에는 총 60가지의 식을 만들 수 있다. 예를 들어, 아래와 같은 식을 만들 수 있다.

- 1+2+3-4×5÷6
- 1÷2+3+4-5×6
- 1+2÷3×4-5+6
- 1÷2×3-4+5+6

식의 계산은 연산자 우선 순위를 무시하고 앞에서부터 진행해야 한다. 또, 나눗셈은 정수 나눗셈으로 몫만 취한다. 음수를 양수로 나눌 때는 C++14의 기준을 따른다. 즉, 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼 것과 같다. 이에 따라서, 위의 식 4개의 결과를 계산해보면 아래와 같다.

- 1+2+3-4×5÷6 = 1
- 1÷2+3+4-5×6 = 12
- 1+2÷3×4-5+6 = 5
- 1÷2×3-4+5+6 = 7

N개의 수와 N-1개의 연산자가 주어졌을 때, 만들 수 있는 식의 결과가 최대인 것과 최소인 것을 구하는 프로그램을 작성하시오.

### 입력
첫째 줄에 수의 개수 N(2 ≤ N ≤ 11)가 주어진다. 둘째 줄에는 A1, A2, ..., AN이 주어진다. (1 ≤ Ai ≤ 100) 셋째 줄에는 합이 N-1인 4개의 정수가 주어지는데, 차례대로 덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수이다.

### 출력
첫째 줄에 만들 수 있는 식의 결과의 최댓값을, 둘째 줄에는 최솟값을 출력한다. 연산자를 어떻게 끼워넣어도 항상 -10억보다 크거나 같고, 10억보다 작거나 같은 결과가 나오는 입력만 주어진다. 또한, 앞에서부터 계산했을 때, 중간에 계산되는 식의 결과도 항상 -10억보다 크거나 같고, 10억보다 작거나 같다.


### 문제분석
- 덧셈 2개, 뺄셈 1개, 곱셈 1개, 나눗셈 1개 -> 5P2 = 5x4x3 = 60
- 셋째줄에 합이 n-1인 4개의 정수가 주어진다는 것이 무슨 의미? A. 연산자개수(덧셈/뺄셈/곱셈/나눗셈)
- 1st line = max / 2nd line = Min

### 코드
```
n = int(input())
candidate = []
sum = 0
# 이 중에서 min값과 max값을 뽑아낼 것이다. -> 조사한 값을 저장할 리스트
a = list(map(int,input().split()))
num_of_sign = list(map(int,input().split())) #리스트로 계산부호의 수를 저장한다.
for i in range(n-1): #n-1=부호의 개수
  sum += i
  #식을 어떻게 만들지..?
```
### 참조코드(Daim's Blog)
1. recursion(재귀) 활용 방법
```
import sys
input = sys.stdin.readline #sys모듈을 사용하여 입력받는 시간을 줄였다.
def cal(num, idx, add, sub, multi, division): #숫자, 인덱스, 덧셈, 뺄셈, 곱셈, 나눗셈
    global n, maxv, minv
    if idx == n:
        maxv = max(num, maxv)
        minv = min(num, minv)
        return
    else:
        if add:
            cal(num + num_list[idx], idx + 1, add-1, sub, multi, division)
        if sub:
            cal(num - num_list[idx], idx + 1, add, sub-1, multi, division)
        if multi:
            cal(num * num_list[idx], idx + 1, add, sub, multi -1, division)
        if division:
            cal(int(num/num_list[idx]), idx + 1, add, sub, multi, division -1)
if __name__ == "__main__":
    maxv = -sys.maxsize - 1
    minv =  sys.maxsize
    n = int(input().strip()) # 숫자의 수
    num_list = list(map(int, input().strip().split()))
    a, b, c, d = map(int, input().strip().split())
    cal(num_list[0], 1, a, b, c, d)
    print(maxv)
    print(minv)
```  
