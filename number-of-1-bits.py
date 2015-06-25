#!/usr/bin/env python
# encoding: utf-8

class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        w = 0
        for i in xrange(32):
            if n >> i & 1:
                w += 1
        return w
