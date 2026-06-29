class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, cur, total):
            if total==target:
                res.append(cur[:])
                return
            if i >= len(nums) or total > target:
                return 
            #when 1st element
            cur.append(nums[i])
            dfs(i,cur,total+nums[i])

            #when we skip that element
            cur.pop()
            dfs(i+1,cur,total)
        dfs(0,[],0)
        return res