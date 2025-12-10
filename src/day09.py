from shapely import Polygon

L = [tuple(x for x in list(map(int, c.split(',')))) for c in open("data/day09.txt", "r")]

def solve_part1(data):
	result = 0

	for i, (x0, y0) in enumerate(data):
		for (x1, y1) in data[i + 1:]:
#			area = (max(x0, x1) - min(x0, x1) + 1) * (max(y0, y1) - min(y0, y1) + 1)
			area = (abs(x0 - x1) + 1) * (abs(y0 -  y1) + 1)
			result = max(result, area)

	return result

def solve_part2(data):
	result = 0

	outer = Polygon(data)

	for i, (x0, y0) in enumerate(data):
		for (x1, y1) in data[i + 1:]:
			p0 = (min(x0, x1), min(y0, y1))
			p1 = (max(x0, x1), min(y0, y1))
			p2 = (max(x0, x1), max(y0, y1))
			p3 = (min(x0, x1), max(y0, y1))

			rect = Polygon([p0, p1, p2, p3])

			if outer.contains(rect):
				result = max(result, (abs(x0 - x1) + 1) * (abs(y0 -  y1) + 1))

	return result

print(solve_part1(L))
print(solve_part2(L))
