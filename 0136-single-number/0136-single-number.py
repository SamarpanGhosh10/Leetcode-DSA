class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c=0
        for i in nums:
            c=c^i
        return c

        