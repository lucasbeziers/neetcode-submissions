class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        n = len(nums)
        for i in range(n):
            indices[nums[i]] = i
        
        for i in range(n):
            a = nums[i]
            diff = target - a
            if diff in indices and indices[diff] > i:
                return [i, indices[diff]]