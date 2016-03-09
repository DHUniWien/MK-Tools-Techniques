allnumbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

num = int(input("Choose a number: "))

new_list = []

for item in allnumbers:
	if item < num:
		new_list.append(item)

print(new_list)