class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = int(len(nums)/2)
        s = set()
        nums.sort()
        for num in nums:
            if not num in s:
                s.add(num)
            else:
                return num
        