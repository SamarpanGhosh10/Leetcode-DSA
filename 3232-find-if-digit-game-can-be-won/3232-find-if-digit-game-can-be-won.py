class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        n=[]
        alice_choice=[]
        for i in range(len(nums)):
            if nums[i]//10==0:
                alice_choice.append(nums[i])
            else:
                n.append(nums[i])
        if sum(alice_choice)>sum(n):
            return True
        elif sum(n)>sum(alice_choice):
            return True
        return False

        