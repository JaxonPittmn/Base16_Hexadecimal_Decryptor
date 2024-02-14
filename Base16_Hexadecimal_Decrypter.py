digits = {'F': 0,
				 'E': 1,
				 'D': 2,
				 'C': 3,
				 'B': 4,
				 'A': 5,
				 '9': 6,
				 '8': 7,
				 '7': 8,
				 '6': 9,
				 '5': 10,
				 '4': 11,
				 '3': 12,
				 '2': 13,
				 '1': 14,
				 '0': 15}


def Challenge():
	groupings = []
	val = 0
	decode = ""
	scheme = input("Proprietary Scheme:\n")
	for i in range(len(scheme)):
		if not i % 2:
			continue
		groupings.append(scheme[i-1:i+1])

	for group in groupings:
		for i,letter in enumerate(group):
			if i == 0:
				val += digits[letter] * 16
			elif i == 1:
				val += digits[letter]
		decode += chr(val)
		val = 0
	print(decode)
Challenge()
