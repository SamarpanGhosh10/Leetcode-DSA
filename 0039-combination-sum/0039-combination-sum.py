class Solution:
    def solve(self,index,total,subset,candidates,target,result):
        if total==target:
            result.append(subset.copy())
            return
        if total>target or index>=len(candidates):
            return
        
        subset.append(candidates[index])
        Sum=total+candidates[index]
        self.solve(index,Sum,subset,candidates,target,result)
        subset.pop()
        
        self.solve(index+1,total,subset,candidates,target,result)
        
        return result


    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.solve(0,0,[],candidates,target,[])

        