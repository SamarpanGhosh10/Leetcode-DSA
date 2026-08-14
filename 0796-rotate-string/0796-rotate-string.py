class Solution(object):
    def rotateString(self, s, goal):
        if len(s)!=len(goal):
            return False
        n=len(s)
        t=s

        for i in range(n):
            if t==goal:
                return True
            t=s[i+1:]+s[:i+1]
        return False
            
            
            
            
