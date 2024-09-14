def solution(code):
	mode = 0
	result = ''

	for idx, val in enumerate(code):
		if not mode:	# mode = 0
			if val.isdigit():	# 숫자면
				mode = not mode
				continue
			else:
				if idx % 2:	# 홀수
					continue
				result += val

		else:			# mode = 1
			if val.isdigit():
				mode = not mode
				continue
			else:
				if not idx % 2:	# 짝수
					continue
				result += val

	return result if result else 'EMPTY'