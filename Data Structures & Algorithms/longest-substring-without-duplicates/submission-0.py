class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        chrSet = set()
        count = 0

        for r in range(len(s)):
            while s[r] in chrSet:
                chrSet.remove(s[l])
                l+=1
            chrSet.add(s[r])
            count = max(count,r-l+1)
        return count
        