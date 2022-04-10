import collections
from typing import List

class Solution:
	def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
		anagram = collections.defaultdict(list)

		for word in strs:
			anagram[''.join(sorted(word))].append(word)
		return sorted(list(anagram.values()))


sol = Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"])
print(sol)

# dict = {
# 	"abt" = ["bat"]
# "aet" = ["eat", "tea", "ate"],
# 		"ant" = ["tan", "nat"]
# }
#
#
#
# anagrams = collections.defaultdict(list)
# anagrams = {}
#
# for word in strs:
# 	# 정렬하여 딕셔너리에 추가
# 	key = ''.join(sorted(word))
#
# 	if key not in anagrams:
# 		anagrams[key] = []
# 	anagrams[key].append(word)
#
# 	#     if key in anagrams:
# 	#         anagrams[key].append(word)
# 	#     else:
# 	#         anagrams[key] = []
# 	#         anagrams[key].append(word)
#
# 	anagrams[''.join(sorted(word))].append(word)
#
# ans = []
# for value in dict:
# 	ans.append(value)
#
# [["bat"], ["eat", "tea", "ate"], ["tan", "nat"]]