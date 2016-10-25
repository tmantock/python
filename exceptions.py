def readVal(valType, requestMsg, errorMsg):
    numTries = 0
    while numTries < 4:
        val = raw_input(requestMsg)
        try:
            val = valType(val)
            return val
        except ValueError:
            print(errorMsg)
            numTries += 1
    raise TypeError('Num tries exceeded')

print readVal(int, 'Enter int: ', 'Not an int.')

try:
   readVal(int, 'Enter int: ', 'Not an int.')
except TypeError, s:
   print s
