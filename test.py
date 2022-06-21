import copy
board = []
def boardSet(boardRawInput):
	if isinstance(boardRawInput, str) and len(boardRawInput) == 81:
		board.clear()
		for i in range(9):
			tempList = []
			for j in range(9):
				tempList.append(int(boardRawInput[i * 9 + j]))
			board.append(tempList)
	elif isinstance(boardRawInput, list):
		if isinstance(boardRawInput[0], int) and len(boardRawInput) == 81:
			board.clear()
			for i in range(9):
				tempList = []
				for j in range(9):
					tempList.append(boardRawInput[j])
				board.append(tempList)
		elif isinstance(boardRawInput[0], list) and len(boardRawInput) == 9 and len(boardRawInput[0]) == 9:
			board.deepcopy(boardRawInput)
		else:
			return False