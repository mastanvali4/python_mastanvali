class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            # If it's a closing bracket
            if char in mapping:
                # Pop from stack if not empty, else assign a dummy value
                top_element = stack.pop() if stack else '#'

                # Check if the mapping matches
                if mapping[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push to stack
                stack.append(char)

        # Stack should be empty if all brackets were matched correctly
        return not stack
