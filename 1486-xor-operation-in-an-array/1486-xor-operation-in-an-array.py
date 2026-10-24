class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums=[]
        s=0
        for i in range(0,n):
            nums.append(start+2*i)
        for j in nums:
            s=s^j
        return s
