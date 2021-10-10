import random
from game import director

# The class constructor
# Define deal cards, get points, can deal, init


class Dealer:
    def __init__(self):
        self.current_cards = []
        self.score = 300

    def deal_cards(self):
        card1 = random.randint(1, 13)
        card2 = random.randint(1, 13)
        self.current_cards = [card1, card2]
        print(f'The Card Is: {self.current_cards[0]}')
        self.guess = input('Higher or lower?(h/l) ')
        print(f'Next Card was: {self.current_cards[1]}')

    def get_points(self):
        """Calulate the points earned for an individual guess.
        Correct = +100
        Incorrect = -100
        Author: Mitchell Ball
        """
        if self.guess == 'h' and self.current_cards[0] < self.current_cards[1]:
            self.score += 100

        elif self.guess == 'l' and self.current_cards[0] > self.current_cards[1]:
            self.score += 100

        elif self.guess == 'h' and self.current_cards[0] > self.current_cards[1]:
            self.score -= 75
        
        elif self.guess == 'l' and self.current_cards[0] < self.current_cards[1]:
            self.score -= 75

        return self.score

    def can_deal(self):
        # Checks to see if the player has lost the game
        # and if they wish to continue
        # Is to be used in an IF statement
        if self.score > 0:
            return True
        else:
            return False
