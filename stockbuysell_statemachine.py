# not my programn, just learning approach
k = 3
prices = [3,2,6,5,0,3,0,3,0,3,2,5]

if k == 0 : print(0)
states = [-float('inf')] * (2 * k)
states[0] = -prices[0]

for price in prices:
    print("price:",price,"xxxxxxxxx")
    for i in range(2 * k):

        if i % 2 == 0:
            states[i] = max(states[i], states[i-1] - price if i > 0 else -price)
            print(i,":",states[i])
        else:
            states[i] = max(states[i], states[i-1] + price)
            print("else:",states[i])

print(states[-1])