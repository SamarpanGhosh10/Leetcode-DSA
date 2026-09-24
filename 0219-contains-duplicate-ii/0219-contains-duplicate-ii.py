class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        n=len(nums)
        dict1={}
        for i in range(0,n):
            if nums[i] not in dict1:
                dict1[nums[i]]=i
            else:
                if abs(dict1[nums[i]]-i)<=k:
                    return True
                dict1[nums[i]]=i
        return False

        