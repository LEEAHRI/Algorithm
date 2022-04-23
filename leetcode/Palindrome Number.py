class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = str(x)
        b = list(a)
        c = b[::-1]

        print(b)
        print(b[::-1])

        for i in range(len(b)):
            if b[i] != c[i]:
                return False
        return True

sol = Solution()
print(sol.isPalindrome(12131))
