# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        curr = head
        finn = ''
        while curr is not None:
            finn = finn + str(curr.val)
            curr = curr.next

        return int(finn,2)