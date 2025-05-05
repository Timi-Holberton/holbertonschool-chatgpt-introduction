#!/usr/bin/python3

def print_board(board):
	for row in board:
		print(" | ".join(row))
		print("-" * 5)

def check_winner(board):
	# Vérification des lignes
	for row in board:
		if row.count(row[0]) == len(row) and row[0] != " ":
			return True

	# Vérification des colonnes
	for col in range(len(board[0])):
		if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
			return True

	# Vérification des diagonales
	if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
		return True

	if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
		return True

	return False

def check_draw(board):
	# Vérifier si la partie est un match nul (toutes les cases sont remplies sans gagnant)
	for row in board:
		if " " in row:
			return False
	return True

def tic_tac_toe():
	board = [[" "]*3 for _ in range(3)]
	player = "X"

	while not check_winner(board) and not check_draw(board):
		print_board(board)

		# Demander à l'utilisateur de saisir la ligne et la colonne avec vérification des entrées
		try:
			row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
			col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))

			# Vérification si l'entrée est valide (entre 0 et 2)
			if row not in [0, 1, 2] or col not in [0, 1, 2]:
				print("Invalid row or column! Please enter values between 0 and 2.")
				continue

			if board[row][col] == " ":
				board[row][col] = player
				if player == "X":
					player = "O"
				else:
					player = "X"
			else:
				print("That spot is already taken! Try again.")

		except ValueError:
			print("Invalid input! Please enter numbers only.")

	# Afficher le résultat
	print_board(board)
	if check_winner(board):
		print("Player " + ("X" if player == "O" else "O") + " wins!")
	else:
		print("It's a draw!")

tic_tac_toe()
