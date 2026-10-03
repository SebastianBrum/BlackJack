import random
import PlayerHand
import DealerHand

class Cards:
    CARD_BUCKET = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

class Game:
    def startHand(self):
        self.player = PlayerHand.PlayerHand()
        self.dealer = DealerHand.DealerHand()

        for i in range(2):
            self.player.playerCards.append(self.dealCard())
            self.dealer.dealerCards.append(self.dealCard())

    def dealCard(self):
        return random.choice(Cards.CARD_BUCKET)

game = Game()

game.startHand()


print( f"{game.player.playerTotal > game.dealer.dealerTotal}")