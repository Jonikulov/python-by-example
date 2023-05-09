# Challenge 147: Mastermind

import random

RULES = """Mastermind (board game):

1) Decoding board has 4 holes.
2) 6 code pegs: red, blue, green, yellow, purple, orange.
3) Key pegs: ⬛ - correct color in correct place,
             ⬜ - correct color in wrong place,
             _nothing_ - wrong color.
4) Duplicates allowed.
5) Blanks not allowed.
6) Codebreaker has 10 attempts.
"""

BOARD_HOLES = 4
CODEBREAK_ATTEMPTS = 10
COLORS = {'red':'🔴',
    'blue':'🔵',
    'green':'🟢',
    'yellow':'🟡',
    'purple':'🟣',
    'orange':'🟠'
}

print(RULES)
secret_code = random.choices(list(COLORS), k=BOARD_HOLES)

board = ""
win = False
for i in range(1, CODEBREAK_ATTEMPTS+1):
    print(f'\tAttempt {i}/{CODEBREAK_ATTEMPTS}:')

    user_cols = []
    while len(user_cols) < BOARD_HOLES:
        color = input(f'{len(user_cols)+1}-color: ').lower()
        if color not in COLORS:
            print("Invalid input.")
            continue
        user_cols.append(color)
    
    cols_row = "".join([COLORS[c] for c in user_cols]) + " | "
    
    # check black
    black_idx = []
    for i in range(BOARD_HOLES):
        if user_cols[i] == secret_code[i]:
            cols_row += '⬛'
            black_idx.append(i)
    
    # check white
    white_idx = {}
    for i in range(BOARD_HOLES):
        if (i not in black_idx) and (i not in white_idx):
            for j in range(BOARD_HOLES):
                if (j not in black_idx) and (j not in white_idx.values()):
                    if user_cols[i] == secret_code[j]:
                        cols_row += '⬜'
                        white_idx[i] = j
                        break

    board += cols_row + '\n'
    print(board)

    if '⬛'*4 in cols_row:
        win = True
        break

if win:
    print("You win!")
else:
    print(f"You lose. Secret code:\n{secret_code}")