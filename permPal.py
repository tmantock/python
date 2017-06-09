def permutationPalindrome(string):
    if string is None:
        return False
    if len(string) == 1 or len(string) == 2:
        return True
    singleOccurence = 0
    instances = {}
    for i in range(len(string)):
        if string[i] in instances:
            instances[string[i]] += 1
        else:
            instances[string[i]] = 1
    for k, v in instances.iteritems():
        if v == 1:
            singleOccurence += 1
    return True if singleOccurence <= 1 else False

print permutationPalindrome("mmo")
print permutationPalindrome("travel")
# print permutationPalindrome("")
