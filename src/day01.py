import re

L = [c.strip() for c in open("data/day01.txt", "r")]

def solve_part1(data):
	result = 0
	dial = 50

	for l in data:
		m = re.search("([LR])(.*)", l)

		if m:
			d = m.group(1)
			v = int(m.group(2))

			if d == "L":
				dial = (dial - v) % 100
			else:
				dial = (dial + v) % 100

		if dial == 0:
			result += 1

	return result

def solve_part2(data):
	result = 0
	dial = 50

	for l in data:
		m = re.search("([LR])(.*)", l)

		if m:
			d = m.group(1)
			v = int(m.group(2))

			add = 1 if d == "R" else -1

			for _ in range(0, v):
				dial += add
				dial %= 100

				if dial == 0:
					result += 1

	return result

print(solve_part1(L))
print(solve_part2(L))
