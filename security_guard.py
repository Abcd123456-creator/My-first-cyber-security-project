print("--- UPGRADED PASSWORD SECURITY GUARD ---")

# 1. Ask the user for a password
password = input("Please enter a password to test: ")

# 2. Setup our security checks
has_eight_characters = len(password) >= 8
has_a_number = False

# 3. Look at each character to find a number
for character in password:
    if character.isdigit():
        has_a_number = True

# 4. The Final Security Report
if has_eight_characters and has_a_number:
    print("✅ SUCCESS: This password is long AND has numbers. Great job!")
elif has_eight_characters and not has_a_number:
    print("❌ ALERT: It is long enough, but you need to add at least one number!")
else:
    print("❌ ALERT: This password is too short!")


