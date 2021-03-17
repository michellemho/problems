class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        code = {}
        for i, letter in enumerate(s):
            if letter not in code and t[i] not in code.values():
                code[letter] = t[i]
            if letter not in code and t[i] in code.values():
                return False
            if code[letter] != t[i]:
                return False
        return True
