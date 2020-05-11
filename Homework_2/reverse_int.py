class Solution():
    def reverse(self, x):
        """ reverses the int x
        x: int
        output: int
        """
        # reverses negative x value
        if x < 0:
            x = int(str(x * -1)[::-1]) * -1
        # reverses positive x value
        else:
            x = int(str(x)[::-1])

        # checks if x exceeds the limit so leetcode doesnt complain.
        if x > 2147483648 or x < -2147483648:
            return 0
        return x
