"""
Simple Password Checker - Generates metrics continuously
"""

import requests
import random
import time
import os

# Passwords to test
WEAK_PASSWORDS = ["password123", "123456", "qwerty", "admin123", "letmein"]
STRONG_PASSWORDS = ["X9$mK2@pL7&nQ4!vT8", "P@ssw0rd!2024#Secure", "My$uper$tr0ng!Pass"]

def check_passwords():
    """Continuously check passwords to generate metrics."""
    
    # Configuration from environment variables
    url = os.getenv("API_URL", "http://127.0.0.1:44805/pwned/check-password")
    session_cookie = os.getenv("SESSION_COOKIE", "")
    interval = int(os.getenv("INTERVAL", "3"))  # seconds between requests
    weak_ratio = float(os.getenv("WEAK_RATIO", "0.7"))  # 70% weak passwords
    
    print(f"⚡ DarkSignal Metric Generator")
    print(f"Target: {url}")
    print(f"Interval: {interval}s")
    print(f"Starting...\n")
    
    session = requests.Session()
    if session_cookie:
        session.cookies.set('session', session_cookie)
    
    count = 0
    while True:
        try:
            # Pick password
            if random.random() < weak_ratio:
                password = random.choice(WEAK_PASSWORDS)
            else:
                password = random.choice(STRONG_PASSWORDS)
            
            # Send request
            response = session.post(url, data={"password": password}, timeout=10)
            count += 1
            
            if response.status_code == 200:
                result = response.json()
                if "warning" in result:
                    print(f"[{count}] 🔴 PWNED - {result.get('count', 0)} times")
                else:
                    print(f"[{count}] ✅ SAFE")
            else:
                print(f"[{count}] ⚠️  Status: {response.status_code}")
            
        except Exception as e:
            print(f"[{count}] ❌ Error: {e}")
        
        time.sleep(interval)

if __name__ == "__main__":
    check_passwords()