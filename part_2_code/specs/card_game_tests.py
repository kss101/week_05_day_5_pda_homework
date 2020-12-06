import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.card_1 = Card("hearts", 1)
        self.card_2 = Card("clubs", 9)

        self.game = CardGame()

    def test_check_for_ace(self):
        self.assertEqual(True, self.game.check_for_ace(self.card_1))

    def test_check_for_ace_false(self):
        self.assertEqual(False, self.game.check_for_ace(self.card_2))

    def test_highest_card_first_card(self):
        self.assertEqual(self.card_2, self.game.highest_card(self.card_2, self.card_1))

    def test_highest_card_second_card(self):
        self.assertEqual(self.card_2, self.game.highest_card(self.card_1, self.card_2))

    def test_cards_total(self):
        self.card_3 = Card("spades", 7)
        self.cards = [ self.card_1, self.card_2, self.card_3]
        self.assertEqual("You have a total of 17", self.game.cards_total(self.cards))
