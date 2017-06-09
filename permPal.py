# Palindrom Permutation Question from CTCI


def permutationPalindrome(string):
    # Check for edge cases
    if string is None:
        return False
    # If the string is equal to one, then it is a Palindrome
    if len(string) == 1:
        return True
    # Create a set to store unique values. Any duplicates will be removed
    s = set(string)
    # Check if the len of the string is greater than half the string plus one
    # The idea is that that a Palindrome will have pairs of characters, with at
    # most one character being single. If this is not the case, it is not a 
    # Palindrome
    # Time Complexity of O(1) - A constant time conditional check
    # Space Complexity:
    #   - Worst case: O(n) - all characters are unique and a set of all
    #     characters have been created
    #   - Best case: O(n/2)
    if len(s) > (len(string) / 2) + 1:
        return False

    return True

print permutationPalindrome("mmo")
print permutationPalindrome("travel")
print permutationPalindrome("uttugg")
print permutationPalindrome("troy")
