def parse():
	fresh = []
	ids = []

	parsing_fresh = True

	lines = [c.strip() for c in open("data/day05.txt", "r")]

	for line in lines:
		if line == "":
			parsing_fresh = False
		else:
			if parsing_fresh:
				a, b = line.split("-")
				fresh.append((int(a), int(b)))
			else:
				ids.append(int(line))

	return fresh, ids

def solve_part1():
	result = 0

	fresh, ids = parse()

	for id in ids:
		spoiled = True

		for a, b in fresh:
			if id >= a and id <= b:
				spoiled = False

		if not spoiled:
			result += 1

	return result

def solve_part2():
	result = 0

	ranges, _ = parse()
	ranges.sort()

	c_min, c_max = ranges[0]

	for i in range(1, len(ranges)):
		n_min, n_max = ranges[i]

		if n_min <= c_max + 1:
			c_max = max(c_max, n_max)
		else:
			result += c_max - c_min + 1
			c_min, c_max = n_min, n_max

	result += c_max - c_min + 1

	return result

print(solve_part1())
print(solve_part2())
