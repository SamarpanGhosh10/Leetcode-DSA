class Solution:
    def judgeCircle(self, moves: str) -> bool:
        a=[0,0]
        for i in moves:
            if i=="R":
                a[0]+=1
            elif i=="L":
                a[0]-=1
            elif i=="U":
                a[1]+=1
            else:
                a[1]-=1
        
        if a==[0,0]:
            return True
        else:
            return False
        