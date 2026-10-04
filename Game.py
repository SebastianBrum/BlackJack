import random
import Cards
import CurrentHand
import Winner

class Game:
    winner = Winner.Winner()

    def dealCard(self):
        return random.choice(Cards.Cards.CARD_BUCKET)

    def checkIfBust(self, player):
        if(player.total > 21):
            if player.numberOfAces > 0:
                self.changeAces(player)
            else:
                player.isBust = True
                print(f"{player.name} has busted")
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
    currentHand = CurrentHand.CurrentHand(game.dealCard, game.checkIfBust, game.winner)
    currentHand.startHand()

    print(f"{game.winner.winner} won this hand")
    print(f"Record: {game.winner.winCount}")
    print(f"{currentHand.player.total} : {currentHand.dealer.total}")

    print ("Play again? Y/N")
    playAgain = input()

    if (playAgain != "Y"):
        break