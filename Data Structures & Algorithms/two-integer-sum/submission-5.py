class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        opt = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in opt:
                return [opt[diff],i]
            opt[n] = i
            
