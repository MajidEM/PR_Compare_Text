import re,sys
diff_text = sys.argv[1]
fh = open(diff_text, "r")
lines = fh.readlines()
str1 = lines[4].lstrip("-")
str2 = lines[5].lstrip("+")
if str1 != str2:
	print ("Diff found in docker images, triggering in the repositories that will recieve the updates")
else:
	print ("No diff found")
