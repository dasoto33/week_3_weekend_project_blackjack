# create a simplified version of the Blackjack game using Python, focusing on object-oriented programming concepts.

# Rules:

# The game will involve two players: the Dealer and the Player. At the start of the game, there will be a deck of 
# 52 cards, divided into four suits: Clubs, Diamonds, Hearts, and Spades. Each suit will contain cards numbered 
# 1 through 13 (Ace to King).

# Note: There will be no wildcards used in this game.

# The game begins with the Dealer shuffling the deck of cards to randomize them. After shuffling, the Dealer 
# deals two cards to the Player and two cards to itself. The Player can see both of their own cards, but can 
# only see one of the Dealer’s cards.

# The objective of the game is for the Player to evaluate the value of their cards. If the Player is 
# unsatisfied with their hand, they have the option to ‘Hit,’ which means requesting an additional card 
# from the Dealer. The Player can hit as many times as they want, as long as they don’t go over a total of 21, 
# resulting in a ‘Bust.’

# If the Player is dealt cards totaling 21 on the first deal, it is considered a ‘Blackjack’ and the 
# Player wins. It’s important to note that Blackjack can only be attained on the first deal.

# The Player cannot see the Dealer’s complete hand until they choose to ‘Stand.’ Standing means the 
# Player decides not to receive any more cards from the Dealer. Once the Player stands, the Player’s 
# and the Dealer’s hands are compared. The hand with the higher total wins. Remember that the Dealer can also 
# bust by going over 21.

import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return f'(self.rank) of (self.suit)'

class Deck:
    def __init__(self):
        suits = ['Clubs', 'Diamonds', 'Spades', 'Hearts']
        ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]
        random.shuffle(self.cards)

    def deal_card(self):
        return self.crds.pop()

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
            value -= 1

        return value

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()

    def add_card_to_hand(self, card):
        self.hand.add_card(card)

    def get_hand_value(self):
        return self.hand.get_value()

class Game:
    def __init__(self):
        self.deck = Deck()
        self.player = Player('Player')
        self.dealer = Player('Dealer')

    def start_game(self):
        print('You have entered the world of Blackjack! Good luck!')
        self.player.add_card_to_hand(self.deck.deal_card)()
        self.player.add_card_to_hand(self.deck.deal_card)()
        self.dealer.add_card_to_hand(self.deck.deal_card)()
        self.dealer.add_card_to_hand(self.deck.deal_card)()

        self.show_hands()

        if self.player.get_hand_value() == 21:
            print('Blackjack! Congratulations, you win! Go buy yourself something nice!')
        else:
            self.player_turn()
    
    def show_hands(self, show_all = False):
        print('\nPlayer Hand: ')
        for card in self.player.hand.cards:
            print(card)
        print('\nDealer Hand: ')
        if show_all:
            for card in self.dealer.hand.cards:
                print(card)
        else: print(self.dealer.hand.cards[0])

    def player_turn(self):
        while True:
            choice = input('\nWould you like to Hit or Stand? (H/S)')
            if choice == 'H':
                self.player.add_card_to_hand(self.deck.deal_card())
                self.show_hands()
                
        



def main():
    game = Game()
    while True:
        game.start_game()