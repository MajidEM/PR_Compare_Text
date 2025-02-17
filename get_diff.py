import re,sys
diff_text = sys.argv[1]
# index 5a49d0c..e1497ad 100644
# --- a/Dockerfile
# +++ b/Dockerfile
# @@ -1,4 +1,4 @@
# -FROM nginx:1.25-alpine3.17-slim
# +FROM nginx:1.25-alpine3.17-slim'''

text = re.split("\n", diff_text)
str1 = text[5].lstrip("-")
str2  =text[6].lstrip("+")
if str1 != str2:
	print ("Diff found in docker images, triggering in the repositories that will recieve the updates")
else:
	print ("No diff found")
