class Solution(object):
    def findMin(self, nums):
        n=len(nums)
        low=0
        high=n-1
        mini=float("inf")
        
        while low<=high:
            
            mid=(low+high)//2

            x=nums[mid]-nums[high]
            
           
            if x>0:
                low=mid+1
            elif x<=0 :
                high=mid-1
            
            
                
            
           
            if nums[mid]<mini:
                mini=nums[mid]
             
            
        return mini
            
            