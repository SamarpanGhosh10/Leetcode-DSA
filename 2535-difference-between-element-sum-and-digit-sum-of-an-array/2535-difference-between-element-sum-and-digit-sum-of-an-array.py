class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        element_sum=0
        digit_sum=0
        for i in nums:
            n=i
            element_sum+=i
            while n>0:
                ld=n%10
                digit_sum+=ld
                n=n//10
        return abs(element_sum-digit_sum)

        