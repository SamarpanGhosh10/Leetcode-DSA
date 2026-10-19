class Solution:
    def countDigits(self, num: int) -> int:
        c=0
        n=num
        while n>0:
            ld=n%10
            if num%ld==0:
                c+=1
            n=n//10
        return c

        