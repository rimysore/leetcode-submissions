class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        mapStk = {")" : "(", "}" : "{", "]" : "["}

        for c in s:
            if c in mapStk:
                if stk and stk[-1] == mapStk[c]:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(c)

        return True if not stk else False