class Solution(object):
    def largestOddNumber(self, num):
        result=""
        count=""
        for i in num:
            if int(i)%2!=0:
                count+=i
                result+=count
                count=""
            else:
                count+=i
        return result

            
            