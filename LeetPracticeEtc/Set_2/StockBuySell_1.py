prices = [7,1,5,3,6,4]
gain=0

if len(prices)<2:
    print(0)

else:
    for i in range (len(prices)-1):
        diff=max(prices[i+1:])-prices[i]
        if diff>gain: gain=diff 
    print(gain)