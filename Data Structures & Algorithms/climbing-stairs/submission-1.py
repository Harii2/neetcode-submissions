class Solution:
    def climbStairs(self, n: int) -> int:
        one_step = 1 
        two_step = 2 
        if n == 1:
            return one_step 
        if n == 2:
            return two_step
        
        ans = 0
        for i in range(3, n+1):
            ans = two_step + one_step
            one_step = two_step 
            two_step = ans 

        return ans  


        