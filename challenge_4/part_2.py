from functools import reduce
from typing import List

def winner(bingo_score_board: List[List[int]]) -> bool:

    # Check the rows
    for i in range(len(bingo_score_board)):
        if reduce(lambda a,b: (a*b), bingo_score_board[i]) == 1:
            return True

    # Check the cols
    for j in range(len(bingo_score_board[0])):
        col: List[int] = []
        for i in range(len(bingo_score_board)):

            col.append(bingo_score_board[i][j])

        if reduce(lambda a,b: (a*b), col) == 1:
            return True
    return False

def sum_unmarked_nums(bingo_board: List[List[str]], bingo_score_board: List[List[int]]) -> int:
    
    sum_u = 0
    for r, row in enumerate(bingo_board):
        for c, _ in enumerate(row):
            if bingo_score_board[r][c] == 0:
                sum_u += int(bingo_board[r][c])

    return sum_u

def play_bingo(bingo_numbers: List[str],bingo_boards: List[List[List[str]]], bingo_score_boards: List[List[List[int]]]) -> int :
    last_score: int
    already_won: List[int] = []
    for _, number in enumerate(bingo_numbers):

        for j, board in enumerate(bingo_boards):

            for r, row in enumerate(board):
                for c, _ in enumerate(row):

                    if board[r][c] == number:
                        bingo_score_boards[j][r][c] = 1
                        
            if j not in already_won and winner(bingo_score_boards[j]):
                last_score = int(number) * sum_unmarked_nums(board, bingo_score_boards[j])
                already_won.append(j)
    return last_score

def main() -> None:
    with open("input.txt") as bingo_file:
        bingo_array = [bingo.split("\n") for bingo in bingo_file.read().split("\n\n")]

    bingo_numbers = bingo_array[0][0].split(",")
    bingo_boards = [ 
        [ 
            bingo_array[i][j].strip().split() 
            for j in range(len(bingo_array[i]))
        ]
        for i in range(1, len(bingo_array))
    ] 
    
    bingo_score_boards =  [ 
        [
            [ 
              
                  0 for _ in range(5)
                  
            
        ] for _ in range(len(bingo_array[i]))]
        for i in range(1, len(bingo_array))
    ] 

    print(play_bingo(bingo_numbers, bingo_boards, bingo_score_boards))

if __name__ == "__main__":
    main()