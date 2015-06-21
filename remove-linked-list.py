class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def __str__(self):
        return "Node:%d" % self.val

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        while current and current.next:
            
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return dummy.next
