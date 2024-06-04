s = "A man, a plan, a canal: Panama"

s=''.join(char for char in s if char.isalnum()).lower()
s_rev=''.join(char for char in (list(reversed(s))))

print(s)
print(s_rev)

print(s==s_rev)