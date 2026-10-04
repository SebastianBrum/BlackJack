class PlayerHand:
    def __init__(self):
        self.name = "player"
        self._total = 0
        self.playerCards = []
        self.numberOfAces = 0
        self.isBust = False

    @property
    def total(self):
        return sum(self.playerCards)