word = 'XMAS'
padding = len(word) - 1

search = list(open("input.txt"))
#search = list(open("test"))

h = len(search)
w = len(search[0].rstrip())
print("Size", h, w)


# Pad with spacing
search = ['.'*padding + line.rstrip() + '.'*padding  for line in search]
for i in range(padding): search.insert(0, "."*(padding*2 + w))
for i in range(padding): search.append(   "."*(padding*2 + w))

#for s in search: print(s)

directions = [
	[0, 1], [0, -1], [1, 0], [-1, 0],
	[1, 1], [1, -1], [-1, 1], [-1, -1],
]

count = 0
for search_x in range(h):
	for search_y in range(w):
		for d in directions:
			y = search_x + padding
			x = search_y + padding
			found = True
			for c in word:
				if (search[x][y] != c): found = False
				x += d[0]
				y += d[1]
			if found: count += 1
print("Part 1:", count)

# X-mas

# Only diagonals count
directions = [
	[1, 1], [1, -1], [-1, 1], [-1, -1],
]

x_mas = 0
for search_x in range(h):
	for search_y in range(w):
		y = search_x + padding
		x = search_y + padding
		# All X-MAS must have an A in the center
		if search[x][y] != 'A': continue
		mas_count = 0;
		for d in directions:
			start = search[x + d[0]][y + d[1]]
			end   = search[x - d[0]][y - d[1]]
			# To count, a MAS must have another at right angles
			if start == 'M' and end == 'S':
				start = search[x - d[1]][y + d[0]]
				end = search[x + d[1]][y - d[0]]
				if start == 'M' and end == 'S': x_mas += 1;
				if start == 'S' and end == 'M': x_mas += 1;
x_mas = x_mas // 2

print("Part 2:", x_mas)
			

				
