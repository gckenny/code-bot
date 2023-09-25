import unittest 


# Fake, just for pass IDE
def fake_solution(s:str) -> int:
    pass


class H001(unittest.TestCase):
    def test_simple1(self):
        self.assertEqual(solution("ldsfaiuerlkjdsaflkcareajlkuiow.adsfkl&^*"), 102)

    def test_simple2(self):
        self.assertEqual(solution("890324578ifaj,k,jfasdjkjuieraskjuierwjkuser"), 115)

    def test_simple3(self):
        self.assertEqual(solution("xxkdafkuioerwqhjkhasdflladfccuiew314985342983452asfmnmnasfd"), 172)

    def test_simple4(self):
        self.assertEqual(solution("13413241324kxxxxxxxkjkkasfdjk89031247901324"), 98)

    def test_simple5(self):
        self.assertEqual(solution("aaaaaccccbbbbbaaacc"), 19)

def solution(s:str) -> int:
    # Step 1: Create frequency table
    freq_table = {}
    for char in s:
        if char in freq_table:
            freq_table[char] += 1
        else:
            freq_table[char] = 1

    # Step 2: Build ternary tree
    tree = {}
    for char, freq in freq_table.items():
        tree[char] = freq

    while len(tree) > 1:
        min1 = min(tree, key=tree.get)
        freq1 = tree.pop(min1)
        min2 = min(tree, key=tree.get)
        freq2 = tree.pop(min2)

        new_char = min1 + min2
        new_freq = freq1 + freq2
        tree[new_char] = new_freq

    # Step 3: Generate ternary codes
    ternary_codes = {}
    def generate_codes(node, code):
        if len(node) == 1:
            ternary_codes[node] = code
        else:
            generate_codes(node[0], code + '0')
            generate_codes(node[1], code + '1')
            generate_codes(node[2], code + '2')

    generate_codes(list(tree.keys())[0], '')

    # Step 4: Calculate total ternary digits
    total_digits = 0
    for char in s:
        total_digits += len(ternary_codes[char])

    return total_digits

if __name__ == '__main__':
    unittest.main()
