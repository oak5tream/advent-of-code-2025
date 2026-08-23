L = [c.strip() for c in open("data/day12.txt", "r")]

def solve(data):
	parsing_shapes = True
	shape_index = 0

	shapes = {}
	result = 0

	for line in data:
		if line == "":
			continue

		if 'x' in line:
			parsing_shapes = False

		if parsing_shapes:
			if ':' in line:
				shape_index = int(line.replace(':', ''))
				shapes[shape_index] = 0
			else:
				shapes[shape_index] += line.count('#')
		else:
			a, b = line.split(':')
			dim = a.split('x')
			
			area = int(dim[0]) * int(dim[1])
			packages = list(map(int, b.lstrip().split(' ')))

			space = 0
			for i, package in enumerate(packages):
				space += package * shapes[i]

			if space <= area:
				result += 1

	return result

print(solve(L))
