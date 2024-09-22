import unittest
from task_6_find_duplicate import find_duplicate  # Adjust the import based on your file structure

class TestFindDuplicate(unittest.TestCase):

    def test_duplicate_in_middle(self):
        nums = [1, 3, 4, 2, 2]
        result = find_duplicate(nums)
        self.assertEqual(result, 2)

    def test_duplicate_at_end(self):
        nums = [3, 1, 3, 4, 2]
        result = find_duplicate(nums)
        self.assertEqual(result, 3)

    def test_duplicate_at_start(self):
        nums = [1, 1, 2]
        result = find_duplicate(nums)
        self.assertEqual(result, 1)

    def test_large_input(self):
        nums = [1] + [2] * 10000 + [3]  # Duplicate is 2
        result = find_duplicate(nums)
        self.assertEqual(result, 2)

    def test_no_duplicate(self):
        nums = [1, 2, 3, 4]  # This should raise an error as there is no duplicate
        with self.assertRaises(IndexError):  # Expecting an IndexError
            find_duplicate(nums)

if __name__ == "__main__":
    unittest.main()
