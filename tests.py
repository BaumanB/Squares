import unittest
from source.screen import Screen

class TestSquares(unittest.TestCase):

    def test_find_next_square(self):
        screen = Screen(10, 15)
        self.assertEqual(screen.find_next_square(), True, 'find_next_square NOT OK')
        self.assertEqual(screen.squares[10], 1, 'got a wrong square')
        self.assertEqual(screen.height, 10, 'height should be left intact')
        self.assertEqual(screen.width, 15, 'width should be left intact')

    def test_find_all_squares(self):
        screen1 = Screen(10, 15)
        screen1.find_all_squares()
        self.assertEqual(screen1.squares[10], 1, 'got wrong squares')
        self.assertEqual(screen1.squares[5], 2, 'got wrong squares')
        self.assertEqual(len(screen1.squares), 2, 'got wrong squares')
        self.assertEqual(screen1.num_of_squares, 3, 'got wrong squares')
        self.assertEqual(screen1.height, 10, 'height should be left intact')
        self.assertEqual(screen1.width, 15, 'width should be left intact')

        screen2 = Screen(11, 15)
        screen2.find_all_squares()
        self.assertEqual(screen2.squares[11], 1, 'got wrong squares')
        self.assertEqual(screen2.squares[4], 2, 'got wrong squares')
        self.assertEqual(screen2.squares[3], 1, 'got wrong squares')
        self.assertEqual(screen2.squares[1], 3, 'got wrong squares')
        self.assertEqual(len(screen2.squares), 4, 'got wrong squares')
        self.assertEqual(screen2.num_of_squares, 7, 'got wrong squares')
        self.assertEqual(screen2.height, 11, 'height should be left intact')
        self.assertEqual(screen2.width, 15, 'width should be left intact')

    def test_initialization(self):
        screen = Screen(0,1)
        self.assertIsNone(screen, 'height initialization not ok')
        screen = Screen(1,0)
        self.assertIsNone(screen, 'width initialization not ok')
        screen = Screen(1,1)
        self.assertIsNotNone(screen, 'width initialization not ok')


if __name__ == '__main__':
    unittest.main()
