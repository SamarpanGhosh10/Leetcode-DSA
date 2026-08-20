# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        stack=[]
        temp=head
        while temp!=None:
            stack.append(id(temp))
            temp=temp.next
            if id(temp) in stack:
                return True
        return False

        