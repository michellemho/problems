class Solution:
    def romanToInt(self, s: str) -> int:
        code = {
                    'M': 1000,
                    'D': 500,
                    'C': 100,
                    'L': 50,
                    'X': 10,
                    'V': 5,
                    'I': 1
                }
        prev_char = None
        value = 0
        for char in s[::-1]:
            char_value = code[char]
            if char == 'I' and prev_char in ['V','X']:
                char_value = -1
            if char == 'X' and prev_char in ['L','C']:
                char_value = -10
            if char == 'C' and prev_char in ['D','M']:
                char_value = -100
            value += char_value
            prev_char = char
        return value
