class Solution:
    def maxDepth(self, s: str) -> int:
        maxi=0
        count=0

        for i in s:
            if i=="(":
                count+=1
            elif i==")":
                count-=1
            
            if count>maxi:
                maxi=count
        return maxi
            
            
       
        