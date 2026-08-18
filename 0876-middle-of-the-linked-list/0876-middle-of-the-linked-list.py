# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n=0
        c=0
       
        temp=head
        while temp !=None:
            n+=1
            temp=temp.next
        temp=head
        num=n//2
        while temp!=None:
            if c>=num:
                return temp
                temp=temp.next
                c+=1
            else:
                temp=temp.next
                c+=1
        return result




        