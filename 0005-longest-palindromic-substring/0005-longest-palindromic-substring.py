class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""

        start, end = 0, 0  # To store best palindrome indices

        def expand_from_center(left, right):
            # Expand while the characters match
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the palindrome length
            return right - left - 1

        for i in range(len(s)):
            len1 = expand_from_center(i, i)       # Odd length palindrome
            len2 = expand_from_center(i, i + 1)   # Even length palindrome
            length = max(len1, len2)

            if length > (end - start):
                # Update start and end based on the palindrome length
                start = i - (length - 1) // 2
                end = i + length // 2

        return s[start:end + 1]

