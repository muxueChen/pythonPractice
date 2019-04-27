# 随机排列库
from random import shuffle

class Card:
    suits = ["♠️", "♥️", "♣️", "♦️"]
    values = [None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    # v 数字
    # s 花色
    def __init__(self, v, s):
        """
        suit 和 value 的值都为整数型
        """
        self.value = v
        self.suit = s

    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False

    def __gt__(self, value):
        if self.value > value.value:
            return True
        if self.value == value.value:
            if self.suit > value.value:
                return True
            else:
                return False
        return False
    
    def __repr__(self):
        v =  self.suits[self.suit] + " " + self.values[self.value]
        return v

# 牌堆
class Deck:
    def __init__(self):
        self.cards = []
        # 创建一副牌
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
        
        # 洗牌
        shuffle(self.cards)

    # 发牌
    def rm_card(self):
        if len(self.cards) <= 0:
            return None
        return self.cards.pop()

# 玩家
class Player:
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.card = None
        
# 游戏
class game:
    def __init__(self):
        name1 = input("玩家1的名字:")
        name2 = input("玩家2的名字:")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    # 玩家赢的数量
    def wins(self, winner):
        w = "{} wins this round"
        w = w.format(winner)
        print(w)
    
    # 玩家抓到的牌
    def draw(self, p1n, p1c, p2n, p2c):
        d = "{} : {} ,{} : {}"
        d = d.format(p1c, p1n, p2c, p2n)
        print(d)
    
    # 开始玩游戏
    def palyer_game(self):
        cards = self.deck.cards
        print("beginning war!")
        while len(cards) >= 2:
            m = "输入 q 退出， 输入其他任意键开始游戏:"
            response = input(m)
            if response is 'q':
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name

            self.draw(p1n, p1c, p2c, p2n)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)

        win = self.winner(self.p1, self.p2)
        print ("游戏结束. {} 赢".format(win))

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "It was a tie!"

if __name__ == '__main__':
    play = game()
    play.palyer_game()