class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.lstrip()  # Remove leading spaces
        if not s:
            return 0

        sign = 1
        index = 0
        if s[0] == '-':
            sign = -1
            index += 1
        elif s[0] == '+':
            index += 1

        num = 0
        while index < len(s) and s[index].isdigit():
            num = num * 10 + int(s[index])
            index += 1

        num *= sign

        # Clamp to 32-bit signed integer range
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX

        return num
