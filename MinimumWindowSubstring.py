


s = "ADOBECODEBANC"
t = "ABC"

# a list to hold all possible windows
all_possible_windows=[]
# each item in the list above has start(index,value),final(index,value)
# all_possible_windows_item=[]

for count, x in enumerate(s):
    if x in t:
        all_possible_windows_item=(count,x,count,x)
        all_possible_windows.append(all_possible_windows_item)
        print(count,x)

print(len(all_possible_windows))