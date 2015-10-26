class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, total = 0, len(nums)
        while i < total:
            ri = total - i - 1
            if ri - 1 >= 0 and nums[ri] == nums[ri-1]:
                nums.pop(ri)
            i+=1
        return len(nums)
