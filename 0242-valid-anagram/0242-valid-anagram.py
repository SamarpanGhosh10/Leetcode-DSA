class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1={}
        if len(s)!=len(t):
            return False
        for i in s:
            if i not in dict1:
                dict1[i]=1
            else:
                dict1[i]+=1
        
        for j in t:
            if j not in dict1:
                return False
            if t.count(j)==dict1[j]:
                continue
            else:
                return False
        return True

        