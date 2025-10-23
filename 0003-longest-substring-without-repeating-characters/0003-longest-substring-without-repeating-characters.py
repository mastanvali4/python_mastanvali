class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_index = {}  # stores the last index of each character
        left = 0         # left pointer of the sliding window
        max_len = 0

        for right, char in enumerate(s):
            # If character already seen and inside the window, move left pointer
            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1

            # Update the last seen index of the character
            char_index[char] = right

            # Update the maximum length
            max_len = max(max_len, right - left + 1)

        return max_len
