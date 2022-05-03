x = 123
class Solution:
    def reverse(self, x: int) -> int:


        if x > 0:
            ans = int(str(x)[::-1])
            if ans > 2**31:
                return 0
            return ans
        else:
            ans = -int(str(-x)[::-1])
            if ans < -(2**31)-1:
                return 0
            return ans


sol = Solution()

print(sol.reverse(x))

