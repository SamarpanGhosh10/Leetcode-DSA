class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr=[]
        
        while nums!=[]:
            s=[]
            s.append(min(nums))
            nums.remove(min(nums))
            s.append(min(nums))
            nums.remove(min(nums))
            arr.extend(s[::-1])
        return arr





        