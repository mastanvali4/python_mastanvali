class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Sort the array to enable the two-pointer technique
        nums.sort()
        result = []
        
        for i in range(len(nums) - 2):  # We need at least 3 elements for a triplet
            # Skip duplicates for 'i'
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total < 0:
                    left += 1  # We need a larger sum, move left pointer to the right
                elif total > 0:
                    right -= 1  # We need a smaller sum, move right pointer to the left
                else:
                    # Found a triplet
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates for 'left'
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicates for 'right'
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # Move both pointers to continue searching for other potential triplets
                    left += 1
                    right -= 1
        
        return result
