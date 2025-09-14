Tic-Tac-Toe AI with Alpha-Beta PruningA classic Tic-Tac-Toe game built with Python and Pygame, featuring a powerful AI opponent that uses the Minimax algorithm with Alpha-Beta pruning for optimal move selection.FeaturesInteractive GUI: A clean and responsive graphical interface built with Pygame.Intelligent AI: An unbeatable AI opponent that uses the Minimax algorithm to find the optimal move.Alpha-Beta Pruning: The AI's decision-making is optimized for speed and efficiency.Multiple Game Modes:Player vs. AI: Challenge the computer.Player vs. Player (PvP): Play against a friend on the same screen.Adjustable AI Difficulty:Level 0: AI plays randomly (great for beginners).Level 1: AI plays perfectly using the full algorithm.Visual Feedback: The winning line is drawn on the board when a player wins.How to Get StartedPrerequisitesPython 3.7 or newerPygame libraryNumPy libraryInstallationClone the repository:git clone [https://github.com/your-username/your-repository.git](https://github.com/siddhm11/your-repository.git)
cd your-repository
Install the required packages:pip install pygame numpy
Run the game:python py-ttt-neat.py
How to PlayThe goal is simple: be the first player to get three of your marks in a row, either horizontally, vertically, or diagonally.ControlsKeyActionMouse ClickPlace your 'X' or 'O' in an empty square.RReset the game and start a new match.GToggle between Player vs. AI and PvP modes.0Set the AI to random mode (Level 0).1Set the AI to optimal/unbeatable mode (Level 1).Technical DetailsProject Structure.
├── py-ttt-neat.py      # Main application logic, including the Game and AI classes.
├── CONSTANTS_TTT.PY    # Contains all game constants like colors, dimensions, etc.
└── readme.md           # This file
The AI AlgorithmThe AI's brain is powered by the Minimax algorithm, a classic decision-making algorithm from game theory.Minimax: It simulates every possible move down to the end of the game, assigning a score to each outcome (win, lose, or draw). It then chooses the move that leads to the best possible outcome for itself, assuming the opponent will also play optimally.Alpha-Beta Pruning: To avoid the massive computation of checking every single game state, this optimization "prunes" branches of the game tree that are not worth exploring. This makes the AI's decision-making significantly faster without sacrificing accuracy.


THIS IS A SAMPLE GAME WHERE THE AI IS CIRCLE 

![image](https://github.com/user-attachments/assets/ec074965-2d28-442b-bcc2-44ed6db0c80e)

when i press R (RESET)

![image](https://github.com/user-attachments/assets/0613f371-0537-4622-a714-694b8f72ed85)

ANOTHER GAME

![image](https://github.com/user-attachments/assets/1a572483-1cdf-4930-99b0-7166cc81fb43)

WHEN self.player = 1 , the user/human starts playing 

![image](https://github.com/user-attachments/assets/62785557-60c4-44e5-b2f0-a18d62bb990b)

when G is clicked , it means the pvp is started 

AND THIS IS THE ALPHA BETA PRUNING INITIATED CODE 

**
class AI :
    def __init__(self , level = 1 , player = 2 ):
        self.player = player
        self.level = level

    def rnd(self,board):
        empty_sqrs = board.get_empty_sqrs()
        idx = random.randrange(0,len(empty_sqrs))
        return empty_sqrs[idx]

    def minimax(self,board ,maximizing,alpha=-100 , beta = 100):
        #terminal cases check
        case = board.final_state()
        #player
        if case == 1 :
            return 1,None #eval , Move

        #ai
        if case == 2:
            return -1,None #eval , Move

        #draw
        elif board.isfull():
            return 0,None

        if maximizing:
            maxeval = -100
            best_move = None
            empty_sqrs = board.get_empty_sqrs()

            for (row, col) in empty_sqrs:
                temp_board = copy.deepcopy(board)
                temp_board.mark_sqr(row, col, 1)
                reval = self.minimax(temp_board, False,alpha , beta)[0]

                if reval>maxeval:
                    maxeval = reval
                    best_move = (row, col)

                alpha= max(alpha , reval)
                if alpha>=beta:
                    break

            return maxeval, best_move


        elif not maximizing:
            mineval = +1000
            best_move = None
            empty_sqrs = board.get_empty_sqrs()

            for (row, col) in empty_sqrs:
                temp_board = copy.deepcopy(board)
                temp_board.mark_sqr(row, col, 2)
                reval = self.minimax(temp_board,True, alpha , beta )[0]

                if mineval > reval :
                    mineval = reval
                    best_move = (row,col)
                beta = min(beta , reval)
                if alpha >= beta:
                    break

            return mineval , best_move


    def eval(self,main_board):
        if self.level == 0 :
            aeval = 'random'
            move = self.rnd(main_board)

        else:
            aeval,move = self.minimax(main_board, False)

        print(f'AI HAS CHOSEN TO MARK THE SQUARE IN POS{move} with an eval of {aeval}')

        return move #row,col
**
