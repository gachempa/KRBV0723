prices = [7,1,5,3,6,4]

min_price=prices[0]
max_profit=0

for p in prices:
    max_profit=max(max_profit,p-min_price)
    min_price=min(min_price,p)

print(max_profit)

# gain=0

# if len(prices)<2:
#     print(0)

# else:
    
#     nextMax_idx=prices.index(max(prices[1:]))
#     nextMax=prices[nextMax_idx]
#     for i in range (len(prices)-1):
#         if nextMax_idx<=i:
#             nextMax_idx=prices.index(max(prices[i+1:]))
#             nextMax=prices[nextMax_idx]
#         else:    
#             diff=nextMax-prices[i]
#             if diff>gain: gain=diff 
#     print(gain)