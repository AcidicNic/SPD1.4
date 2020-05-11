class Solution(object):
    def isPalindrome(self, x):
        """ Checks if the integer x is a palindrome.
        x: int
        output: bool
        """
        # If x is negative it's not a palindrome, so we skip a step and return False now!
        if x < 0:
            return False

        # convert x to a string
        x = str(x)

        # compare x to x reversed. If they are equal it's a palindrome, otherwise it's not.
        return x == x[::-1]


""" isPalindrome(121)

   var   | value 
--------------------
    x    |  121
    x    | "121"
returned | True

"""
