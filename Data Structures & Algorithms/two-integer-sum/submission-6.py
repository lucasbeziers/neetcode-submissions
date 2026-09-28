class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        values = {}

        # fill
        for i in range(len(nums)):
            values[nums[i]] = i
        
        # search
        for i in range(len(nums)):
            value_needed = target - nums[i]
            if value_needed in values:
                j = values[value_needed]
                if j != i:
                    return [i, j]
        
