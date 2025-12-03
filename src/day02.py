import re

L = [c.split(",") for c in open("data/day02.txt", "r")][0] # FIXME

def solve_part1(data):
	result = 0

	for d in data:
		r = d.split("-")

		for i in range(int(r[0]), int(r[1]) + 1):
			s = str(i)

			if len(s) % 2 == 0:
				s0, s1 = s[:len(s) // 2], s[len(s) // 2:]
		
				if s0 == s1:
					result += i

	return result

def solve_part2(data):
	result = 0

	for d in data:
		r = d.split("-")

		for i in range(int(r[0]), int(r[1]) + 1):
			if re.fullmatch(r"(.+)\1+", str(i)):
				result += i

	return result

print(solve_part1(L))
print(solve_part2(L))
