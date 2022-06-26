class Solution(object):
    def check(self, s):
        c = 0
        for ch in s:
            if ch == '(':
                c += 1
            if ch == ')':
                c -= 1
                if c < 0:
                    return False
        return c == 0

    def dfs(self, s, d_l, d_r, res, hist):
        if d_l == 0 and d_r == 0:
            if not s in res and self.check(s):
                res[s] = True
        elif s == "":
            return
        else:
            for i in range(len(s)):
                if not s[0:i] + s[i + 1:] in hist:
                    hist[s[0:i] + s[i + 1:]] = True

                    if s[i] == '(' and d_l > 0:
                        self.dfs(s[0:i] + s[i + 1:], d_l - 1, d_r, res, hist)

                    if s[i] == ')' and d_r > 0:
                        self.dfs(s[0:i] + s[i + 1:], d_l, d_r - 1, res, hist)

    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        res = {}
        hist = {}
        d_r = 0  # number of '(' to be deleted
        d_l = 0  # number of ')' to be deleted
        for ch in s:
            if ch == '(':
                d_l += 1
            if ch == ')':
                if d_l > 0:
                    d_l -= 1
                else:
                    d_r += 1

        self.dfs(s, d_l, d_r, res, hist)

        return res.keys()