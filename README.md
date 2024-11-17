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
Sends large payloads repeatedly without validation or limits.

2. Server-Side Request Forgery (SSRF)
Endpoint: /ssrf
Exploits the API by making requests to attacker-supplied URLs.

3. Security Misconfiguration
Endpoint: /store
Triggers debug mode stack traces using invalid payloads.

4. Unsafe Consumption of APIs
Endpoint: /fetch
Provides a URL to the API, which fetches data without validation.
