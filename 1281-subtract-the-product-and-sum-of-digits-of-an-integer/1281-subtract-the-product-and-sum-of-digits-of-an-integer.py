class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product=1
        Sum=0
        nums=n
        while nums>0:
            ld=nums%10
            Sum+=ld
            product*=ld
            nums=nums//10
        return product - Sum
        