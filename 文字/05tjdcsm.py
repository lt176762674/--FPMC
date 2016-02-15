document = open("test.rtf","r")
string = str(document)
def countnumbers(string):
    strings = string.split(" ")
    #print strings
    count = len(strings)
    #print count
    print "the numbers of the word in the document is %d"%count

countnumbers(string)
