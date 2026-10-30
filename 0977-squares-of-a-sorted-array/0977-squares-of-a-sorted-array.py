class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        output=[]
        for i in nums:
            output.append(i**2)
        a=sorted(output)
        return a