'''
Using XOR
This is not my solution.
Link: https://leetcode.com/problems/single-number/discuss/42997/My-O(n)-solution-using-XOR

1. nums[0] ^ nums[1] ^ ... nums[i-1], nums[i]
2. Using Associative rule and bind same numbers so that we can make 0 (in XOR, if the two numbers are the same, 0)
3. Only one left will be returned

* '^' is a bitwise operator
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num = 0
        for i in range(0, len(nums)):
            num ^= nums[i]
        return num