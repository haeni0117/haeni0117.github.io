import sys
from collections import Counter


n = int(sys.stdin.readline())
a = []
b=0
def mode(nums):
    mode_dict = Counter(nums)
    modes = mode_dict.most_common()    
    
    if len(nums) > 1 : 
        if modes[0][1] == modes[1][1]:
            mod = modes[1][0]
        else : 
            mod = modes[0][0]
    else : 
        mod = modes[0][0]

    return mod



for i in range(n):
    k = int(input())
    b+=k
    a.append(k)
a.sort()

print(b/n)
mode(a)
print(a[(n-1)/2])
 #최빈값
 #2차원배열???!!!



   
print(a[n-1]-a[0])
    