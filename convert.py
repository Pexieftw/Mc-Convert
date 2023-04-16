def romanToDecimal(s):
	romanMap = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
	result = 0
	prevVal = 0
	for c in s[::-1]:
		val = romanMap[c]
		result = result - val if (val < prevVal) else result + val
		prevVal = val
	
	return str(result)

text = '1100 since V/III/MCMLXXXV'
words = text.split()
roman = words[-1].split("/")
words[-1] = "/".join([romanToDecimal(r) for r in roman])
print(" ".join(words))