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
