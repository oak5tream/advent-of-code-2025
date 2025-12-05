G = {}

for y, line in enumerate(open("data/day04_test.txt", "r")):
	for x, c in enumerate(list(line.strip())):
		if c == '@':
			G[x + y * 1j] = c

def num_neighbours(grid, pos):
	neighbours = 0

	for d in [-1, 1, 1j, -1j, -1 - 1j, -1 + 1j, 1 - 1j, 1 + 1j]:
		if pos + d in grid:
			neighbours += 1

	return neighbours

def solve_part1(data):
	result = 0

	for pos in data:
		if num_neighbours(data, pos) < 4:
			result += 1

	return result

def solve_part2(data):
	result = 0
	complete = False
	
	while not complete:
		remove = []

		for pos in data:
			neighbours = num_neighbours(data, pos)

			if neighbours < 4:
				remove.append(pos)

		if len(remove) > 0:
			for r in remove:
				del data[r]

			result += len(remove)
		else:
			complete = True

	return result

print(solve_part1(G))
print(solve_part2(G))
