class Solution:
    def solve(self,index,total,candidate,subset,result):
        if total==0:
            result.append(subset.copy())
            return
        if total<0:
            return
        if index>=len(candidate):
            return
        for i in range(index,len(candidate)):
            if i>index and candidate[i]==candidate[i-1]:
                continue
            subset.append(candidate[i])
            Sum=total-candidate[i]
            self.solve(i+1,Sum,candidate,subset,result)
            subset.pop()
        return result
    
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        return self.solve(0,target,candidates,[],[])
       
        