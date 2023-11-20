
# input list of stock prices, and number of trades allowed 
# for iniital testing
# actual problem will use auto-inputs from source 
stockDailyPrices = [2,3,4,5,4,3,3,5,3,6,2,4]
numberOfTrades = 2

# the size of the list or number of values provided 
len_stockDailyPrices = len(stockDailyPrices)

# all_trades is the list[list] to store [trade_counter, buy_price, sell_price, profit]
all_trades=[] # list to store all possible trades
trade_counter=0  # counter to track buy-sell sequence
stockBought = False # bool to track buy iteration step

for x in range(len_stockDailyPrices):
    if stockBought:
        if stockDailyPrices[x]>=sell_price:
            sell_price=stockDailyPrices[x]
        else:
            this_trade=[trade_counter,buy_price,sell_price,sell_price-buy_price]
            all_trades.append(this_trade)
            trade_counter=trade_counter+1
    else:
        buy_price=stockDailyPrices[x]
        sell_price=stockDailyPrices[x]
        stockBought=True

print("Daily price of stock = ", stockDailyPrices)
print("Length of stockDailyPrices = ", len_stockDailyPrices)
print("Value of all_Trades = ", all_trades)