class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.q.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        self.q.pop(len(self.q)-1)

    def top(self):
        """
        :rtype: int
        """
        return self.q[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.q) == 0
