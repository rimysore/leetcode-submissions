class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #nums = [0.3.2.100.200.1]
        #nset = []
         nset = set(nums)
         i = 0

         for num in nset:
            if (num-1) not in nset:
                incr = 1
                while(num+incr) in nset:
                    incr+=1
                i = max(incr, i)
         return i
