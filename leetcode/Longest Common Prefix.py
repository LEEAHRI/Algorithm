from typing import *


strs = ["flower", "flow", "flight"]
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        strs.sort(key=lambda x:len(x)) #단어길이 순으로 정렬

        if len(strs) == 0:
            return ""
        else:
            for i in range(1,len(strs[0])):
                for j in range(1, len(strs)):
                    if strs[0][i] != strs[j][i]:
                        return strs[0][:i] #단어가 틀려지기 전까지 반환
            return strs[0]
            #조건문에 하나도 걸리지 않는경우 strs의 첫번째 요소 반환

sol = Solution()
print(sol.longestCommonPrefix(strs))