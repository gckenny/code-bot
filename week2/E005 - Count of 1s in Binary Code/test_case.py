import unittest 


# Fake, just for pass IDE
def solution(bcode: str) -> int:
    pass


class E005(unittest.TestCase):
    def test_simple1(self):
        self.assertEqual(solution("00000000"), 0)

    def test_simple2(self):
        self.assertEqual(solution("11111111"), 8)

    def test_simple3(self):
        self.assertEqual(solution("10000100"), 2)

    def test_simple4(self):
        self.assertEqual(solution("00100011"), 3)

    def test_simple5(self):
        self.assertEqual(solution("10011101"), 5)

    def test_simple6(self):
        self.assertEqual(solution("10110100"), 4)

    def test_simple7(self):
        self.assertEqual(solution("10110101"), 5)

    def test_simple8(self):
        self.assertEqual(solution("10110110"), 5)

    def test_simple9(self):
        self.assertEqual(solution("10100100"), 3)

    def test_simple10(self):
        self.assertEqual(solution("10010100"), 3)

    def test_simple11(self):
        self.assertEqual(solution("10110111"), 6)

    def test_simple12(self):
        self.assertEqual(solution("11110111"), 7)

