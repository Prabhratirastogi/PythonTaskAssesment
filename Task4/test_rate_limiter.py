import time
import unittest
from task_4_rate_limiter import RateLimiter  # Adjust the import based on your file structure

class TestRateLimiter(unittest.TestCase):
    
    def setUp(self):
        self.rate_limiter = RateLimiter(max_requests=5, time_window=60)
        self.user_id = "user1"

    def test_allow_request_within_limit(self):
        # Test allowing requests within the limit
        for _ in range(5):
            self.assertTrue(self.rate_limiter.allow_request(self.user_id))

    def test_deny_request_exceeding_limit(self):
        # Allow 5 requests
        for _ in range(5):
            self.rate_limiter.allow_request(self.user_id)
        
        # Deny the 6th request
        self.assertFalse(self.rate_limiter.allow_request(self.user_id))

    def test_requests_reset_after_time_window(self):
        # Allow 5 requests
        for _ in range(5):
            self.rate_limiter.allow_request(self.user_id)
        
        # Deny the 6th request
        self.assertFalse(self.rate_limiter.allow_request(self.user_id))
        
        # Wait for the time window to reset
        time.sleep(60)  # This should match your time_window
        
        # Now, we should be able to make requests again
        for _ in range(5):
            self.assertTrue(self.rate_limiter.allow_request(self.user_id))

if __name__ == "__main__":
    unittest.main()
