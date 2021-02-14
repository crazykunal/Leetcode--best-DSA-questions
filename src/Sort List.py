# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
#         if not head or not head.next:
#             return head
#         fast, slow = head.next, head
#         while fast and fast.next:
#             fast = fast.next.next
#             slow = slow.next
#         start = slow.next
#         slow.next = None
#         l, r = self.sortList(head), self.sortList(start)
#         return self.merge(l, r)
    
#     def merge(self, l, r):
#         if not l or not r:
#             return l or r
#         dummy = p = ListNode(0)
#         while l and r:
#             if l.val < r.val:
#                 p.next = l
#                 l = l.next
#             else:
#                 p.next = r
#                 r = r.next
#             p = p.next
#         p.next = l or r
#         return dummy.next
    
        # (iterative)
        if head is None: return None
        
        def getSize(head):
            counter = 0
            while(head is not None):
                counter +=1
                head = head.next
            return counter
        
        def split(head, size):
            i = 1
            while (i < size and head):
                head = head.next
                i += 1 
            if head is None: return None
            #disconnect
            temp = head.next 
            head.next=None
            return temp
        
        def merge(l, r, head):
            cur = head
            while(l and r):
                if l.val < r.val:
                    cur.next= l
                    l=l.next
                else:
                    cur.next= r
                    r=r.next
                cur = cur.next
            if l:
                cur.next = l 
            else:
                cur.next=r
            while cur.next:
                cur = cur.next
            return cur

        total_length = getSize(head)
        size = 1
        dummy = ListNode(0)
        dummy.next = head
        l, r, tail = None, None, None
        while (size <total_length ):
            cur = dummy.next
            tail = dummy
            while cur:
                l = cur
                r = split(l, size)
                cur = split(r, size)
                tail = merge(l, r, tail)
            size=size*2
        return dummy.next
