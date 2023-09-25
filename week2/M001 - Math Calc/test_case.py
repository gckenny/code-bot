import unittest 


# Fake, just for pass IDE
def solution(money: list[int], m: int) -> int:
    pass


class M001(unittest.TestCase):
    def test_simple1(self):
        self.assertEqual(solution([7, 5, 3, 3, 2, 1], 112), 216)

    def test_simple2(self):
        self.assertEqual(solution([6, 5, 4, 3, 2, 1], 24), 26)

    def test_simple3(self):
        self.assertEqual(solution([5, 3, 3, 1, 1, 1], 43), 21)

    def test_simple4(self):
        self.assertEqual(solution([10, 5, 5, 2, 2, 1], 30), 101)

    def test_simple5(self):
        self.assertEqual(solution([6, 5, 4, 0, 0, 0], 100), -1)

    def test_simple6(self):
        self.assertEqual(solution([1, 1, 1, 1, 1, 1], 83), -1)

