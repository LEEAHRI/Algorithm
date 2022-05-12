s = "()[]{}"


class Solution:

    def isOpenParentheses(self, ch):
        return ch == '[' or ch == '(' or ch == '{'

    def is_stack_empty(self, stack):
        return len(stack) == 0

    def sameParentheses(self, top, ch):
        if (ch == ']' and top != '[') or (ch == ')' and top != '(') or (ch == '}' and top != '{'):
            return False
        return True

    def isValid(self, s: str) -> bool:
        a = list(s)
        answer = True
        stack = []
        if len(a) % 2 != 0:
            return False
        for i in a:
            if self.isOpenParentheses(i):
                stack.append(i)
            elif self.is_stack_empty(stack):
                return False
            else:
                b = stack.pop()
                if not self.sameParentheses(b, i):
                    return False

        if not self.is_stack_empty(stack):
            return False
        return True


sol = Solution()
print(sol.isValid(s))
