class Solution:
    def calPoints(self, operations: list[str]) -> int:
        result=[]
        for i in operations:
            if i not in ['C','D','+']:
                result.append(int(i))
            elif i=="C":
                result.pop()
            elif i=="D":
                result.append(result[-1]*2)
            elif i=="+":
                result.append(result[-1]+result[-2])
        
        if result==[]:
            return 0
        else:
            return sum(result)

        