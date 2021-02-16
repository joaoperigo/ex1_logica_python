N = int(input())

for i in range(N):
	entrada = input()
	total = 0
	menor = 0
	for j in range(len(entrada)):
		if(entrada[j] == "<"):
			menor += 1
		if(entrada[j] == ">" and menor > 0):
			total += 1
			menor -= 1

	print(total)
