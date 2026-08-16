class Solution:
    def frequencySort(self, s: str) -> str:
        hash_map={}
        result=""
        for i in s:
            if i not in hash_map:
                hash_map[i]=1
            else:
                hash_map[i]+=1
        
        sorted_dict=dict(sorted(hash_map.items(),key=lambda x:x[1],reverse=True))

        for i in sorted_dict:
            result += sorted_dict[i]*i
        

        return result
        
        