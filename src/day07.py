from functools import cache

def parse():
	grid = {}
	start_pos = None
	grid_size = [0, 0]

	for y, line in enumerate(open("data/day07.txt", "r")):
		for x, c in enumerate(list(line.strip())):
			pos = x + y * 1j

			if c == 'S':
				start_pos = pos

			grid[pos] = c
			
			grid_size[0] = max(grid_size[0], x + 1)

		grid_size[1] = max(grid_size[1], y + 1)

	return grid, start_pos, grid_size

def solve_part1():
	result = 0
	grid, start_pos, _ = parse()

	visited = set()
	beams = set()
	beams.add(start_pos + 1j)

	while len(beams) > 0:
		beam = beams.pop()

		if grid[beam] == '.':
			if beam + 1j in grid:
				beams.add(beam + 1j)
		elif grid[beam] == '^':
			if beam in visited:
				continue

			visited.add(beam)

			beams.add(beam - 1)
			beams.add(beam + 1)

			result += 1

	return result

def solve_part2():
	grid, start_pos, grid_size = parse()

	@cache
	def get_timelines(pos):
		if int(pos.imag) == grid_size[1]:
			return 1
		elif grid[pos] == '^':
			return get_timelines(pos + (-1 + 1j)) + get_timelines(pos + (1 + 1j))
		else:
			return get_timelines(pos + 1j)

	return get_timelines(start_pos)

print(solve_part1())
print(solve_part2())
