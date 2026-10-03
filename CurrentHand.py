import PlayerHand
import DealerHand

class CurrentHand:
    def __init__(self, dealCard, checkIfBust):
        self.result = None
        self.dealCard = dealCard
        self.checkIfBust = checkIfBust

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

    def getPlayerDecision(self):
        while True:
            if self.checkIfBust(self.player):
                print("You are bust")
                return
            while True:
                print(f"Your total is {self.player.playerTotal}")
                print("H or S")
                self.PlayerDecision = input()

                if self.PlayerDecision in ["H", "S"]:
                    break

            if (self.PlayerDecision == "H"):
                 self.givePlayerCard()
            else:
                 return