#height = [0,2,0,3,1,0,1,3,2,1]
#          l                 r

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l = 0 
        r = len(height)-1
        res = 0
        leftMax = height[l]
        rightMax = height[r]

        while l<r:
            if leftMax<rightMax:
                l+=1
                leftMax = max(leftMax,height[l])#2
                res += leftMax - height[l]

            else:
                r-=1
                rightMax = max(rightMax,height[r])
                res+= rightMax - height[r]
        return res

        
