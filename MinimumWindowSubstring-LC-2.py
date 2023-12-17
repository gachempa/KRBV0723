
# s = "ADOBECODEBANC"
# t = "ABC"

s="ABC"
t="BC"

if len(s)<len(t) or (len(s)==len(t) and bool(s==t)==False):
    print("")
elif s==t:
    print(s)
elif len(t)==1 and t in s:
    print(t)
else:
    the_minimum_window=""

    # a list to hold all possible windows, removes non-t alphabets
    all_possible_windows=[]

    for count, x in enumerate(s):
        if x in t:
            # all_possible_windows_item=[startindex,startvalue]
            all_possible_windows_item=(count,x)
            all_possible_windows.append(all_possible_windows_item)
            # print(count,x)

    print(all_possible_windows)

    # pop an item from a string
    def pop_from_string(the_string, pop_what):
        new_string=the_string.replace(pop_what[1], "", 1)
        return new_string

    # function to find window from a specific starting point
    def window_from_any_index(start_index, full_string,window_for_index):
        for x in range(start_index+1,len(full_string)):
            if full_string[x][1] in window_for_index:
                # print("found",full_string[x][1])
                window_for_index=pop_from_string(window_for_index,full_string[x])
                if len(window_for_index) ==0:
                    # print("Window found, end index",x)
                    return(x)
                # print(x,full_string[x])
                # print(window_for_index)

    # fn takes the list of all possible windows, which window index to use (index, character)
    # and the window (remove the start-character then iterate and find other characters)
    def create_windows(x_,all_possible_windows_,which_window_index,t_):
        new_t_window=pop_from_string(t_,which_window_index)
        # print(new_t_window)
        a=all_possible_windows_[x_]
        # print(a)

        window_end=window_from_any_index(x_,all_possible_windows_,new_t_window)
        # print("end index returned",window_end)
        return(window_end)

    # fn to create all possible windows list
    for x in range (len(all_possible_windows)):
        # this will return the end index of window
        window_end=create_windows(x,all_possible_windows,all_possible_windows[x],t)
        # print("window-end is",window_end)
        if the_minimum_window=="" and window_end is not None:
            s_start_index=all_possible_windows[x][0]
            s_end_index=all_possible_windows[window_end][0]
            the_minimum_window=s[s_start_index:s_end_index+1]
            print("min window is",the_minimum_window)
        elif window_end is not None:
            s_start_index=all_possible_windows[x][0]
            s_end_index=all_possible_windows[window_end][0]
            new_window=s[s_start_index:s_end_index+1]
            # print("min window is",new_window)
            if len(new_window)<len(the_minimum_window):
                the_minimum_window=new_window
                # print("updated new min window is",the_minimum_window)

    print(the_minimum_window)