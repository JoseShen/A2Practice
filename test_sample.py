import unittest
from sample import foo

class TestFoo(unittest.TestCase):

  def test_foo(self):
    self.assertEqual(foo(1), 3)
    self.assertEqual(foo(2), 4)
    self.assertEqual(foo(3), 5)

if __name__ == "__main__":
  unittest.main()
