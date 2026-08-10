class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        n=len(nums)
       
        result=set()
        if n<3:
            return []
        
        for i in range(0,n-1):
            hash_set=set()
            for j in range(i+1,n):
                
                
                third=-(nums[i]+nums[j])
                
                if third in hash_set:
                    temp=[nums[i],nums[j],third]
                    temp.sort()
                    
                    result.add(tuple(temp))
                else:
                    hash_set.add(nums[j])
        return [  list(ans)   for ans in result]