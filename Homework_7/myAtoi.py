from re import sub


def myAtoi(str):
    """ return the integer representation of int
    str: str
    output: int
    """
    str = sub(" ", "", str)
    valid = "0123456789-+"
    if str[0] in valid:
        str = sub(r"[^-0-9]", "", str)
        print(str)
        result = int(str)
        if result > 2147483648:
            return 2147483648
        elif result < -2147483648:
            return -2147483648
        else:
            return result
    return 0


""" myAtoi("    -42")
   Var   |   Value
------------------------
   str   | "  -42 what"
   str   |   "-42what"
   str   |     "-42"
  result |      -42
  output |      -42
"""

