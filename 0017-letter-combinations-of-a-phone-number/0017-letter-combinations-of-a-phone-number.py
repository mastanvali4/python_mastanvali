class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        # Mapping of digits to corresponding letters
        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []

        def backtrack(index, current):
            # Base case: if the combination is complete
            if index == len(digits):
                result.append(current)
                return
            
            # Get possible letters for current digit
            possible_letters = phone_map[digits[index]]
            
            # Try each letter and recurse
            for letter in possible_letters:
                backtrack(index + 1, current + letter)

        # Start backtracking
        backtrack(0, "")
        return result
