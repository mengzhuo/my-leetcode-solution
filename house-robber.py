#!/usr/bin/env python
# encoding: utf-8

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        if not nums:
            return 0
        
        a, b = 0,0
        for i, n in enumerate(nums):
            if i%2:
                a = max(a+n, b)
            else:
                b = max(b+n, a)
                
        return max(a,b)
