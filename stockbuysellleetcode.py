
# input list of stock prices, and number of trades allowed 
# for iniital testing
# actual problem will use auto-inputs from source 
stockDailyPrices = [2,3,4,5,4,3,3,5,3,6,2,4,3,5]
numberOfTrades = 2

# the size of the list or number of values provided 
len_stockDailyPrices = len(stockDailyPrices)

# all_trades is the list[list] to store [trade_counter, buy_price, sell_price, profit]
all_trades=[] # list to store all possible trades
trade_counter=0  # counter to track buy-sell sequence
stockBought = False # bool to track buy iteration step

for x in range(len_stockDailyPrices):
    if stockBought:
        if x<len_stockDailyPrices-1 and stockDailyPrices[x]<=stockDailyPrices[x+1]:
           sell_price=stockDailyPrices[x]
        else:
            sell_price=stockDailyPrices[x]              
            this_trade=[trade_counter,buy_price,sell_price,sell_price-buy_price]
            all_trades.append(this_trade)
              
            trade_counter=trade_counter+1
            stockBought=False
    else:
        if stockDailyPrices[x]>=stockDailyPrices[x+1]:
            continue
        else:
            buy_price=stockDailyPrices[x]
            sell_price=stockDailyPrices[x]
            stockBought=True

print("Daily price of stock = ", stockDailyPrices)
print("Length of stockDailyPrices = ", len_stockDailyPrices)
print("Value of all_Trades (before collpsing) = ", all_trades)

# program below is to collapse the output down to problem's allowed trades
# capture 1st trade index, value created or lost
collapsible_trades=[]
for x in range(len(all_trades)):
    # two trades can be combined if buy1<=buy2 and sell1<sell2
    if x+1<len(all_trades) and all_trades[x][1]<=all_trades[(x+1)][1] and all_trades[x][2]<all_trades[(x+1)][2]:
        print("Trades", x, "and", x+1, "can be collapsed if needed")
        valueCreatedOnCollapse=(all_trades[x+1][2]-all_trades[x][1]-(all_trades[x][3]+all_trades[x+1][3]))
        thisTradeValue=[x,x+1,valueCreatedOnCollapse]
        print("Collapsible trade:",thisTradeValue)
    # elif (all_trades[(x+1)][2]-all_trades[x][1])>(all_trades[(x+1)][3]+all_trades[x][3]):
    #     print("")