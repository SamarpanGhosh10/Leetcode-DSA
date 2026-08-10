class Solution(object):
    def isPalindrome(self, x):
        nums=x
        palindrome_num=0
        if nums<0:
            return False
        while nums>0:
            ld=nums%10
            palindrome_num=palindrome_num*10+ld
            nums=nums//10
        if palindrome_num==x:
            return True      
        else:
            return False