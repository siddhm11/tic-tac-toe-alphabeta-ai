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
