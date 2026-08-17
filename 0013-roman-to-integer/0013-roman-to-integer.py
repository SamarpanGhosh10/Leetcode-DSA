class Solution:
    def romanToInt(self, s: str) -> int:
        value={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

        result=0

        n=len(s)

        for i in range(n-1):
            if value[s[i]]<value[s[i+1]]:
                result-=value[s[i]]
            else:
                result+=value[s[i]]


        result+=value[s[-1]]

        return result