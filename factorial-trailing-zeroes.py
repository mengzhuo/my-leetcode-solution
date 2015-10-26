class Solution(object):
    def trailingZeroes(self, n):
        c = 0
        while n >0:
            n /= 5
            c += n
        return c
