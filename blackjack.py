import random

# Card Class:
# need two attributes suit and rank
# use str method to represent cards

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

# Deck Class:
# create instances of card class for rank/suit combination
# create method to pop card from deck and return a new one
# import random to be able to shuffle cards

class Deck:
    def __init__(self):
        suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

# Hand Class:
# create method to add card to hand (use .append)
# create method to get the value of hand by assigning values to each card type

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        value = 0
        num_aces = 0
        for card in self.cards:
            if card.rank == 'Ace':
                value += 11
                num_aces += 1
            elif card.rank in ['King', 'Queen', 'Jack']:
                value += 10
            else:
                value += int(card.rank)
        
        while value > 21 and num_aces > 0:
            value -= 10
            num_aces -= 1

        return value

# Player Class:
# create method to store their hand
# create method to get the value of their hand

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()

    def add_card_to_hand(self, card):
        self.hand.add_card(card)

    def get_hand_value(self):
        return self.hand.get_value()

# Main/Game Class:

class Game:
    def __init__(self):
        self.deck = Deck()
        self.player = Player("Player")
        self.dealer = Player("Dealer")

# create method to reset everyone's cards when new game is started
    def reset_game(self):
        self.deck = Deck()
        self.player = Player("Player")
        self.dealer = Player("Dealer")

# create method to to begin the game
# each player is dealt two cards
# if player hand value is 21, player wins, if not, then both players are shown their hand
# two cards for player and one for dealer

    def start_game(self):
        print("Welcome to the World of Blackjack!")
        self.reset_game()
        self.player.add_card_to_hand(self.deck.deal_card())
        self.player.add_card_to_hand(self.deck.deal_card())
        self.dealer.add_card_to_hand(self.deck.deal_card())
        self.dealer.add_card_to_hand(self.deck.deal_card())

        self.show_hands()

        if self.player.get_hand_value() == 21:
            print("Blackjack! You win, 21 Savage!")
        else:
            self.player_turn()

    def show_hands(self, show_all=False):
        print("\nPlayer's Hand:")
        for card in self.player.hand.cards:
            print(card)

        print("\nDealer's Hand:")
        if show_all:
            for card in self.dealer.hand.cards:
                print(card)
        else:
            print(self.dealer.hand.cards[0])

# create method for the players turn
# needs an input for hit or stand, shouldn't matter what casing the word is (use .lower)
# if their hand value is more than 21, they bust/lose
# if they pick 's' to stand, it is now the dealers turn (new method)

    def player_turn(self):
        while True:
            choice = input("\nDo you want to Hit or Stand? (H/S): ").lower()
            if choice == 'h':
                self.player.add_card_to_hand(self.deck.deal_card())
                self.show_hands()
                if self.player.get_hand_value() > 21:
                    print("Bustaroni! You lose!")
                    break
            elif choice == 's':
                self.dealer_turn()
                break
            else:
                print("Invalid input. Please enter 'H' to Hit or 'S' to Stand.")

# create method for the dealer's turn
# dealers card can now be seen
# display each card after it is shown and show values
# if the dealer's hand value is more than 21, they lose/player wins
# if dealer's hand value equals player's hand value, tie
# if dealer's hand is more than the player's hand value, dealer wins

    def dealer_turn(self):
        self.show_hands(show_all=True)
        while self.dealer.get_hand_value() < 17:
            self.dealer.add_card_to_hand(self.deck.deal_card())
            self.show_hands(show_all=True)

        player_value = self.player.get_hand_value()
        dealer_value = self.dealer.get_hand_value()

        if dealer_value > 21:
            print("Dealer busts! You win!")
        elif dealer_value == player_value:
            print("It's a tie!")
        elif dealer_value > player_value:
            print("Oof, Dealer wins! Play again to redeem yourself!")
        else:
            print("Congrats! You win! Keep the win streak and play again!")

# create method to give player option to play again
# requires input (y/n)

    def play_again(self):
        choice = input("\nWould you like to play again? (Y/N): ").lower()
        if choice == "y":
            return choice
        if choice == "n":
            quit()
        else:
            print("Invalid input. Please enter 'Y' to play again or 'N' to quit.")

def main():
    game = Game()
    while True:
        game.start_game()
        if not game.play_again():
            break

if __name__ == '__main__':
    main()