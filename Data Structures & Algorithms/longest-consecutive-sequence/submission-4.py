class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
      numSet = set(nums)
      count = 0
 #[2,20,3,4,21] 2+1=3
      for num in numSet:
        if (num - 1) not in numSet:
            long = 1
            while (num+long) in numSet:
                long +=1
            count = max(count, long)
      return count 
