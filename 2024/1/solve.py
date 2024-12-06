list1 = []
list2 = []

for line in open("input.txt"):
	(loc1, loc2) = line.split("   ")
	list1.append(int(loc1))
	list2.append(int(loc2))

list1.sort()
list2.sort()

total = 0
for (item1, item2) in zip(list1, list2):
	total += abs(item1 - item2)

print("Part 1:", total)

similarity = 0

for item in list1:
	in2 = len([x for x in list2 if x == item])
	similarity += in2 * item


print("Part 2:", similarity)
