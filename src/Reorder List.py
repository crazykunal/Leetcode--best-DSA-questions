# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return None
        slow=head
        fast=head
        while(fast and fast.next):
            slow=slow.next
            fast=fast.next.next
        mid=slow
        prev=None
        cur=mid
        while cur:
            temp=cur.next
            cur.next=prev 
            prev=cur
            cur=temp
        head_of_second_rev = prev
        first=head 
        second=head_of_second_rev
        while second.next:
            next_hop = first.next
            first.next = second
            first = next_hop
            next_hop = second.next
            second.next = first
            second = next_hop
        
        
        
#         if not head or not head.next:
#             return
        
#         slow, fast = head, head
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
        
#         prev, slow.next, slow = None, None, slow.next
#         while slow:
#             prev, prev.next, slow = slow, prev, slow.next

#         slow = head
#         while prev:
#             slow.next, slow = prev, slow.next
#             prev.next, prev = slow, prev.next
        
