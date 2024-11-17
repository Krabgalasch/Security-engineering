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

In a new terminal navigate to script\vdemo.py -><br>
run: python vdemo.py<br>

1. Unrestricted Resource Consumption<br>
Endpoint: /store<br>
debug:<br>
"127.0.0.1 - - [17/Nov/2024 17:30:25] "POST /ssrf HTTP/1.1" 500 -"<br>
This shows the vulnerability of Unrestricted Resource Consumption, as data is being stored without any checks or limits.

2. Server-Side Request Forgery (SSRF)<br>
Endpoint: /ssrf<br>
debug:<br>
127.0.0.1 - - [17/Nov/2024 17:30:25] "POST /ssrf HTTP/1.1" 500 -<br>
This confirms that the server is making requests to user-supplied URLs, proving the SSRF vulnerability exists.


3. Security Misconfiguration<br>
Endpoint: /store<br>
debug:<br>
127.0.0.1 - - [17/Nov/2024 17:30:29] "POST /fetch HTTP/1.1" 500 -<br>
The vulnerability of Unsafe Consumption of APIs is evident, as no checks are in place for the external URL or its content2

4. Unsafe Consumption of APIs<br>
Endpoint: /fetch<br>
debug:<br>
This is an example of Security Misconfiguration, as debug mode exposes sensitive server information such as:<br>
File paths (e.g., D:\Anaconda\Lib\site-packages\requests)
