class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        
        one = two = three = 0
        for x in A:
            two = two | one & x
            one = one ^ x
            three = one & two
            one = one & ~three
            two = two & ~three
        return one

if __name__ == '__main__':
    so = Solution()
    print 'result:%d' % so.singleNumber([7,7,3,7])
