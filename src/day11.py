from functools import cache
from heapq import heappop, heappush

def parse():
	data = {}

	for l in [c.strip().split(": ") for c in open("data/day11.txt", "r")]:
		data[l[0]] = l[1].split(" ")

	return data

def solve_part1():
	data = parse()
	heap_id = 0
	path_id = 1
	queue = []

	heappush(queue, (heap_id, "you", path_id))

	while queue:
		(_, key, _) = heappop(queue)

		for i, next_key in enumerate(data[key]):
			if next_key == "out":
				continue

			if i > 0:
				path_id += 1

			heap_id += 1
			heappush(queue, (heap_id, next_key, path_id))

	return path_id

def solve_part2():
	data = parse()

	@cache
	def valid_paths(key, dac = False, fft = False):
		if "out" in data[key]:
			return 1 if dac and fft else 0

		if key == "dac":
			dac = True
		if key == "fft":
			fft = True

		paths = 0

		for next_key in data[key]:
			paths += valid_paths(next_key, dac, fft)

		return paths

	return valid_paths("svr")

print(solve_part1())
print(solve_part2())
