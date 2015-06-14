"""
https://leetcode.com/problems/contains-duplicate-ii/
"""

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        
        d = {}
        for i, v in enumerate(nums):
            if v in d and i - d[v] <=k:
                return True
            else:
                d[v] = i
        return False
