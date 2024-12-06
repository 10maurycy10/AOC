import tqdm

lab_map = list(open("input.txt"))
#lab_map = [str(line) for line in open("test")]
h = len(lab_map)
w = len(lab_map[0].strip())

obsticles = []
guard = None
for (i, line) in enumerate(lab_map):
	obsticles.append([c == '#' for c in line.rstrip()])
	assert(len(line.rstrip()) == w)
	if '^' in line:
		guard = (i, line.index('^'))
print("Guard is at", guard)

def check_loop(start_x, start_y, obs, extra_x, extra_y):
	visited = [[False for x in range(w)] for y in range(h)]
	position = [start_x, start_y]
	route = [[None for x in range(w)] for y in range(h)]
	position = [guard[0], guard[1]]

	if start_x == extra_x and start_y == extra_y: return (False, 0)

	visited[position[0]][position[1]] = True
	direction = [-1, 0]
	while True:
		position[0] += direction[0]
		position[1] += direction[1]
		if position[0] < 0 or position[0] >= h: break
		if position[1] < 0 or position[1] >= w: break
		if obsticles[position[0]][position[1]] or (position[0] == extra_x and position[1] == extra_y):
			position[0] -= direction[0]
			position[1] -= direction[1]
			(direction[0], direction[1]) = (direction[1], -direction[0])
		# Record route taken and check for loops
		if route[position[0]][position[1]] == (direction[0], direction[1]):
			return (True, None)
		elif not route[position[0]][position[1]]:
			route[position[0]][position[1]] = (direction[0], direction[1])

		visited[position[0]][position[1]] = True
	return (False, sum([sum(line) for line in visited]))

print("Part 1:", check_loop(guard[0], guard[1], obsticles, -1, -1)[1])

spots = 0
for x in tqdm.tqdm(range(h)):
#	line = ""
	for y in range(w): 
		creates_loop = check_loop(guard[0], guard[1], obsticles, x, y)[0]
		if (creates_loop):
			spots += 1
#			line += 'X'
#		else:
#			line += lab_map[x][y]
#	print(line)
		
print("Part 2", spots)
