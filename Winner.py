class Winner:
    def __init__(self):
        self.winner = None
        self.winCount = {
                         "Player" : 0,
                         "Dealer": 0
                        }

    def decideWinner(self, player, dealer):
        if (player.total == dealer.total):
            self.winner = "Noone"
            return

        playerWon = self.checkIfPlayerWon(player.total, dealer.total)

        if playerWon:
            winner = "Dealer" if player.isBust else "Player"
        else:
            winner = "Player" if dealer.isBust else "Dealer"
        self.updateWinnerDetails(winner)
            

    def checkIfPlayerWon(self, playerTotal, dealerTotal):
        return playerTotal > dealerTotal

    def updateWinnerDetails(self, winner):
        self.winner = winner
        self.winCount[winner] += 1