class Solution:
    def isValid(self, s: str) -> bool:
        s_list = list(s)
        stack = []

        if len(s_list) % 2 != 0:
            return False
        for i in s_list:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            elif len(stack) == 0:
                return False
            else:
                top = stack.pop()
                if (i == ')' and top != '(') or (i == ']' and top != '[') or (i == '}' and top != '{'):
                    return False
                continue
        if len(stack) != 0:
            return False

        return True