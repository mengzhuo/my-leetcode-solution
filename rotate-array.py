#!/usr/bin/env python
# encoding: utf-8


class Solution:
# @param {integer[]} nums
# @param {integer} k
# @return {void} Do not return anything, modify nums in-place instead.
    def rotate(self, nums, k):

        n = len(nums)
        k %= n
        nums[:] = nums[n-k:] + nums[:n-k]

    def rotate_1(self, nums, k):
        while k:
            nums.insert(0, nums.pop())
            k -= 1

    def rotate_2(self, nums, k):
        def reverse(nums, low, high):
            if low > high:
                return
            while low < high:
                nums[low], nums[high-1] = nums[high-1], nums[low]
                low += 1
                high -= 1

        l = len(nums)
        k %= l

        reverse(nums, 0, l -k)
        reverse(nums, l-k, l)
        reverse(nums, 0, l)
