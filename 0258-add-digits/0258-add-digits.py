class Solution:
    def addDigits(self, num: int) -> int:
        n=num
        while n>=10:
            s=0
            while n>0:
                s+=n%10
                n=n//10

            n=s
        return n
        