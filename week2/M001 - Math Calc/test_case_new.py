import unittest 


# Fake, just for pass IDE
def fake_solution(money: list[int], m: int) -> int:
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

def solution(money, m):
    memo = {}
    def helper(amount, idx):
        if amount == 0:
            return 0
        if idx == len(money):
            return -1
        if (amount, idx) in memo:
            return memo[(amount, idx)]
        max_count = amount // money[idx]
        min_count = float('inf')
        for count in range(max_count, -1, -1):
            remaining = amount - count * money[idx]
            if remaining == 0:
                memo[(amount, idx)] = count
                return count
            res = helper(remaining, idx + 1)
            if res != -1:
                min_count = min(min_count, count + res)
        memo[(amount, idx)] = min_count if min_count != float('inf') else -1
        return memo[(amount, idx)]
    return helper(m, 0)

if __name__ == '__main__':
    unittest.main()
