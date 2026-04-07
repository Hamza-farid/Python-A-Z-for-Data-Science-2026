# =========================
# Section 1: Import Modules
# =========================
import requests
import time

# =========================
# Section 2: API Request
# =========================
url = "https://jsonplaceholder.typicode.com/todos/1"

try:
    # Make a GET request to the API
    response = requests.get(url)
    
    # =========================
    # Section 3: Status Code Handling
    # =========================
    print("Status Code:", response.status_code)
    
    # Check for successful response
    if response.status_code == 200:
        # =========================
        # Section 4: Parse JSON Response
        # =========================
        data = response.json()
        print("Full JSON Response:", data)
        print("ID Field:", data['id'])
    else:
        print("Failed to fetch data. Status code:", response.status_code)
        
        # =========================
        # Section 5: Rate Limiting Example
        # =========================
        # Many APIs return 429 for too many requests
        if response.status_code == 429:
            print("Rate limit exceeded. Waiting before retrying...")
            # Wait and retry logic (simple example)
            time.sleep(5)
            # You would typically retry the request here

except requests.exceptions.RequestException as e:
    # =========================
    # Section 6: Error Handling
    # =========================
    print("An error occurred:", e)

# =========================
# Section 7: API Challenges (Interview Notes)
# =========================
"""
Common API Challenges:
1. Rate Limiting:
   - APIs may restrict the number of requests per minute/hour (HTTP 429).
   - Solution: Implement retry logic with exponential backoff.

2. Authentication:
   - Many APIs require API keys or OAuth tokens.
   - Always keep credentials secure.

3. Error Handling:
   - Handle network errors, timeouts, and unexpected responses.
   - Use try-except blocks and check status codes.

4. Data Validation:
   - Always validate and sanitize API responses before using.

5. Pagination:
   - Some APIs return data in pages; handle pagination to get all results.

6. Throttling and Backoff:
   - Respect server limits; use time.sleep() or backoff libraries.

7. Security:
   - Use HTTPS, validate SSL certificates, and avoid exposing sensitive data.

8. Logging and Monitoring:
   - Log requests and responses for debugging and monitoring.

9. Timeout Handling:
   - Set timeouts for requests to avoid hanging indefinitely.
     Example: requests.get(url, timeout=5)
"""