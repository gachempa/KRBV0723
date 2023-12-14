


s = "ADOBECODEBANC"
t = "ABC"

# a list to hold all possible windows
all_possible_windows=[]

for count, x in enumerate(s):
    if x in t:
        # all_possible_windows_item=[start(index,value),final(index,value)]
        all_possible_windows_item=(count,x,count,x)
        all_possible_windows.append(all_possible_windows_item)
        print(count,x)

print(len(all_possible_windows))

# take the list of all possible windows, which window index to use (index, character)
# and the window (remove the start-character then iterate and find other characters)
def create_windows(start_list,which_window_index,t_window):
    to_pop_index=which_window_index[0]
    t_window.pop(to_pop_index)
    print(t_window)
    print(len(t_window))

create_windows(all_possible_windows,all_possible_windows[1],list(t))