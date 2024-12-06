lines = list(open("input.txt"))
#lines = list(open("test"))

# Parse input
rules = lines[:lines.index("\n")]
rules = [(int(a), int(b)) for (a, b) in [rule.split('|') for rule in rules]]

pages = lines[lines.index("\n"):]
pages = [[int(no) for no in page.rstrip().split(',') if len(no) != 0] for page in pages if len(page) > 1]

def test(page):
	safe = True
	for rule in rules:
		if rule[0] in page and rule[1] in page:
			if page.index(rule[0]) > page.index(rule[1]):
				safe = False
	return safe

print(sum([page[len(page)//2] for page in pages if test(page)]))

def reorder(page):
	if test(page): return 0
	# Create a copy
	page = [x for x in page]
	# Fix the ordering
	total = 0;
	while not test(page):
		for rule in rules:
			if rule[0] in page and rule[1] in page:
				idx0 = page.index(rule[0])
				idx1 = page.index(rule[1])
				# If the order is wrong, swap it
				if idx0 > idx1:
					total += 1
					(page[idx0], page[idx1]) = (page[idx1], page[idx0])
	print(total)
	return page[len(page)//2]

print(sum([reorder(page) for page in pages]))
