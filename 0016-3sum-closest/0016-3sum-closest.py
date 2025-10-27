class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Step 1: Sort the numbers
        nums.sort()
        n = len(nums)

        # Step 2: Initialize closest_sum with a large value
        closest_sum = float('inf')

        # Step 3: Iterate through each number
        for i in range(n - 2):
            left, right = i + 1, n - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                # If this sum is closer to target than previous, update closest_sum
                if abs(target - current_sum) < abs(target - closest_sum):
                    closest_sum = current_sum

                # Move pointers based on comparison with target
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    # Exact match found
                    return current_sum
        
        return closest_sum
