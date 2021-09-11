class Solution:
    count = 0;
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = self.count + 1
        while(i <= len(nums) - 1):
            if(nums[self.count] + nums[i] == target):
                return [self.count, i]
            i+=1;
        self.count+=1
        return self.twoSum(nums, target)