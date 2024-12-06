
reports = []

for report in open('input.txt'):
	reports.append([int(x) for x in report.split(" ")])
print("Got",len(reports),"lines")

number_safe = 0
could_be_safe = 0

for report in reports:
	# Check if it is safe	
	if report[1] > report[0]:
		allowed = [1, 2, 3]
	else:
		allowed = [-1, -2, -3]
	
	safe = True
	for i in range(len(report) - 1):
		delta = report[i+1] - report[i]
		if delta not in allowed:
			safe = False
	if safe: number_safe += 1

	# Check if it could be made safe
	can_be_safe = safe
	for remove_no in range(len(report)):
		changed = [x for (i, x) in enumerate(report) if i != remove_no]	
		# Update allowed list
		if changed[1] > changed[0]:
			allowed = [1, 2, 3]
		else:
			allowed = [-1, -2, -3]
		assert(len(changed) + 1 == len(report))
		# Check safety
		safe = True
		for i in range(len(changed) - 1):
			delta = changed[i+1] - changed[i]
			if delta not in allowed: safe = False
		if safe: can_be_safe = True
	if can_be_safe: could_be_safe += 1

print(number_safe, "safe")
print(could_be_safe, "could be safe")

	
