# Floyd’s Tortoise and Hare algorithm

'''
One of the best and most optimized ways to solve the problem in terms of both time and space complexity. Here's why:

Optimal Approach: Floyd’s Tortoise and Hare Algorithm
Time Complexity: O(n) — The slow and fast pointers traverse the array in linear time.
Space Complexity: O(1) — No extra space is used, as the algorithm only uses a few pointers.
'''

def find_duplicate(nums):
    # Edge case: Handle empty list or list with no duplicate
    if not nums or len(nums) == 1:
        return None  # No duplicate possible in empty or single-element list

    # Initialize slow and fast pointers
    slow_ptr = nums[0]
    fast_ptr = nums[0]

    # Phase 1: Move slow pointer by 1 step and fast pointer by 2 steps until they meet
    while True:
        slow_ptr = nums[slow_ptr]
        fast_ptr = nums[nums[fast_ptr]]
        if slow_ptr == fast_ptr:
            break

    # Phase 2: Reset fast pointer to start and move both pointers by 1 step until they meet
    fast_ptr = nums[0]
    while slow_ptr != fast_ptr:
        slow_ptr = nums[slow_ptr]
        fast_ptr = nums[fast_ptr]

    # The meeting point is the duplicate number
    return slow_ptr

# Example usage
if __name__ == "__main__":
    # You can call the function directly with a predefined list for testing
    nums = [1, 3, 4, 2, 2]  # Example input
    duplicate = find_duplicate(nums)
    if duplicate:
        print(f"The duplicate number is: {duplicate}")
    else:
        print("No duplicate found or invalid input.")
