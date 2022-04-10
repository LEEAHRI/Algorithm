from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
		#reversed()는 역순의 사본을 이용하고 싶을때 !
        s.reverse()
        return s

sol = Solution().reverseString(["H","E","L","L","O"])
print(sol)