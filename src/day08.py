import  math

L = [tuple(x for x in list(map(int, line.strip().split(",")))) for line in open("data/day08.txt", "r")]

def parse(data):
	circuits = {}

	for d in data:
		circuits[d] = {d}

	pairs_by_distance = []
	for j in range(len(data)):
		for i in range(j + 1, len(data)):
			pairs_by_distance.append((data[j], data[i]))

	pairs_by_distance = sorted(pairs_by_distance, key = lambda x: math.dist(*x))

	return circuits, pairs_by_distance

def solve_part1(data, test = False):
	result = 0
	num_iterations = 10 if test else 1000

	circuits, pairs_by_distance = parse(data)

	for i, (b0, b1) in enumerate(pairs_by_distance):
		c0 = None
		c1 = None

		for c in circuits:
			if b0 in circuits[c]:
				c0 = c
			if b1 in circuits[c]:
				c1 = c

		if c0 and c1 and c0 != c1:
			circuits[c0].update(circuits[c1])
			del circuits[c1]

		if i + 1 == num_iterations:
			num_boxes = []

			for c in circuits:
				num_boxes.append(len(circuits[c]))
			
			num_boxes = sorted(num_boxes)

			result = math.prod(num_boxes[x] for x in range(len(num_boxes) - 3, len(num_boxes)))
	
	return result

def solve_part2(data):
	circuits, pairs_by_distance = parse(data)

	for b0, b1 in pairs_by_distance:
		c0 = None
		c1 = None

		for c in circuits:
			if b0 in circuits[c]:
				c0 = c
			if b1 in circuits[c]:
				c1 = c

		if c0 and c1 and c0 != c1:
			circuits[c0].update(circuits[c1])
			del circuits[c1]

		if len(circuits) == 1:
			return b0[0] * b1[0]
	
	return 0

print(solve_part1(L))
print(solve_part2(L))
