import math

# EX
# n = 8
# 1,1,1,1,1,1,1,1 = 8C0
# 2,1,1,1,1,1,1 = 7C1
# 2,2,1,1,1,1 = 6C2 
# 2,2,2,1,1 = 5C3
# 2,2,2,2 = 4C4

class Solution:
    def climbStairs(self, n: int) -> int:
        
        # Result
        r = 0
        
        # How many 2's can n have at most?
        maximum = int(n//2)
        
        # Pick i number of 2's from n number of 1's and 2's
        for i in range(0, maximum+1):
            r += math.comb(n, i)
            n-=1
            
        return r