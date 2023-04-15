import unittest
from unittest import result
import chess

class Test_Chess(unittest.TestCase):
    def test_pow(self):
        self.assertEqual(chess.pow(2,64),18446744073709551615)


if __name__ == '__main__':
    unittest.main()