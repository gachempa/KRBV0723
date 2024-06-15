s = "PAYPALISHIRING"
numRows = 6

if numRows == 1:
    print(s)

rows = [""] * numRows

add = 0
inc = 1
for i in s:
    rows[add] += i
    if add == 0:
        inc = 1
    elif add == numRows - 1:
        inc = -1

    add += inc
    
print("".join(rows)) 