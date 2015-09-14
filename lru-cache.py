#!/usr/bin/env python
# encoding: utf-8


class LRUCache(object):

    __slot__ = ['head', 'tail', 'cap', 'd']

    class Node(object):

        __slot__ = ['key', 'val', 'prev', 'next']

        def __init__(self, key, val=None):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None

        def __str__(self):
            return "k:%s v:%s next:%s prev:%s" % (self.key, self.val, self.next, self.prev)

    def __init__(self, cap=100):
        self.cap = cap
        self.head = self.Node("head")
        self.tail = self.Node("tail")
        self.head.next = self.tail
        self.tail.prev = self.head

        self.d = {}

    def get(self, key):
        if key in self.d:
            n = self.d[key]
            self.unlinkNode(n)
            self.insertNodeToHead(n)
            return n.val
        return -1
        
    def set(self, key, value):

        if key not in self.d:
            if len(self.d) >= self.cap:
                n = self.unlinkNode(self.tail.prev)
                del self.d[n.key]
                del n

            n = self.Node(key)
            n.val = value
            self.d[key] = n

        else:
            n = self.d[key]
            n.val = value
            self.unlinkNode(n)
            
        self.insertNodeToHead(n)

    def insertNodeToHead(self, n):
        n.prev, n.next = self.head, self.head.next # Link to n
        self.head.next.prev, self.head.next = n, n # unlink original

    def unlinkNode(self, n):
        n.next.prev, n.prev.next = n.prev, n.next
        n.prev = None
        n.next = None
        return n
