class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Merge the two arrays
        merged = sorted(nums1 + nums2)
        n = len(merged)
        
        # If odd, return middle
        if n % 2 == 1:
            return merged[n // 2]
        else:
            # If even, average of two middle numbers
            return (merged[n // 2 - 1] + merged[n // 2]) / 2.0
