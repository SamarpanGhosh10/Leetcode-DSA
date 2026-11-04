class Solution:
    def signFunc(self,x):
        if x>0:
            return 1
        elif x==0:
            return 0
        else:
            return -1
    def arraySign(self, nums: list[int]) -> int:
        c=1
        for i in nums:
            c*=i
        return self.signFunc(c)
