class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # Map of Roman symbols and their values (in order from largest to smallest)
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syms = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]

        roman = ""
        i = 0

        while num > 0:
            # Check how many times the current value fits into num
            count = num // val[i]
            # Append the symbol that many times
            roman += syms[i] * count
            # Subtract the total value added
            num -= val[i] * count
            i += 1

        return roman
