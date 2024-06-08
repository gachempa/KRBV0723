# not interested in bit manipulation so not completing this

n = 0b00000010100101000001111010011100

# n=int(n,2)

print(n)

n=bin(n)[2:]
print(n)
n=int(n[::-1],2)

print(n)