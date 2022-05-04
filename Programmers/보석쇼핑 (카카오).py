gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]

from collections import defaultdict

#투포인터 알고리즘 공부하기
def solution(gems):
    answer = [0, 0]
    candidates = []
    start,  end = 0, 0
    gems_len, gem_kind = len(gems), len(set(gems))
    gems_dict = defaultdict(lambda:0)






