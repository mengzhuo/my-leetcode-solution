class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0 
        n = len(s)
        for i in range(n):
            res += (ord(s[n-1-i]) - 64) * 26 ** i
        return res
