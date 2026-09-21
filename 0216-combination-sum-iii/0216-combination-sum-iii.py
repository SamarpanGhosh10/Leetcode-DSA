class Solution:
    def solve(self,index,given,subset,result,k,n):
        if len(subset)>=k:
            if sum(subset)==n:
                result.append(subset.copy())
            return
        if index>=len(given):
            return
       
        
           
        subset.append(given[index])
        self.solve(index+1,given,subset,result,k,n)
        subset.pop()
        self.solve(index+1,given,subset,result,k,n)
        return result
        

    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        given=[1,2,3,4,5,6,7,8,9]
        return self.solve(0,given,[],[],k,n)
        