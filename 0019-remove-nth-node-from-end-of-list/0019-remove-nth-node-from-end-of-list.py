# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=head
        c=1
        while temp.next != None:
            c+=1
            temp=temp.next
        front=c-n
       
        if c==n:
            temp=head
            head=temp.next
            return head
        

        temp=head

        for _ in range(front-1):
            temp=temp.next
        if temp!=None and temp.next != None:
            temp.next=temp.next.next
        

        return head
        