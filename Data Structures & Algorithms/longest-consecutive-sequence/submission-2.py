class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
          numSet = set(nums)
          count = 0
          for num in numSet:
            if (num-1) not in numSet:
                lent = 1
                while(num+lent) in numSet:
                    lent+=1
                count = max(lent,count)
          return count