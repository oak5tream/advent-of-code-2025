L = [list(map(int, c.strip())) for c in open("data/day03.txt", "r")]

def calculate_joltage(bank, num):
	i = [0] * num
	v = [0] * num
	i_prev = 0

	for n in range(num):
		for b in range(i_prev, len(bank) - (num - (n + 1))):
			if bank[b] > v[n]:
				v[n] = bank[b]
				i[n] = b

		i_prev = i[n] + 1

	result = 0

	for i in range(num):
		result += v[i] * pow(10, num - i - 1)

	return result

def solve(banks, num):
	result = 0

	for bank in banks:
		result += calculate_joltage(bank, num)

	return result

print(solve(L, 2))
print(solve(L, 12))
