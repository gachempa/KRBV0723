x=121

x_s=str(x)

if len(x_s)==1:
    print("true")
else:

    loop_num=int(len(x_s)/2)

    print(loop_num)

    for i in range(loop_num):
        # print(i)
        if x_s[i]!=x_s[len(x_s)-i-1]:
            print("false")
            break
        else:
            if i==loop_num-1:
                print("true")



