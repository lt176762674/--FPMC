word = "momomom"
count = len(word)-1
wordnew = ""
for i in range(len(word)):
	wordnew += word[count]
	count -= 1
if wordnew == word:
    print True
else:
    print False	

