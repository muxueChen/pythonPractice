
def hangman(word):
    # 错误的次数
    wrong = 0
    stages = ["",
        "_______              ",
        "|                    "
        "|        |           ",
        "|        O           ",
        "|       /|\          ",
        "|       / \          ",
        "|                    "
    ]
    # 用来记录word 中的每一个字母
    rletters = list(word)
    win = False
    board = ["_"]*len(word)
    print("Welcome to Hangeman")
    # 只要答错的次数小于划线的次数，证明还活着，可以继续c答题
    while wrong < len(stages) - 1:
        print("\n")
        msg = "guess a letter:"
        # 用户输入字母
        char = input(msg)
        # 输入的字母存在单词中，说明答对了一个字母
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("You win!")
            print("".join(board))
            win = True
            break
    
    if win == False:
        print("game over!!!")

if __name__ == '__main__':
    hangman('hello')