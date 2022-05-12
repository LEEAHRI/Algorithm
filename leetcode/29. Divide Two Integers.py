dividend = 10
divisor = 3
import math
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:


        #math.trunc - > 버림함수
        answer = math.trunc(dividend / divisor)

        if answer > (pow(2,31) -1):
            answer = pow(2,31) -1
        elif answer < (pow(2,31) * (-1)):
            answer = pow(2,31) * (-1)
        return answer
