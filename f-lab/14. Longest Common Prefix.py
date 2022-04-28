class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        strs.sort(key=lambda x: len(x))  # 단어길이 순으로 정렬

        if len(strs) == 0:
            return ""
        else:
            for i in range(len(strs[0])):
                for j in range(len(strs)):
                    if strs[0][i] != strs[j][i]:
                        return strs[0][:i]
            return strs[0]