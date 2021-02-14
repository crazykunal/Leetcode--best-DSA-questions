# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        stack = []
        res = []
        id = 0
        while head:
            res.append(0)
            while stack and head.val > stack[-1][0]:
                a, ind = stack.pop()
                res[ind] = head.val
            stack.append((head.val,id))
            head = head.next
            id += 1
            
        return res
