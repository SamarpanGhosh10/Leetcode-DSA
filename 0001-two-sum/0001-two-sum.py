class Solution(object):
    def twoSum(self, nums, target):
        n=len(nums)
        hash_map={}
        for i in range(0,n):
            remainder=target-nums[i]
            if remainder in hash_map:
                return [hash_map[remainder],i]
            hash_map[nums[i]]=i
        