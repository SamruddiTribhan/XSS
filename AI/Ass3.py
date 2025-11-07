# assignment 3: Minimax Algorithm for Tic-Tac-Toe

# using easyAI library and negamax strategy variant of minimax algorithm
# from easyAI import TwoPlayerGame, Human_Player, AI_Player, Negamax

# class TicTacToe(TwoPlayerGame):
#     def __init__(self, players):
#         self.players = players
#         self.board = [0] * 9
#         self.current_player = 1
#
#     def possible_moves(self):
#         return [i + 1 for i, spot in enumerate(self.board) if spot == 0]
#
#     def make_move(self, move):
#         self.board[int(move) - 1] = self.current_player
#
#     def show(self):
#         board_display = ['.', 'X', 'O']
#         print('\n'.join([
#             ' '.join([board_display[self.board[3*i + j]] for j in range(3)])
#             for i in range(3)
#         ]))
#         print()
    
#     def is_win(self):
#         board = self.board
#         lines = [
#             [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
#             [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
#             [0, 4, 8], [2, 4, 6]               # diagonals
#         ]
#         return any(board[a] == board[b] == board[c] == self.current_player 
#                    for a, b, c in lines)
    
#     def is_over(self):
#         return self.is_win() or len(self.possible_moves()) == 0
    
#     def scoring(self):
#         if self.is_win():
#             return 100
#         return 0

# def play_game():
#     # AI uses Negamax (variant of Minimax) with depth 9 for perfect play
#     ai_algo = Negamax(9)
#     game = TicTacToe([Human_Player(), AI_Player(ai_algo)])
    
#     game.play()
#     game.show()
    
#     if game.is_win():
#         print(f"Player {3 - game.current_player} wins!")
#     else:
#         print("It's a draw!")

# if __name__ == "__main__":
#     play_game()



# Tic-Tac-Toe Game using Minimax Algorithm (Simplified)

board = [0, 0, 0,
         0, 0, 0,
         0, 0, 0]

def print_board():
    
    """Show the game board"""
    symbols = {0: ' ', 1: 'O', -1: 'X'}
    print("\n")

    for i in range(3):
        print(f" {symbols[board[i*3]]} | {symbols[board[i*3+1]]} | {symbols[board[i*3+2]]} ")
        if i < 2:
            print("-----------")
    print("\n")




def check_winner():
    """Check who won: 1=AI, -1=Human, 0=No winner"""
    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    
    for combo in wins:
        a, b, c = combo
        if board[a] == board[b] == board[c] != 0:
            return board[a]
    return 0



def is_full():
    """Check if all cells are filled"""
    return 0 not in board



def minimax(depth, is_ai):
    """
    Find the best score:
    - is_ai=True: AI turn (try to win, return high score)
    - is_ai=False: Human turn (try to lose, return low score)
    """
    winner = check_winner()
    
    # Stop if game is over
    if winner == 1:
        return 10
    if winner == -1:
        return -10
    if is_full():
        return 0
    
    if is_ai:
        # AI's turn - find the BEST score
        best = -1000
        for i in range(9):
            if board[i] == 0:
                board[i] = 1
                score = minimax(depth + 1, False)
                board[i] = 0
                best = max(best, score)
        return best
    else:
        # Human's turn - find the WORST score (from AI's view)
        worst = 1000
        for i in range(9):
            if board[i] == 0:
                board[i] = -1
                score = minimax(depth + 1, True)
                board[i] = 0
                worst = min(worst, score)
        return worst
    



def ai_move():
    """AI picks the best move"""
    best_score = -1000
    best_spot = 0
    
    for i in range(9):
        if board[i] == 0:
            board[i] = 1
            score = minimax(0, False)
            board[i] = 0
            
            if score > best_score:
                best_score = score
                best_spot = i
    
    return best_spot





def play():
    """Main game"""
    global board
    board = [0] * 9
    
    print("=== TIC-TAC-TOE ===")
    print("You=X, AI=O")
    print("Positions:\n 0|1|2\n 3|4|5\n 6|7|8\n")
    
    while True:
        print_board()
        
        # Your turn
        while True:
            move = int(input("Your move (0-8): "))
            if 0 <= move <= 8 and board[move] == 0:
                board[move] = -1
                break
            print("Bad move!")
        
        if check_winner() == -1:
            print_board()
            print("You won!")
            break
        if is_full():
            print_board()
            print("Draw!")
            break
        
        # AI turn
        ai_pos = ai_move()
        board[ai_pos] = 1
        print(f"AI plays at {ai_pos}")
        
        if check_winner() == 1:
            print_board()
            print("AI won!")
            break
        if is_full():
            print_board()
            print("Draw!")
            break




if __name__ == "__main__":
    play()