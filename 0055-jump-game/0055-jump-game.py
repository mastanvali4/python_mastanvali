class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_reach = 0
        n = len(nums)

        for i in range(n):
            # If we are at a position we can't reach, return False
            if i > max_reach:
                return False

            # Update the farthest reachable index
            max_reach = max(max_reach, i + nums[i])

            # If we can reach or go beyond the last index, return True
            if max_reach >= n - 1:
                return True

        return True
