from typing import *

nums = [2, 7, 11, 15]
target = 9
# class Solution:
#     def twoSum(self, nums: List[int]) -> List[int]:
#         #target = 9
#
# #브루트 포스로 접근하기
#         for i in range(len(nums)):
#             for j in range(len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
# sol = Solution().twoSum(nums)
# print(sol)

#in을 이용한 탐색

class Solution:
    def twoSum(self, nums: List[int]) -> List[int]:
        for i, n in enumerate(nums):
            ans = target - n
            if ans in nums[i + 1:]:

                #[i+1:]로 생략된 앞 인덱스만큼 i를 더해주고 0부터 시작하니까 +1을 해준다. !!
                return [nums.index(n), nums[i + 1:].index(ans) + i + 1]

sol = Solution().twoSum(nums)
print(sol)
#


