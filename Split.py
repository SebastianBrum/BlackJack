class Split:
    def __init__(self):
        self.newHand = [[], []]
    
    def splitHand(self, playerHand):
        self.newHand[0].append(playerHand[0])
        self.newHand[1].append(playerHand[1])

        return self.newHand