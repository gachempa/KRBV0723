
# input list of stock prices, and number of trades allowed 
# for iniital testing
# actual problem will use auto-inputs from source 
stockDailyPrices = [2,3,4,5,4,3,3,5,3,6,2,4]
numberOfTrades = 2

# the size of the list or number of values provided 
len_stockDailyPrices = len(stockDailyPrices)

# the list[list] to store [buy_counter, all_trades, buy_price, sell_price, profit]

buy_counter=0  # counter to track buy sequence
all_trades=0 # counter to track number of possible trades

print("Daily price of stock = ", stockDailyPrices)
print("Length of stockDailyPrices = ", len_stockDailyPrices)