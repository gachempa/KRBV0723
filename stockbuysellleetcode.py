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
        if stockDailyPrices[x]>=stockDailyPrices[x+1]:
            continue
        else:
            buy_price=stockDailyPrices[x]
            sell_price=stockDailyPrices[x]
            stockBought=True

print("Daily price of stock = ", stockDailyPrices)
print("Length of stockDailyPrices = ", len_stockDailyPrices)
print("all_Trades (before collpsing) = ", all_trades)

# use maxplus_... to replace profit of trades to be deleted later (net few "codes")
maxplus_all_trades=max(all_trades, key=lambda x: x[2])[2]*10000
# the higher artificial profit will prevent trades from being picked up as minimums (later)
print("The max+1 of sell prices is:",maxplus_all_trades)

# program below is to collapse the output down to problem's allowed trades
# capture 1st trade index, value created or lost
collapsible_trades=[]
for x in range(len(all_trades)):
    # two trades can be combined if buy1<buy2 and sell1<sell2
    if x+1<len(all_trades) and all_trades[x][1]<all_trades[(x+1)][1] and all_trades[x][2]<all_trades[(x+1)][2]:
    #    print("Trades", x, "and", x+1, "can be collapsed if needed")
        valueOnCollapse=(all_trades[x][3]+all_trades[x+1][3])-(all_trades[x+1][2]-all_trades[x][1])
        thisTradeValue=[x,x+1,valueOnCollapse]
        collapsible_trades.append(thisTradeValue)
print("Collapsible trades:",collapsible_trades)

# we have to remove trades if allowed trades is smaller than all possible trades
index_trades_to_remove=[] # to collect indices to remove in final step
len_trades_to_remove=len(all_trades)-numberOfTrades
print("Trades to remove =",len_trades_to_remove)
        
if len_trades_to_remove>0:
    for x in range(len_trades_to_remove):
        # which step to remove? find the "minimum-loss" from the two lists, compare and remove the smaller loss
        # the minimum loss trade in all_trades possible
        min_all_trades=min(all_trades, key=lambda x: x[3])
        print("The minimum for all_trades is at",min_all_trades)

        if len(collapsible_trades)>0:
            # the minimum loss consolidation 
            min_collapsible_trades=min(collapsible_trades, key=lambda x: x[2])
            print("The minimum for collapsible_trades is at",min_collapsible_trades)
        
            if min_collapsible_trades[2]<min_all_trades[3]:
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
                index_trades_to_remove.append(min_collapsible_trades[1])
                print("removing collapsible trade:",min_collapsible_trades)
                # remove the collapsed trade from the collapsible list
                print("all_trades to remove is at x[1] of:", min_collapsible_trades)
                # set profit of remove-trade to max+1 (trade will be removed later from all_trade list)
                # this will remove it from future considerations in this loop
                all_trades[(min_collapsible_trades[1])][3] = maxplus_all_trades
                print("The collapsed trade - with maxplus value",all_trades[(min_collapsible_trades[1])])
                all_trades.pop(collapsible_trades.index(min_collapsible_trades))
                # remove the collapsed trade from the collapsible list                
                collapsible_trades.pop(collapsible_trades.index(min_collapsible_trades))
            else:
                # add to index to remove later
                index_trades_to_remove.append(min_all_trades[0])
                all_trades.pop(all_trades.index(min_all_trades))
            
print("The indices to remove from all trades:",index_trades_to_remove)
print("The final all_trades list: ",all_trades)
#    all_trades.pop(min_collapsible_trades[1]) # after this step, existing indices will be wrong



