from collections import Counter


def solution(grade):
	def get_grade_counter(grade):
		return Counter(grade)

	def get_ranks_dict(grade):
		counter = get_grade_counter(grade)
		ranks_dict = {}
		prev_sum = 1
		for element in sorted(counter.keys(), reverse=True):
			ranks_dict[element] = prev_sum
			prev_sum += counter.get(element)
		return ranks_dict

	def get_answer(grade, ranks_dict):
		return list(map(lambda item: ranks_dict[item], grade))

	ranks_dict = get_ranks_dict(grade)
	return get_answer(grade, ranks_dict)