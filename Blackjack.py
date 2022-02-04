import random
import math as m

def CreateDeck():
    Deck = []
    Faces = ["A", "J", "Q", "K"]
    for i in range(4):
        for carte in range(2,11):
            Deck.append(str(carte))
        for carte in Faces:
            Deck.append(carte)
    random.shuffle(Deck)
    return Deck

class Player:
    def __init__(self, hand = [], money = 100):
        self.hand = hand
        self.score = self.setScore()
        self.money = money
        self.bet = 0

    def __str__(self):
        cards_in_hand = ""
        for card in self.hand:
            cards_in_hand += str(card) + " "
        return "You got " + cards_in_hand + "with a total score of: " + str(self.score)
    
    def setScore(self):
        self.score = 0
        ace_score = 0
        pointsDict = {"A":11,"J":10, "Q":10, "K":10, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8,"9":9,"10":10}
        
        for cards in self.hand:
            if "A" in self.hand:
                ace_score +=1
            self.score += pointsDict[cards]

        if self.score > 21 and ace_score != 0:
            self.score -= 10
            ace_score -= 1
        return self.score       

    def drawCard(self, newCard):
        self.hand.append(newCard)
        self.score = self.setScore()
    
    def newHand(self, newHand):
        self.hand = newHand
        self.setScore()

    def betMoney(self, bet):
        self.money -= bet
        self.bet += bet

    def win(self, winCondition):
        if winCondition == True:
            if self.score == 21 and len(self.hand) == 2:
                self.money += m.ceil(2.5 * self.bet)
            else:
                self.money += 2*self.bet
            
            self.bet = 0
            print("The Player has won")
        else:
            self.bet = 0
            print("The Player has lost")
    
    def hasBlackjack(self):
        if self.score == 21 and len(self.hand) == 2:
            return True
        else:
            return False
        
    def Tie(self):
        self.money += self.bet
        self.bet = 0
        print("It's a tie")

    def setMoney(self, money):
        self.money = money

def printHouse(house):
    for card in range(len(house.hand)):
        if card == 0:
            print("X", end = " ")
        elif card == len(house.hand) - 1:
            print(house.hand[card])
        else:
            print(house.hand[card], end= " ")

def printHouse_final(house):
    cards_in_hand = " "
    for card in house.hand:
        cards_in_hand += card + " "
    print("The house has" + cards_in_hand + "with a total score of: " + str(house.score))

Deck = CreateDeck()
print(Deck)

Player_hand = []
House_hand = []

Player1 = Player(Player_hand)
House = Player(House_hand)

suma_intrare = int(input("Introdu suma pe care doresti sa o joci: "))
Player1.setMoney(suma_intrare)

while(True):
    
    if len(Deck) < 20:
        Deck = CreateDeck()
    
    Player_hand = [Deck.pop(),Deck.pop()]
    House_hand = [Deck.pop(),Deck.pop()]

    Player1.newHand(Player_hand)
    House.newHand(House_hand)

    Bet = int(input("Please insert the bet: "))
    Player1.betMoney(Bet)

    printHouse(House)
    print(Player1)

    if Player1.hasBlackjack():
        if House.hasBlackjack():
            Player1.Tie()
        else:
            Player1.win(True)
    else:

        while(Player1.score < 21):
            action = input ("Do you want to draw a card ? (y/n): ")
            if action == "y":
                Player1.drawCard(Deck.pop())
                print(Player1)
                printHouse(House)
            else:
                break
        while(House.score <17):
            House.drawCard(Deck.pop())
            printHouse(House)
        printHouse_final(House)

    if Player1.score > 21:   #De implementat, daca treci de 21, house nu mai trage carti si jocul se incheie
        if House.score > 21:
            Player1.Tie()
        else:
            Player1.win(False)
    elif Player1.score > House.score:
        Player1.win(True)
    elif Player1.score == House.score:
        Player1.Tie()
    else:
        if House.score > 21:
            Player1.win(True)
        else:
            Player1.win(False)

    print(Player1.money)

    continua = input("Do you wish to continue ? (yes/no): ")
    if continua == "yes":
        pass
    else:
        break