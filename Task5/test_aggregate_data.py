import unittest
from typing import List, Dict
from task_5_aggregate_data import aggregate_data, sum_values

class TestAggregateData(unittest.TestCase):
    
    def setUp(self):
        # Sample data that will be used in tests
        self.data = [
            {'category': 'A', 'value': 10},
            {'category': 'B', 'value': 20},
            {'category': 'A', 'value': 15},
            {'category': 'B', 'value': 25},
            {'category': 'C', 'value': 30}
        ]

    def test_aggregate_by_category_with_sum(self):
        # Test aggregate_data by category and sum the values
        expected_result = {'A': 25, 'B': 45, 'C': 30}
        result = aggregate_data(self.data, 'category', sum_values)
        self.assertEqual(result, expected_result)

    def test_aggregate_with_empty_data(self):
        # Test with empty data
        result = aggregate_data([], 'category', sum_values)
        self.assertEqual(result, {})

    def test_aggregate_with_missing_key(self):
        # Test when some dictionaries do not contain the key
        data_with_missing_key = [
            {'category': 'A', 'value': 10},
            {'category': 'B', 'value': 20},
            {'value': 15}  # Missing 'category' key
        ]
        expected_result = {'A': 10, 'B': 20}
        result = aggregate_data(data_with_missing_key, 'category', sum_values)
        self.assertEqual(result, expected_result)

    def test_aggregate_with_different_aggregator(self):
        # Test with a different aggregator (e.g., count of items)
        def count_items(items: List[Dict]) -> int:
            return len(list(items))

        expected_result = {'A': 2, 'B': 2, 'C': 1}
        result = aggregate_data(self.data, 'category', count_items)
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()
