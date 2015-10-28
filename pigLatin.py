print 'Welcome to the Pig Latin Translator!'

original = (raw_input("Please type the word you wish to translate:  "))
indexMax = len(original)
    
pyg = 'ay'
result = ''

if len(original) > 0 and original.isalpha():
    original.lower()
    for i in range(1, indexMax):
        result = result + original[i]
    result = result + original[0] + pyg
else:
    print "empty"
print result
