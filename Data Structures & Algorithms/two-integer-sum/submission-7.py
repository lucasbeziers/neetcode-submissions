class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        prev_values = {}

        for i in range(len(nums)):
            num = nums[i]
            value_needed = target - num
            if value_needed in prev_values:
                j = prev_values[value_needed]
                return [j, i]
            prev_values[num] = i

