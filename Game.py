import random
import PlayerHand
import DealerHand
import Cards
import CurrentHand

class Game:
    def dealCard(self):
        return random.choice(Cards.Cards.CARD_BUCKET)

    def checkIfBust(self, player):
        if(player.playerTotal > 21):
            if player.numberOfAces > 0:
                self.changeAces(player)
            else:
                return True
        else:
            return False

    def changeAces(self, player):
        for index, card in enumerate(player.playerCards):
            if (card == 11):
                player.playerCards[index] = 1
                player.numberOfAces -= 1
                break
        
        self.checkIfBust(player)
                


game = Game()

while True:
    currentHand = CurrentHand.CurrentHand(game.dealCard, game.checkIfBust)
    currentHand.startHand()

    print(currentHand.player.playerTotal > currentHand.dealer.dealerTotal)
    print(f"{currentHand.player.playerTotal} : {currentHand.dealer.dealerTotal}")

    print ("Play again? Y/N")
    playAgain = input()

    if (playAgain != "Y"):
        break