class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash_map={}
        for i in range(len(nums)):
            remainder=target-nums[i]
            if remainder in hash_map:
                return [hash_map[remainder],i]
            else:
                hash_map[nums[i]]=i
            
        
        