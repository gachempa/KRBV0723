import numpy

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
        if x<len_stockDailyPrices-1 and stockDailyPrices[x]>=stockDailyPrices[x+1]:
            continue
        else:
            buy_price=stockDailyPrices[x]
            sell_price=stockDailyPrices[x]
            stockBought=True

# print("Daily price of stock = ", stockDailyPrices)
# print("Length of stockDailyPrices = ", len_stockDailyPrices)
# print("all_Trades (before collpsing) = ", all_trades)

len_trades_to_remove=len(all_trades)-numberOfTrades
# print("Trades to remove =",len_trades_to_remove)

# function to return trade with minimum profit
def min_profit_trade(all_trades):
    min_all_trades=min(all_trades, key=lambda x: x[3])
    # print("The minimum for all_trades is at",min_all_trades)
    return(min_all_trades)

# function to return collapsible_trades with "minimum loss of profit" when collapsing-trades
def min_profit_collapsible_Trades(all_trades):
    for x in range(len(all_trades)):
        collapsible_trades=[]
        # two trades can be combined if buy1<buy2 and sell1<sell2
        if x+1<len(all_trades) and all_trades[x][1]<all_trades[(x+1)][1] and all_trades[x][2]<all_trades[(x+1)][2]:
            # print("Trades", x, "and", x+1, "can be collapsed if needed")
            valueOnCollapse=(all_trades[x][3]+all_trades[x+1][3])-(all_trades[x+1][2]-all_trades[x][1])
            # print("Value on collapse:",valueOnCollapse)
            thisTradeValue=[x,x+1,valueOnCollapse]
            collapsible_trades.append(thisTradeValue)
            # print("Collapsible trades:",collapsible_trades)
            min_collapsible_trades=min(collapsible_trades, key=lambda x: x[2])
            # print("The minimum for collapsible_trades is at",min_collapsible_trades)
            return(min_collapsible_trades)

# function to remove trade with "minimum profit" from all_trades
def remove_least_profit_transaction(min_all_trades, min_collapsible_trades, all_trades):
    if (min_collapsible_trades is not None) and min_collapsible_trades[2]<min_all_trades[3]:
        # collapse the min trade[tradeindex1,tradeindex2,value]; change sell price for 1st ste, change profit, remove 2nd
        # new sell price, new profit for consolidated trade
        trade_counter=min_collapsible_trades[0]
        sell_price=all_trades[(min_collapsible_trades[1])][2]
        buy_price=all_trades[trade_counter][1]
        profit=sell_price-buy_price
        # assing new sell price to collapsed trade first, second will be deleted later
        all_trades[trade_counter][2]=sell_price
        all_trades[trade_counter][3]= profit # (all_trades[trade_counter][2])-(all_trades[trade_counter][1])
        # add the 2nd collapsible_trade to remove it later from all_trades list 
        index_trades_to_remove=(min_collapsible_trades[1])
        # print("removing collapsible trade from all_trades (index):",index_trades_to_remove)
        # remove the collapsed trade from the collapsible list
        all_trades.pop(index_trades_to_remove)
        # print("all_trades after removing (2nd) collapsible trade:", all_trades)
        return all_trades
    else:
        index_trades_to_remove = (min_all_trades[0])
        all_trades.pop(index_trades_to_remove)
        # print("all_trades after removing min_all_trades:", all_trades)
        return all_trades

if len_trades_to_remove>0:
    for x in range(len_trades_to_remove):
        min_all_trades=min_profit_trade(all_trades)
        min_collapsible_trades=min_profit_collapsible_Trades(all_trades)
        all_trades=remove_least_profit_transaction(min_all_trades,min_collapsible_trades,all_trades)

# print("Final trade list:", all_trades)

maximum_profit=0

# print("lenth of all trades:",len(all_trades))

for x in range(len(all_trades)):
    maximum_profit=maximum_profit+all_trades[x][3]
    # print("max profit is:",maximum_profit)

print(maximum_profit)