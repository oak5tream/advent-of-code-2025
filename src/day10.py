from itertools import combinations
import re
import z3

L = [c.strip() for c in open("data/day10.txt", "r")]

def parse(data, bitwise_buttons = True):
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
				button_list = list(map(int, button.replace("(", "").replace(")", "").split(",")))
				
				if bitwise_buttons:
					for val in button_list:
						b |= 1 << (len(indicators) - 1 - val)

					buttons.append(b)
				else:
					buttons.append(button_list)

			joltages = list(map(int, m.group(3).replace("{", "").replace("}", "").split(",")))

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

def solve_part2(data):
	result = 0

	machines = parse(data, False)

	for _, buttons, joltages in machines:
		solver = z3.Optimize()
		variables = []
		joltage_vars = [None] * len(joltages)

		for i, button in enumerate(buttons):
			z3_var = z3.Int(str(i))

			variables.append(z3_var)

			solver.add(z3_var >= 0)

			for button_val in button:
				if joltage_vars[button_val] is None:
					joltage_vars[button_val] = z3_var
				else:
					joltage_vars[button_val] = joltage_vars[button_val] + z3_var

		for i, _ in enumerate(joltages):
			if joltage_vars[i] is None:
				continue

			solver.add(joltages[i] == joltage_vars[i])

		presses = solver.minimize(sum(variables))

		if solver.check() == z3.sat:
			result += presses.value().as_long()

	return result

print(solve_part1(L))
print(solve_part2(L))
