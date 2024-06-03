import re

haystack=str()
needle=str()

haystack = "sadbutsbd"
needle = "sbde"

if re.search(needle, haystack):
    print(re.search(needle, haystack).start())
else: 
    print(-1)
