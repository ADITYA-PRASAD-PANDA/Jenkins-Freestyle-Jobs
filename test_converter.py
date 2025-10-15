import unittest
from converter import c_to_f, f_to_c

class TestConverter(unittest.TestCase):
    def test_c_to_f(self):
        self.assertEqual(c_to_f(0), 32)
        self.assertEqual(c_to_f(100), 212)

    def test_f_to_c(self):
        self.assertAlmostEqual(f_to_c(32), 0)
        self.assertAlmostEqual(f_to_c(212), 100)

if __name__ == "__main__":
    unittest.main()
