"""
https://leetcode.com/problems/contains-duplicate/
"""

class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        if not nums:
            return False
            
        nums.sort()
        i = len(nums)-1
        while i > 0:
            if nums[i] == nums[i-1]:
                return True
            i -= 1
        return False
