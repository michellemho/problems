class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid_pairings = {"}":"{",
                          ")":"(",
                          "]":"["}
        
        # edge case, all odd-length strings are false
        if len(s) % 2 != 0:
            return False
        
        for char in s:
            if len(stack) == 0:
                stack.append(char)
            else:
                # Check if char is a closing paren
                if char in valid_pairings.keys():
                    last_item = stack.pop()
                    if valid_pairings[char] == last_item:
                        continue
                    else:
                        return False
                else:
                    stack.append(char)
                    
        if stack == []:
            return True
        else:
            return False
