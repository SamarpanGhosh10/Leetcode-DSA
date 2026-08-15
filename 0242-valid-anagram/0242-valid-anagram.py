class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False 

        hash_map={}

        for i in s:
            if i not in hash_map:
                hash_map[i]=1
            else:
                hash_map[i]+=1
        
        for j in t:
            if j not in hash_map:
                return False
            elif hash_map[j]!=t.count(j):
                return False
        return True
            