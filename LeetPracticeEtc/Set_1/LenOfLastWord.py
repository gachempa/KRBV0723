import re

s="   fly me   to   the moon  "

lastWord=(re.findall(r'\b\w+\b',s))[-1]

print(len(lastWord))