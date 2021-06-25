n = int(input())
s = [[0]*n for _ in range(n)]
visited = [[0]*n for _ in range(n)]

for i in range(n):
    s[i] = map(int,input().split())
