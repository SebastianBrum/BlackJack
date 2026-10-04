import PlayerHand
import DealerHand
import Split

class CurrentHand:
    #
    # Initialize a new hand to be played
    # 
    # @param {func} dealCard - The function to deal a card to the player/dealer
    # @param {func} checkIfBust - The function to check if the player/dealer is bust
    # @param {object} winner - The winner object
    def __init__(self, dealCard, checkIfBust, winner):
        self.result = None
        self.dealCard = dealCard
        self.checkIfBust = checkIfBust
        self.winner = winner

        self.Splitting = Split.Split()

    #
    # Starts a new hand
    #
    def startHand(self):
        #Initialize a new player and dealer
        self.player = PlayerHand.PlayerHand()
        self.dealer = DealerHand.DealerHand()

        #Deals 2 cards each to the dealer and the player
        for i in range(2):
            self.givePlayerCard()
            self.giveDealerCard()

        #Game continues to the player's turn
        self.playerTurn()

    #       
    # Give the player a card
    #
    def givePlayerCard(self):
         card = self.dealCard()

         #Counts how many aces the player has
         if card == 11:
             self.player.numberOfAces += 1

         self.player.playerCards.append(card)

    #
    # Give the dealer a card
    #
    def giveDealerCard(self):
        card = self.dealCard()

        #Counts how many aces the dealer has
        if card == 11:
            self.dealer.numberOfAces += 1

        self.dealer.dealerCards.append(card)

    #
    # The player's turn
    #
    def playerTurn(self):
        # While the player hits the code block needs to run
        while True:
            #If the player is bust then the current hand stops and the dealer wins
            if self.checkIfBust(self.player):
                self.winner.decideWinner(self.player, self.dealer)
                return

            #Displays the player's cards as well as the dealer's cards.

            #The player is prompted to hit or stand
            playerDecision = self.getPlayerDecision().upper()

            #If the player has chosen to hit than they are given another card
            #If the player has chosen to stand then the game continues on with the dealer's turn
            match playerDecision:
                case "H":
                    self.givePlayerCard()
                case "S":
                    self.dealerTurn
                    return
                case "P":
                    self.player.playerCards = self.Splitting.splitHand(self.player.playerCards)
                    print(f"Your Cards: {self.player.playerCards}")
                    print(f"Dealer Cards: {self.dealer.dealerCards}")  
    #
    # Prompts the user for a decision to hit or stand
    #
    def getPlayerDecision(self):
        #Escapes when the player has decided to hit or stand
        while True:
            #Shows the player their total
            print(f"Your total is {self.player.total}")
            #Prompts to player to hit or stand
            print("H or S")
            playerDecision = input()    
            #Escapes the loop if the player has chosen to hit or stand
            if playerDecision in ["H", "S", "P"]:
                return playerDecision


    def dealerTurn(self):
        #While the dealer has less than 17 it hits
        while self.dealer.total < 17:
            self.giveDealerCard()

            #Checks if the dealer is buts, passing the current dealer object
            self.checkIfBust(self.dealer)

        # Check who won between the dealer and the player, passing the current dealer and current player's objects
        self.winner.decideWinner(self.player, self.dealer)
