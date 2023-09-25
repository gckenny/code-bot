import unittest 


# Fake, just for pass IDE
def solution(s: str) -> str:
    pass


class E003(unittest.TestCase):
    def test_simple1(self):
        self.assertEqual(solution("Good3Bye"), "GoodGoodGood")

    def test_simple2(self):
        self.assertEqual(solution("abc11db0bm3ee3"), "abcabcabcabcabcabcabcabcabcabcabcbmbmbmeeeeee")

    def test_simple3(self):
        self.assertEqual(solution("13baa3b4"), "baabaabaabbbb")

    def test_simple4(self):
        self.assertEqual(solution("t3t4t5"), "tttttttttttt")

    def test_simple5(self):
        self.assertEqual(solution("A0010B00B010"), "AAAAAAAAAABBBBBBBBBB")

