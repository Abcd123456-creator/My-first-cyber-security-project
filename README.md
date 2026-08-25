# --- STEP 1: The List of Banned Common Passwords ---
# Real hackers use lists like this to guess passwords instantly!
banned_passwords = ["123456", "password", "123456789", "qwerty", "letmein123"]

print("--- Welcome to Python Password Security Guard (Advanced) ---")

# --- STEP 2: Ask the user to type a password ---
user_password = input("Please enter a password to test: ")

# --- STEP 3: Check if the password is too common ---
if user_password in banned_passwords:
    print("❌ SECURITY ALERT: This password is way too common! Hackers will guess it instantly.")
else:
    print("✅ Clear: This password is not on the common blocklist.")
import urllib.request  # This built-in Python tool lets us fetch data from the internet

print("--- Welcome to Python Password Security Guard (Advanced v2.0) ---")
print("Loading real-world threat intelligence blocklist... Please wait...")

try:
    # This URL holds a famous list of the 1,000 most common hacked passwords
    url = "https://githubusercontent.com"
    
    # Python goes to the internet, grabs the text, and splits it into a list of words
    response = urllib.request.urlopen(url)
    common_passwords = response.read().decode('utf-8').splitlines()
    print("✅ Blocklist successfully loaded!\n")

except Exception as e:
    # If your internet is off, the program will use this emergency backup list
    print("⚠️ Could not connect to internet. Using offline backup list.")
    common_passwords = ["123456", "password", "123456789", "qwerty", "letmein123"]

# --- ASK USER FOR INPUT ---
user_password = input("Enter a password to scan for security risks: ")

# --- ADVANCED SECURITY CHECKS ---

# Check 1: Is it too short?
if len(user_password) < 8:
    print("❌ RISK DETECTED: Password must be at least 8 characters long.")

# Check 2: Is it on the real hacker blocklist?
elif user_password.lower() in common_passwords:
    print("❌ CRITICAL RISK: This password is in the Top 1,000 most breached passwords globally! Hackers can crack this in milliseconds.")

# Check 3: Is it safe?
else:
    print("💎 SUCCESS: This password passed the length check and is not on the common hacker blocklist!")
import urllib.request  # This built-in Python tool lets us download data from the internet

print("--- Welcome to Python Password Security Guard (Advanced v2.0) ---")
print("Loading real-world threat intelligence blocklist... Please wait...")

try:
    # This URL connects to a famous database of the 1,000 most common passwords leaked in real data breaches
    url = "https://githubusercontent.com"
    
    # Python goes to the internet, grabs the text file, and turns it into a giant list of words
    response = urllib.request.urlopen(url)
    common_passwords = response.read().decode('utf-8').splitlines()
    print("✅ Real-world threat list successfully loaded!\n")

except Exception as e:
    # If your internet disconnects, this backup list will keep the program running safely
    print("⚠️ Could not connect to internet. Using offline backup list.")
    common_passwords = ["123456", "password", "123456789", "qwerty", "letmein123"]

# --- ASK USER FOR INPUT ---
user_password = input("Enter a password to scan for security risks: ")

# --- ADVANCED SECURITY CHECKS ---

# Check 1: Length Check
if len(user_password) < 8:
    print("❌ RISK DETECTED: Password must be at least 8 characters long.")

# Check 2: The Real Hacker Blocklist Check
# This looks through all 1,000 leaked passwords instantly!
elif user_password.lower() in common_passwords:
    print("❌ CRITICAL RISK: This password is in the Top 1,000 most breached passwords globally! Hackers can crack this instantly.")

# Check 3: Success State
else:
    print("💎 SUCCESS: This password passed the length check and is not on the common hacker blocklist!")
import urllib.request  # Tool to download data from the internet
import re              # New Tool! 're' stands for Regular Expressions. It helps us scan text patterns.

print("--- Welcome to Python Password Security Guard (Advanced v3.0) ---")
print("Loading real-world threat intelligence blocklist... Please wait...")

try:
    # URL to fetch the top 1,000 most common leaked passwords
    url = "https://githubusercontent.com"
    response = urllib.request.urlopen(url)
    common_passwords = response.read().decode('utf-8').splitlines()
    print("✅ Real-world threat list successfully loaded!\n")

except Exception as e:
    print("⚠️ Could not connect to internet. Using offline backup list.")
    common_passwords = ["123456", "password", "123456789", "qwerty", "letmein123"]

# --- ASK USER FOR INPUT ---
user_password = input("Enter a password to scan for security risks: ")

# --- ADVANCED SECURITY CHECKS ---

# Check 1: Length Check
if len(user_password) < 8:
    print("❌ RISK DETECTED: Password must be at least 8 characters long.")

