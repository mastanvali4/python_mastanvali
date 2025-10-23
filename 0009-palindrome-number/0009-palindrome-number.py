class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Negative numbers are not palindrome
        if x < 0:
            return False
        
        # Convert number to string and check if it reads same forwards and backwards
        return str(x) == str(x)[::-1]
