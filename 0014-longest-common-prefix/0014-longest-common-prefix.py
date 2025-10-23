class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        # Start with the first word as the prefix
        prefix = strs[0]

        # Compare with every other word
        for s in strs[1:]:
            # Reduce the prefix until it matches the start of s
            while s.find(prefix) != 0:
                prefix = prefix[:-1]  # remove last character
                if not prefix:
                    return ""
        return prefix
