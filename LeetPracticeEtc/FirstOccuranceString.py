import re

haystack=str()
needle=str()

haystack = "sadbutsbd"
needle = "sbd"

a=re.search(needle, haystack).start()

print(a)