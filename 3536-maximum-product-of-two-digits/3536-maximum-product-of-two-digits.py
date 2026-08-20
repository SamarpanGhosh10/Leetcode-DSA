class Solution:
    def maxProduct(self, n: int) -> int:
        largest=float("-inf")
        s_largest=float("-inf")
        nums=n
        while nums>0:
            ld=nums%10
            if ld>=largest:
                s_largest=largest
                largest=ld
                
            elif ld>s_largest and ld<largest:
                s_largest=ld
            nums=nums//10
        return largest*s_largest

        