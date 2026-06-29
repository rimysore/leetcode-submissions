class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        opt = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                stackI, stackT = stack.pop()
                opt[stackI] = i - stackI
            stack.append((i,t))
        return opt