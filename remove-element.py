class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        begin = 0
        for i in nums:
            if i != val:
                nums[begin] = i
                begin += 1
        return begin
