#!/usr/bin/env python
# encoding: utf-8


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def __repr__(self):
        return "LN:%d" % self.val
def merge_sort(l):

    final = []

    
class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head, is_circular=False):
        
        if not head or not head.next:
            return head

        p = head
        insize = 1
        while True:
            p = head
            old_head = p
            _list = None
            tail = None

            nmerges = 0

            while p:
                nmerges += 1
                q = p
                psize = 0
                i = 0
                while i < insize:
                    i += 1
                    psize += 1

                    if is_circular:
                        q = q.next if q.next == old_head else None
                    else:
                        q = q.next

                    if not q:
                        break
                qsize = insize

                while psize > 0 or (qsize > 0 and q):

                    if not psize:
                        e = q
                        q = q.next
                        qsize -= 1
                        if is_circular and q == old_head:
                            q = None
                    elif qsize == 0 or not q:
                        e = p
                        p = p.next
                        psize -= 1
                        if is_circular and p == old_head:
                            p = None
                    elif p.val <= q.val:
                        e = p
                        p = p.next
                        psize -= 1
                        if is_circular and p == old_head:
                            p = None
                    else:
                        e = q
                        q = q.next
                        qsize -= 1
                        if is_circular and q == old_head:
                            q = None
                    if tail:
                        tail.next = e
                    else:
                        _list = e
                    
                    tail = e

                p = q

            if is_circular:
                tail.next = _list
            else:
                tail.next = None

            if nmerges <= 1:
                return _list
            insize *= 2
