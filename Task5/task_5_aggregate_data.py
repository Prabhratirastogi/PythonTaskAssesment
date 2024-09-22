from typing import List, Dict, Callable
from collections import defaultdict

def aggregate_data(data: List[Dict], key: str, aggregator: Callable) -> Dict:
    aggregated_result = defaultdict(list)

    # Group the dictionaries by the specified key
    for item in data:
        if key in item:
            aggregated_result[item[key]].append(item)

    # Apply the aggregator function to the grouped values
    result = {}
    for group_key, items in aggregated_result.items():
        # Aggregate the values based on the aggregator function
        result[group_key] = aggregator(items)  # Use items directly

    return result

# Example aggregator function
def sum_values(items: List[Dict]) -> float:
    return sum(item['value'] for item in items)

# Example usage
if __name__ == "__main__":
    data = [
        {'category': 'A', 'value': 10},
        {'category': 'B', 'value': 20},
        {'category': 'A', 'value': 15},
        {'category': 'B', 'value': 25},
        {'category': 'C', 'value': 30}
    ]

    aggregated_data_result = aggregate_data(data, 'category', sum_values)
    print(aggregated_data_result)  # Output should be {'A': 25, 'B': 45, 'C': 30}



# OutPut Should be {'A': 25, 'B': 45, 'C': 30}