# Check 2: The Real Hacker Blocklist Check
elif user_password.lower() in common_passwords:
    print("❌ CRITICAL RISK: This password is in the Top 1,000 most breached passwords globally! Hackers can crack this instantly.")

# Check 3: Complexity Pattern Check (New!)
# We check if it is missing uppercase letters, lowercase letters, numbers, or symbols.
elif not re.search("[A-Z]", user_password):
    print("❌ WEAK PASSWORD: Your password needs at least one CAPITAL letter (A-Z).")

elif not re.search("[a-z]", user_password):
    print("❌ WEAK PASSWORD: Your password needs at least one lowercase letter (a-z).")

elif not re.search("[0-9]", user_password):
    print("❌ WEAK PASSWORD: Your password needs at least one number (0-9).")

elif not re.search("[_@$#!%*?&]", user_password):
    print("❌ WEAK PASSWORD: Your password needs at least one special character (like @, #, $, %, etc.).")

# Success State
else:
    print("💎 SUCCESS: This password is long, structurally strong, and safe from common hacker lists!")
import urllib.request  # Tool to download data from the internet
import re              # Tool to scan text patterns

print("--- Welcome to Python Password Security Guard (Advanced v4.0) ---")
print("Loading real-world threat intelligence blocklist... Please wait...")

try:
    # URL to fetch the top 1,000 most common leaked passwords
    url = "https://githubusercontent.com"
    response = urllib.request.urlopen(url)
    common_passwords = response.read().decode('utf-8').splitlines()
    print("✅ Real-world threat list successfully loaded!")
    print("Type 'exit' at any time to close the tool.\n")

except Exception as e:
    print("⚠️ Could not connect to internet. Using offline backup list.")
    common_passwords = ["123456", "password", "123456789", "qwerty", "letmein123"]

# --- THE CONTINUOUS LOOP ---
while True:
    print("-" * 50) # Prints a neat dividing line
    
    # Ask user for input
    user_password = input("Enter a password to scan for security risks: ")
    
    # If the user types 'exit', break the loop and stop the program
    if user_password.lower() == 'exit':
        print("\nThank you for using Password Security Guard. Stay safe online! 👋")
        break

    # --- ADVANCED SECURITY CHECKS ---

    # Check 1: Length Check
    if len(user_password) < 8:
        print("❌ RISK DETECTED: Password must be at least 8 characters long.")

    # Check 2: The Real Hacker Blocklist Check
    elif user_password.lower() in common_passwords:
        print("❌ CRITICAL RISK: This password is in the Top 1,000 most breached passwords globally! Hackers can crack this instantly.")

    # Check 3: Complexity Pattern Check
    elif not re.search("[A-Z]", user_password):
        print("❌ WEAK PASSWORD: Your password needs at least one CAPITAL letter (A-Z).")

    elif not re.search("[a-z]", user_password):
        print("❌ WEAK PASSWORD: Your password needs at least one lowercase letter (a-z).")

    elif not re.search("[0-9]", user_password):
        print("❌ WEAK PASSWORD: Your password needs at least one number (0-9).")

    elif not re.search("[_@$#!%*?&]", user_password):
        print("❌ WEAK PASSWORD: Your password needs at least one special character (like @, #, $, %, etc.).")

    # Success State
    else:
        print("💎 SUCCESS: This password is long, structurally strong, and safe from common hacker lists!")
# 🛡️ Advanced Python Password Security Guard

An advanced, enterprise-grade password scanner built in Python. This tool moves beyond simple length checks by integrating live threat intelligence and pattern analysis to defend against modern cyber threats.

## ✨ Advanced Features
- **🌐 Live Threat Intelligence**: Automatically downloads and checks passwords against a real-world hacker blocklist of the top 1,000 most common breached passwords globally.
- **🧠 Pattern Complexity Analysis**: Scans internal password structure for uppercase letters, lowercase letters, numbers, and special symbols using Regular Expressions (`re`).
- **🛡️ NIST-Aligned Rules**: Enforces strict industry-standard rules including a minimum 8-character limit.
- **🔄 Continuous Session Loop**: Runs safely in a continuous test loop so users can analyze multiple credentials in one session.
- **🔌 Offline Fallback**: Features a built-in safety net to keep scanning using an offline database if internet connectivity is lost.

## 🚀 How It Works
1. Run `security_guard.py` in your terminal or Python IDLE.
2. The script establishes a connection to online threat databases to load the latest blocklist.
3. Enter any password to view real-time security telemetry and risk flags.
4. Type `exit` to safely close the program.

## 🛠️ Built With
- **Python 3** (Core Language)
- `urllib.request` (For live threat data fetching)
- `re` (For cryptographic text pattern matching)
