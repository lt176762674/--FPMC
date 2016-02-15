original = raw_input("input a string:")
numbers = 0
for i in original:
    if i in ["a","e","i","o","u"]:
    	numbers += 1
    else:
        pass
print numbers	
for i in ["a","e","i","o","u"]:
	print i +" show%dtimes"%original.count(str(i))
