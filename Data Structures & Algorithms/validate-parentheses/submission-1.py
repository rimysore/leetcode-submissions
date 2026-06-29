class Solution:
    def isValid(self, s: str) -> bool:
       stk = []
       mapping = {")":"(","}":"{","]":"["}

       for ch in s:
        if ch in mapping.values():
            stk.append(ch)
        elif ch in mapping.keys():
            if not stk or mapping[ch] != stk.pop():
                return False
       return not stk