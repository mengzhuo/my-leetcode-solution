class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex <= 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
            
        rows = [[1,1]]
        for i in xrange(1, rowIndex):
            rows.append(map(lambda x,y: x+y, rows[-1]+[0], [0]+rows[-1]))
            
        return rows[-1]

