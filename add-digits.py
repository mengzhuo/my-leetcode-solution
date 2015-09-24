class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int

        https://en.wikipedia.org/wiki/Digital_root
        """
        if num == 0:
            return 0
        return num-9*int((num-1)/9)
