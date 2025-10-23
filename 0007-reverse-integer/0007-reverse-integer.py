class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Define the 32-bit integer range
        INT_MAX = 2**31 - 1  # 2147483647
        INT_MIN = -2**31     # -2147483648

        # Handle the sign
        sign = -1 if x < 0 else 1
        x = abs(x)

        # Reverse the digits
        reversed_num = 0
        while x != 0:
            pop = x % 10
            x //= 10

            # Check for overflow before it happens
            if reversed_num > (INT_MAX - pop) // 10:
                return 0

            reversed_num = reversed_num * 10 + pop

        return sign * reversed_num
