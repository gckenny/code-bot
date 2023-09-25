import unittest 


# Fake, just for pass IDE
def solution(n: int, broken: list[int]) -> int:
    pass


class M007(unittest.TestCase):
    def test_simple1(self):
        self.assertEqual(solution(10, [2, 5]), 5)

    def test_simple2(self):
        self.assertEqual(solution(6, [1, 5]), 2)

    def test_simple3(self):
        self.assertEqual(solution(10, [3, 4]), 0)

    def test_simple4(self):
        self.assertEqual(solution(10, [10]), 0)

    def test_simple5(self):
        self.assertEqual(solution(20, [3, 10, 16]), 240)

    def test_simple6(self):
        self.assertEqual(solution(10, [2, 4, 8]), 2)

    def test_simple7(self):
        self.assertEqual(solution(10, [2, 5, 8]), 1)

    def test_simple8(self):
        self.assertEqual(solution(20, [4, 8, 12]), 252)

    def test_simple9(self):
        self.assertEqual(solution(40, [10, 20, 30]), 3496900)

    def test_simple10(self):
        self.assertEqual(solution(45, [1]), 701408733)

    def test_simple11(self):
        self.assertEqual(solution(20, [2, 5, 14, 19]), 63)

