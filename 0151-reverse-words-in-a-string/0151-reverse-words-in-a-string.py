class Solution(object):
    def reverseWords(self, s):
        result=""
        l1=s.split()
        l2=l1[::-1]
        result =" ".join(l2)
        return result