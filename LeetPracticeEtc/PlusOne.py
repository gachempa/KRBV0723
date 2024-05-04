digits = [1,2,3]

digits=str([int("".join([str(i) for i in digits]))+1][0])
print(digits)
digits=[int(i) for i in digits]

print(digits)

# s_digits="".join(s_digits)

# print(s_digits)