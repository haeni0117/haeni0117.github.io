cities = int(input())
distance = list(map(int,input().split()))
oil_price = list(map(int,input().split()))
money = oil_price[0]*distance[0]
for i in range(1,cities-1):
    
    if oil_price[i-1]>=oil_price[i]:
        money+=oil_price[i]*distance[i]
    else:
        oil_price[i]=oil_price[i-1]
        money+=oil_price[i]*distance[i]
  
    
print(money)
               