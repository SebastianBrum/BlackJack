class DealerHand:
    def __init__(self):
        self.dealerCards = []
        self._dealerTotal = 0

    @property
    def dealerTotal(self):
        return sum(self.dealerCards)