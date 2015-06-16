"""
https://leetcode.com/problems/isomorphic-strings/
"""

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
    
        d = {}
        for i in zip(s,t):
            if not i[0] in d:
                d[i[0]] = i
            elif d[i[0]] != i:
                return False
        sd = {}
        for i in zip(t,s):
            if not i[0] in sd:
                sd[i[0]] = i
            elif sd[i[0]] != i:
                return False
    
        return True
