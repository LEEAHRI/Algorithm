class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        list_x = list(str_x)
        reverse_x = list_x[::-1]

        if x < 0:
            return False

        for i in range(len(list_x)):
            if list_x[i] != reverse_x[i]:
                return False
        return True