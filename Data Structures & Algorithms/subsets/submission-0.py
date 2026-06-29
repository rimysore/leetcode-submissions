class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset[:])
                return
            #I decide to add value num[i]
            subset.append(nums[i])
            dfs(i+1)

            #I decide not to add value num[i]
            subset.pop()
            dfs(i+1)
        dfs(0)
        return res
