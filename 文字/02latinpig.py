pyg = 'ay'

original = raw_input('Enter a word:')
word = original.lower()
if len(word) > 0 and word.isalpha():
    print word
else:
    print 'empty'
first = word[0]
new_word = word[1:len(word)] + first + pyg
print new_word