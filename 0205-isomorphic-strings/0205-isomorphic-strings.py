class Solution(object):
    def isIsomorphic(self, s, t):
    
        result={}
        n=len(s)
        for i in range(0,n):
            if t[i] in result.values() and s[i]  not in result:
                return False
            if s[i] not in result:
                result[s[i]]=t[i]
            elif t[i]!=result[s[i]]:
                return False
        return True
        
            
      