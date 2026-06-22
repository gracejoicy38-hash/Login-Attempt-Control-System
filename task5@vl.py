import time
# Correct credentials
USERNAME = "admin"
PASSWORD = "secure123"
max_attempts = 3
lock_time = 10  # seconds
attempts = 0
while True:
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    if username == USERNAME and password == PASSWORD:
        print("Login Successful!")
        break
    else:
        attempts += 1
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"Invalid credentials! {remaining} attempt(s) remaining.")
        else:
            print(f"\nToo many failed attempts!")
            print(f"Account locked for {lock_time} seconds.\n")
            time.sleep(lock_time)
            attempts = 0
            print("You can try logging in again.")