from itertools import combinations
import re
#import scipy.optimize

L = [c.strip() for c in open("data/day10.txt", "r")]

def parse(data):
	machines = []

	for line in data:
		light = 0
		buttons = []
		joltages = []
		
		m = re.search(r"(\[.*\]) (.*) (\{.*\})", line)
		if m:
			indicators = list(m.group(1).replace("[", "").replace("]", ""))
			indicators.reverse()

			for i, val in enumerate(indicators):
				if val == '#':
					light += 2 ** i

			buttons = []

			for button in m.group(2).split(" "):
				b = 0

				for val in button.replace("(", "").replace(")", "").split(","):
					b |= 1 << (len(indicators) - 1 - int(val))

				buttons.append(b)

			joltages.append(m.group(3))

		machines.append((light, buttons, joltages))

	return machines
	
def solve_part1(data):
	result = 0
	machines = parse(data)
	
	for light, buttons, _ in machines:
		min_presses = 16384

		for j in range(1, len(buttons)):
			for button in combinations(buttons, j):
				num = 0
				presses = 16384

				for i, p in enumerate(button):
					num ^= p

					if num == light:
						presses = i + 1
						break

				min_presses = min(min_presses, presses)

			if min_presses < 16384:
				result += min_presses
				break

	return result

print(solve_part1(L))
