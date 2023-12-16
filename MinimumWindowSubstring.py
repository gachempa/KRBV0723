


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

# pop an item from a string
def pop_from_string(the_string, pop_what):
    new_string=the_string.replace(pop_what[1], "", 1)
    return new_string

# function to find window from a specific starting point
def window_from_any_index(start_index, full_string,window_for_index):
    start_from=start_index[0]
    for x in range(start_from,len(full_string)):
        print(x)
        print(window_for_index)

# fn takes the list of all possible windows, which window index to use (index, character)
# and the window (remove the start-character then iterate and find other characters)
def create_windows(start_list,which_window_index,t_window):
    new_t_window=pop_from_string(t_window,which_window_index)
    print(new_t_window)

    # for x in range(len(start_list)-len(t_window)):
    #     print(x)

    window_from_any_index(start_list[0],start_list,new_t_window)

create_windows(all_possible_windows,all_possible_windows[1],t)

# new_t=pop_from_string(t,all_possible_windows[1])
# print(new_t)