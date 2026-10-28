class Solution:
    def triangleType(self, nums: List[int]) -> str:
        s=set(nums)
        a=sorted(nums)
        if len(s)==1:
            return "equilateral"
        elif len(s)==2:
            if a[0]+a[1]>a[2]:
                return "isosceles"
            else:
                return "none"
     
        else:
          
            if a[0]+a[1]>a[2]:
                return "scalene"
            else:
                return "none"
            
                
        
           
                
        


        