# Security-engineering | Vulnerable API 

This API demonstrates intentional vulnerabilities based on the OWASP API's:
- **Unrestricted Resource Consumption**: `/store` endpoint accepts unlimited data without validation.
- **Server-Side Request Forgery (SSRF)**: `/ssrf` endpoint allows fetching attacker-controlled URLs.
- **Security Misconfiguration**: Debug mode enabled, server exposed to public access.
- **Unsafe Consumption of APIs**: `/fetch` endpoint consumes external APIs without validation.

## Requirements

- Python 3.8 or above
- `Flask` library
- `requests` library

## Setup Instructions

1. Clone or download the repository.
2. Navigate to the project directory.
3. Install dependencies:
   ```bash
   pip install flask requests

Start the API server:
python app.py

In a new terminal navigate to script\vdemo.py ->
run: python vdemo.py

1. Unrestricted Resource Consumption
Endpoint: /store
debug:
"127.0.0.1 - - [17/Nov/2024 17:30:25] "POST /ssrf HTTP/1.1" 500 -"


3. Server-Side Request Forgery (SSRF)
Endpoint: /ssrf

127.0.0.1 - - [17/Nov/2024 17:30:25] "POST /ssrf HTTP/1.1" 500 -

3. Security Misconfiguration
Endpoint: /store
debug:
127.0.0.1 - - [17/Nov/2024 17:30:29] "POST /fetch HTTP/1.1" 500 -


4. Unsafe Consumption of APIs
Endpoint: /fetch
debug:
This is an example of Security Misconfiguration, as debug mode exposes sensitive server information such as:
File paths (e.g., D:\Anaconda\Lib\site-packages\requests)
