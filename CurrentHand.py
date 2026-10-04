import PlayerHand
import DealerHand

class CurrentHand:
    def __init__(self, dealCard, checkIfBust, winner):
        self.result = None
        self.dealCard = dealCard
        self.checkIfBust = checkIfBust
        self.winner = winner

    def startHand(self):
        self.player = PlayerHand.PlayerHand()
        self.dealer = DealerHand.DealerHand()

        for i in range(2):
            self.givePlayerCard()
            self.dealer.dealerCards.append(self.dealCard())

        self.getPlayerDecision()
            

    def givePlayerCard(self):
         card = self.dealCard()
         if card == 11:
             self.player.numberOfAces += 1
         self.player.playerCards.append(card)

    def giveDealerCard(self):
        card = self.dealCard()
        if card == 11:
            self.dealer.numberOfAces += 1
        self.dealer.dealerCards.append(card)

    def getPlayerDecision(self):
        while True:
            if self.checkIfBust(self.player):
                self.winner.decideWinner(self.player, self.dealer)
                return

            print(f"Your Cards: {self.player.playerCards}")
            print(f"Dealer Cards: {self.dealer.dealerCards}")
            
            while True:
                print(f"Your total is {self.player.total}")
                print("H or S")
                self.PlayerDecision = input()

                if self.PlayerDecision in ["H", "S"]:
                    break

            if (self.PlayerDecision == "H"):
                 self.givePlayerCard()
            else:
                 self.dealerTurn()
                 return

    def dealerTurn(self):
        while self.dealer.total < 17:
            self.giveDealerCard()
            self.checkIfBust(self.dealer)

        self.winner.decideWinner(self.player, self.dealer)
