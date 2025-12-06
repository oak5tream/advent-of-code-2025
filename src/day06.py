def solve_part1():
	data = [c.split() for c in open("data/day06.txt", "r")]
	data = list(map(list, zip(*data)))
	result = 0

	for eq in data:
		op = eq[-1]
		val = int(eq[0])

		for num in eq[1:-1]:
			val = val + int(num) if op == "+" else val * int(num)

		result += val

	return result

def solve_part2():
	result = 0
	data = []

	for line in open("data/day06.txt", "r"):
		data.append(list(line.rstrip('\n')))

	data = list(map(list, zip(*data)))

	def parse_math(l):
		val = 0
		op = None
		exp = 0

		for c in reversed(l):
			if c == '*' or c == '+':
				op = c
			elif c != ' ':
				val += int(c) * pow(10, exp)
				exp += 1

		return val, op

	value = 0
	operator = None

	for d in data:
		val, op = parse_math(d)
		
		if op:
			operator = op

		if val:
			if not value:
				value = val
			else:
				value = value + val if operator == "+" else value * val
		else:
			result += value
			value = 0

	result += value
	
	return result

print(solve_part1())
print(solve_part2())
