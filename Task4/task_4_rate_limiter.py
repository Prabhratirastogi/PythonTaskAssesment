import time
from collections import defaultdict
from threading import Lock

class RateLimiter:
    def __init__(self, max_requests=5, time_window=60):
        self.max_requests = max_requests  # Max requests allowed
        self.time_window = time_window    # Time window in seconds
        self.user_requests = defaultdict(list)  # Store requests for each user
        self.lock = Lock()  # Lock for thread safety

    def allow_request(self, user_id):
        with self.lock:
            current_time = time.time()
            # Clean up old requests
            self.user_requests[user_id] = [
                request_time for request_time in self.user_requests[user_id]
                if current_time - request_time < self.time_window
            ]
            
            if len(self.user_requests[user_id]) < self.max_requests:
                # Add the current request time
                self.user_requests[user_id].append(current_time)
                return True  # Request is allowed
            else:
                return False  # Request limit reached

# Example Usage
if __name__ == "__main__":
    rate_limiter = RateLimiter()

    user_id = "user1"
    for _ in range(7):  # Test 7 requests
        if rate_limiter.allow_request(user_id):
            print("Request allowed")
        else:
            print("Request denied")
        time.sleep(10)  # Wait 10 seconds between requests


# Output 
'''Request allowed
Request allowed
Request allowed
Request allowed
Request allowed
Request denied
Request denied'''
