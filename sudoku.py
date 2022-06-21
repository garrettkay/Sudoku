import pygame
import sqlite3 as sql

boardString = "200800000904602031600009800000405062409700100060000070000007006000390200090080053"
board = []
for i in range(9):
	tempList = []
	for j in range(9):
		tempList.append(int(boardString[i * 9 + j]))
	board.append(tempList)

boardPoss= [[[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]],
			[[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]],
			[[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]],
			[[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]],
			[[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]],
			[[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]],
			[[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]],
			[[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]],
			[[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]]]

def boardPossSet():
	for r in range(9):
		for c in range(9):
			if board[r][c] != 0:
				boardPoss[r][c].clear()
				boardPoss[r][c].append(board[r][c])
def boxRowCheck(r):
	if r in range(0,3):
		return 0
	elif r in range(3,6):
		return 1
	else:
		return 2
def boxColCheck(c):
	if c in range(0,3):
		return 0
	elif c in range(3,6):
		return 1
	else:
		return 2
def cellCheck():
	for r in range(9):
		for c in range(9):
			if board[r][c] == 0:
				for row in range(9):
					if board[row][c] in boardPoss[r][c]:
						boardPoss[r][c].remove(board[row][c])
				for col in range(9):
					if board[r][col] in boardPoss[r][c]:
						boardPoss[r][c].remove(board[r][col])
				boxRow = boxRowCheck(r)
				boxCol = boxColCheck(c)
				for bRow in range(3):
					for bCol in range(3):
						if  board[boxRow*3+bRow][boxCol*3+bCol] in boardPoss[r][c]:
							boardPoss[r][c].remove(board[boxRow*3+bRow][boxCol*3+bCol])
def cellSolve():
	for row in range(9):
		for col in range(9):
			if board[row][col] == 0 and len(boardPoss[row][col]) == 1:
				board[row][col]=boardPoss[row][col][0]
				boardPoss[row][col].clear()
				boardPoss[row][col].append(board[row][col])
def rowSolve():
	for num in range(1,10):
		for r in range(9):
			count = 0
			pos = -1
			br = False
			for c in range(9):
				if board[r][c] == num:
					br = True
					break
				if num in boardPoss[r][c]:
					count = count + 1
					pos = c
			if count == 1 and not br:
				board[r][pos] = num
				boardPoss[r][pos].clear()
				boardPoss[r][pos].append(num)
def colSolve():
	for num in range(1,10):
		for c in range(9):
			count = 0
			pos = -1
			br = False
			for r in range(9):
				if board[r][c] == num:
					br = True
					break
				if num in boardPoss[r][c]:
					count = count + 1
					pos = r
			if count == 1 and not br:
				board[pos][c] = num
				boardPoss[pos][c].clear()
				boardPoss[pos][c].append(num)
def boxSolve():
	for num in range(1,10):
		for boxRow in range(3):
			for boxCol in range(3):
				count = 0
				posR = -1
				posC = -1
				br = False
				for bRow in range(3):
					for bCol in range(3):
						if board[boxRow*3 + bRow][boxCol*3 + bCol] == num:
							br = True
							break
						if num in boardPoss[boxRow*3 + bRow][boxCol*3 + bCol]:
							count = count + 1
							posR = boxRow*3 + bRow
							posC = boxCol*3 + bCol
				if count == 1 and not br:
					board[posR][posC] = num
					boardPoss[posR][posC].clear()
					boardPoss[posR][posC].append(num)
def randomSolve():
	global board
	boardPoints = []
	rcPoints = []
	posPoints = []
	rc = 0
	pos = 0
	while rc < 81:
		r = int(rc % 9)
		c = int(rc / 9)
		if len(boardPoss[r][c]) > 1:
			while pos < len(boardPoss[r][c]):
				board[r][c] = boardPoss[r][c][pos]
				if isValid():
					boardPoints.append([])
					for row in range(9):
						boardPoints[-1].append(board[row][:])
					boardPoints[-1][r][c] = 0
					rcPoints.append(rc)
					posPoints.append(pos)
					break
				else:
					pos = pos + 1
					continue
		if pos >= len(boardPoss[r][c]):
			board.clear()
			for r in range(9):
				board.append(boardPoints[-1][r][:])
			del boardPoints[-1]
			rc = rcPoints[-1]
			del rcPoints[-1]
			pos = posPoints[-1] + 1
			del posPoints[-1]
		else:
			pos = 0
			rc = rc + 1
def isValid():
	global board
	for r in range(9):
		for c in range(9):
			if board[r][c] != 0:
				for row in range(9):
					if row != r and board[r][c] == board[row][c]:
						return False
				for col in range(9):
					if col != c and board[r][c] == board[r][col]:
						return False
				boxRow = boxRowCheck(r)
				boxCol = boxColCheck(c)
				for bRow in range(3):
					for bCol in range(3):
						if (boxRow*3 + bRow != r or boxCol*3 + bCol != c) and board[r][c] == board[boxRow*3 + bRow][boxCol*3 + bCol]:
							return False
	return True
def boardPrint(b):
	for row in range(9):
		print (b[row])
	print ("")
def boardSave():
	tempBoard = []
	for r in range(9):
		tempBoard.append(board[r][:])
	return tempBoard
def boardPossSave():
	tempBoardPoss = []
	for r in range(9):
		tempBoardPoss.append([])
		for c in range(9):
			tempBoardPoss.append(boardPoss[r][c][:])
	return tempBoardPoss

boardPrint(board)
boardPossSet()
for a in range(10):
	cellCheck()
	cellSolve()
	rowSolve()
	colSolve()
	boxSolve()
# randomSolve()
boardPrint(board)