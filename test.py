boardList = [2,5,0,0,0,3,0,9,1,3,0,9,0,0,0,7,2,0,0,0,1,0,0,6,3,0,0,0,0,0,0,6,8,0,0,3,0,1,0,0,4,0,0,0,0,6,0,3,0,0,0,0,5,0,1,3,2,0,0,0,0,7,0,0,0,0,0,0,4,0,6,0,7,6,4,0,1,0,0,0,0]
board = []
for i in range(9):
	tempList = []
	for j in range(9):	
		tempList.append(boardList[j])	
	board.append(tempList)
	for k in range(9):
		boardList.pop(0)

def boardPrint(b):
	for row in range(9):
		print (b[row])
	print ("")
	
boardPrint(board)