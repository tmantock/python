def twosComplement(num):
    # Get the twos comlement of a number
    return (~num + 1)

def testComplement():
    for i in range(8):
        print i
        print twosComplement(i)
        print "------"

testComplement()