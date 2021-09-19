import math

class Solution:
    def isHappy(self, n: int) -> bool:
        hash_map = set()
        sum = 0
        while n != 1 and n not in hash_map:
            s = str(n)
            for c in s:
                hash_map.add(int(c))
                sum += int(math.pow(int(c), 2))
            n = sum
            sum = 0    
        return n == 1