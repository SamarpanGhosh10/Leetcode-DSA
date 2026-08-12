class Solution(object):
    def longestCommonPrefix(self, strs):
        result=""
        base=strs[0]
        if len(strs)==0:
            return result
        for i in range(0,len(base)):
            for word in strs[1:]:
                if i==len(word) or base[i]!=word[i]:
                    return result
            result+=base[i]
        return result
    
                


        

        

        



        