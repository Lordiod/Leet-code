# https://leetcode.com/problems/roman-to-integer/description/
# difficulty: easy

class Solution:
    def romanToInt(self, s):
        numbers = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        
        for i in range(len(s)):
            if i+1 < len(s) and numbers[s[i]] < numbers[s[i+1]]:
                result -= numbers[s[i]]
            else:
                result += numbers[s[i]]
                
        return result