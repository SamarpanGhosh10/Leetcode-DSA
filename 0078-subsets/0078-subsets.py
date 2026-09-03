class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        n=len(nums)
        total_subs=1<<n
        for num in range(0,total_subs):
            lst=[]
            for i in range(0,n):
                if num&(1<<i)!=0:
                    lst.append(nums[i])
            result.append(lst)
        return result




        