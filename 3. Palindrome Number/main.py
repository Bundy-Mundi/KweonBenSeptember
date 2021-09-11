class Solution:
    def isPalindrome(self, x: int) -> bool:
        stack = []
        s = str(x)
        mid = int(len(s)/2)
        i = 0

        if(x < 0): return False
        if(0 <= x < 10): return True
        
        while(i < mid):
            stack.append(s[i])
            i+=1

        # If odd add one to i so that we can neglect it.
        if(len(s)%2!=0): i+=1
        while(i < len(s)):
            if(s[i] != stack.pop()): return False
            i+=1
        return True