import re

total = 0
for line in open("input.txt"):
	instructions = re.findall("mul\\(\\d+,\\d+\\)", line)
	for command in instructions:
		(a, b) = re.findall('[1234567890]+', command)
		total += (int(a) * int(b))
print(total)

total = 0
do = True
for line in open("input.txt"):
	instructions = re.findall("(mul\\(\\d+,\\d+\\))|(do\\(\\))|(don't\\(\\))", line)
	for command in instructions:
		if command[0] and do:
			(a, b) = re.findall('[1234567890]+', command[0])
			total += (int(a) * int(b))
		if command[1]: do = True
		if command[2]: do = False
print(total)
