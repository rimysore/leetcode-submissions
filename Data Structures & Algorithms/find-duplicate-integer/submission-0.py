class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        arr = []
        for num in nums:
            if num not in arr:
                arr.append(num)
            else:
                return num