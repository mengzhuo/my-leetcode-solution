class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
        t = s.strip().rpartition(" ")
        if t[-1]:
            return len(t[-1])
        else:
            return len(t[0])
