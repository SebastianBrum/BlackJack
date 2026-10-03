class PlayerHand:
    def __init__(self):
        self._playerTotal = 0
        self.playerCards = []
        self.numberOfAces = 0

    @property
    def playerTotal(self):
        return sum(self.playerCards)