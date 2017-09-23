def check(l):
	list1 = [1, 2, 3, 4, 5, 6, 7, 8, '']
	if l == list1:
		print("Congrats! Puzzle solved!")
		exit(0)

import random
data = list(range(1, 9))
data.append('')
random.shuffle(data)
# print(data)
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, '']
def print_board():
	print(data[0:3])
	print(data[3:6])
	print(data[6:9])

print_board()
print("Move the empty space to left, right, up, or down")

while(True):
	if data.index('') == 0:
		a = input("Enter your move")
		if a == "right":
			data[0], data[1] = data[1], data[0]
			print_board()
			check(data)
		elif a == "down":
			data[0], data[3] = data[3], data[0]
			print_board()
			check(data)
		else:
			print("Can't Move, Try other inputs")
			print_board()

	elif data.index('') == 1:
		a = input("Enter your move")
		if a == "left":
			data[0], data[1] = data[1], data[0]
			print_board()
			check(data)
		elif a == "right":
			data[1], data[2] = data[2], data[1]
			print_board()
			check(data)
		elif a == "down":
			data[1], data[4] = data[4], data[1]
			print_board()
			check(data)
		else:
			print("Can't Move, Try other inputs")
			print_board()

	elif data.index('') == 2:
		a = input("Enter your move")
		if a == "left":
			data[2], data[1] = data[1], data[2]
			print_board()
			check(data)
		elif a == "down":
			data[2], data[5] = data[5], data[2]
			print_board()
			check(data)
		else:
			print("Can't Move, Try other inputs")
			print_board()

	elif data.index('') == 3:
		a = input("Enter your move")
		if a == "up":
			data[0], data[3] = data[3], data[0]
			print_board()
			check(data)
		elif a == "right":
			data[3], data[4] = data[4], data[3]
			print_board()
			check(data)
		elif a == "down":
			data[3], data[6] = data[6], data[3]
			print_board()
			check(data)
		else:
			print("Can't Move, Try other inputs")
			print_board()

	elif data.index('') == 4:
		a = input("Enter your move")
		if a == "left":
			data[3], data[4] = data[4], data[3]
			print_board()
			check(data)
		elif a == "right":
			data[4], data[5] = data[5], data[4]
			print_board()
			check(data)
		elif a == "down":
			data[7], data[4] = data[4], data[7]
			print_board()
			check(data)
		elif a == "up":
			data[1], data[4] = data[4], data[1]
			print_board()
			check(data)
		else:
			print("Can't Move, Try other inputs")
			print_board()

	elif data.index('') == 5:
		a = input("Enter your move")
		if a == "left":
			data[5], data[4] = data[4], data[5]
			print_board()
			check(data)
		elif a == "up":
			data[5], data[2] = data[2], data[5]
			print_board()
			check(data)
		elif a == "down":
			data[5], data[8] = data[8], data[5]
			print_board()
			check(data)
		else:
			print("Can't Move, Try other inputs")
			print_board()

	elif data.index('') == 6:
		a = input("Enter your move")
		if a == "up":
			data[6], data[3] = data[3], data[6]
			print_board()
			check(data)
		elif a == "right":
			data[6], data[7] = data[7], data[6]
			print_board()
			check(data)
		else:
			print("Can't Move, Try other inputs")
			print_board()

	elif data.index('') == 7:
		a = input("Enter your move")
		if a == "left":
			data[7], data[6] = data[6], data[7]
			print_board()
			check(data)
		elif a == "right":
			data[7], data[8] = data[8], data[7]
			print_board()
			check(data)
		elif a == "up":
			data[7], data[4] = data[4], data[7]
			print_board()
			check(data)
		else:
			print("Can't Move, Try other inputs")
			print_board()

	elif data.index('') == 8:
		a = input("Enter your move")
		if a == "up":
			data[5], data[8] = data[8], data[5]
			print_board()
			check(data)
		elif a == "left":
			data[8], data[7] = data[7], data[8]
			print_board()
			check(data)
		else:
			print("Can't Move, Try other inputs")
			print_board()


