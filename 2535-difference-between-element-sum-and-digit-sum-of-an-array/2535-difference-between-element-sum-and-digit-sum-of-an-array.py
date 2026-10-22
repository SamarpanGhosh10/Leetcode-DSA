class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        element_sum=0
        digit_sum=0
        for i in nums:
            element_sum+=i
            s=str(i)
            for j in s:
                digit_sum+=int(j)
        return abs(element_sum-digit_sum)

        