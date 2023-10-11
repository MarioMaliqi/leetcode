class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x).replace("-", "")[::-1] == str(x)

if __name__ == "__main__":
    res = Solution().isPalindrome(212)
    print(res)
