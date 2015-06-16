"""
https://leetcode.com/problems/longest-common-prefix/
"""


class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        strs.sort()
        prefix = strs[0]
        for s in strs[1:]:
            i = 0
            while i < len(prefix):
                if prefix[i] != s[i]:
                    if i == 0:
                        return ""
                    prefix = prefix[:i]
                    break
                i += 1
        return prefix
