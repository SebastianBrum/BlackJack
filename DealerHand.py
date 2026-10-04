class DealerHand:
    def __init__(self):
        self.name = "Dealer"
        self.dealerCards = []
        self._total = 0
        self.numberOfAces = 0
        self.isBust = False

    @property
    def total(self):
        return sum(self.dealerCards)