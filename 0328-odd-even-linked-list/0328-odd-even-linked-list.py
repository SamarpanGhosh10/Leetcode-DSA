# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        temp=head
        if temp==None:
            return head
        result=[]
        while temp is not None:
            result.append(temp.val)
            if temp.next==None:
                break
            else:
                temp=temp.next.next
           
        
        temp=head.next
        while temp is not None and temp.next is not None:
            result.append(temp.val)
            temp=temp.next.next
        

        n=len(result)
        temp=head
        for i in range(n):
            temp.val=result[i]
            temp=temp.next
        

        return head
        


        