original = raw_input("input a string:")
numbers = 0
for i in original:
    if i in ["a","e","i","o","u"]:
    	numbers += 1
    else:
        pass
print numbers	