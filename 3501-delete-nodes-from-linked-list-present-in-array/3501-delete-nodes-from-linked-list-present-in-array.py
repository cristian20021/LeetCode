# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        rm_set = set(nums)
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy

        while prev.next:
            if prev.next.val in rm_set:
                prev.next = prev.next.next
            else:
                prev = prev.next
        return dummy.next