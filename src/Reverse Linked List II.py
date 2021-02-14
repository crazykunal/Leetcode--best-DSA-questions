# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # global successor
        
        def reverse(head,n):
            nonlocal successor
            if(n==1):
                successor=head.next
                return head
            last=reverse(head.next,n-1)
            head.next.next=head
            head.next=successor
            return last
        successor=None
        if(m==1):
            return reverse(head,n)
        head.next=self.reverseBetween(head.next,m-1,n-1)
        return head
        
#         dummy = node = ListNode(next=head)
#         for i in range(m-1): node = node.next 
        
#         prev, curr = None, node.next
#         for i in range(m, n+1): 
#             temp=curr.next
#             curr.next=prev
#             prev=curr
#             curr=temp
#         node.next.next = curr
#         node.next = prev
#         return dummy.next
