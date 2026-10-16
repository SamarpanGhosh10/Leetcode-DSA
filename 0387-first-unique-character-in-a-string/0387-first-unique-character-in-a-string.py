class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_map={}
        n=len(s)
        for i in s:
            if i not in hash_map:
                hash_map[i]=1
            else:
                hash_map[i]+=1
        for j in hash_map:
            if hash_map[j]==1:
                return s.index(j)
        return -1

            
        

        