#!/usr/bin/python3

class Solution:
    def romanToInt(self, s: str) -> int:
        romanValue = { 
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        num = 0
        for i in range(len(s)):
            if i != len(s) - 1:
                if s[i] == 'I' and s[i + 1] == 'V' or s[i + 1] == 'X':
                    num += s[i + 1] - 1
                elif s[i] == 'X' and s[i + 1] == 'L' or s[i + 1] == 'C':
                    num += s[i + 1] - 10
                elif s[i] == 'C' and s[i + 1] == 'D' or s[i + 1] == 'M':
                    num += s[i + 1] - 100
                else:
                    num += romanValue[s[i]]
            else:
                num += romanValue[s[i]]
        return num

if __name__ == "__main__":
    res = Solution().romanToInt("MCMXCIV")
    print(res)
