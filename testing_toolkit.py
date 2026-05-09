import socket
import requests

# =========================
# PORT SCANNER MODULE
# =========================
def port_scanner(target, ports):
    print(f"\nScanning Target: {target}\n")

    for port in ports:
        scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        scanner.settimeout(1)

        result = scanner.connect_ex((target, port))

        if result == 0:
            print(f"[OPEN] Port {port}")
        else:
            print(f"[CLOSED] Port {port}")

        scanner.close()

# =========================
# BANNER GRABBER MODULE
# =========================
def banner_grabber(target, port):
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((target, port))

        banner = s.recv(1024).decode().strip()

        print(f"\nBanner from {target}:{port}")
        print(banner)

        s.close()

    except:
        print("Could not grab banner")

# =========================
# HTTP HEADER CHECKER
# =========================
def header_checker(url):
    try:
        response = requests.get(url)

        print("\nHTTP Headers:\n")

        for header, value in response.headers.items():
            print(f"{header}: {value}")

        important_headers = [
            "Content-Security-Policy",
            "Strict-Transport-Security",
            "X-Frame-Options"
        ]

        print("\nSecurity Header Analysis:\n")

        for header in important_headers:
            if header in response.headers:
                print(f"[OK] {header} Present")
            else:
                print(f"[MISSING] {header}")

    except:
        print("Unable to access website")

# =========================
# PASSWORD STRENGTH CHECKER
# =========================
def password_checker(password):
    strength = 0

    if len(password) >= 8:
        strength += 1

    if any(char.isdigit() for char in password):
        strength += 1

    if any(char.isupper() for char in password):
        strength += 1

    if any(char in "!@#$%^&*" for char in password):
        strength += 1

    print("\nPassword Strength Result:\n")

    if strength == 4:
        print("Strong Password")
    elif strength == 3:
        print("Moderate Password")
    else:
        print("Weak Password")

# =========================
# MAIN MENU
# =========================
while True:
    print("\n===== PENETRATION TESTING TOOLKIT =====")
    print("1. Port Scanner")
    print("2. Banner Grabber")
    print("3. HTTP Header Checker")
    print("4. Password Strength Checker")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        target = input("Enter target IP or domain: ")
        ports = [21, 22, 23, 25, 53, 80, 110, 443]
        port_scanner(target, ports)

    elif choice == "2":
        target = input("Enter target IP or domain: ")
        port = int(input("Enter port number: "))
        banner_grabber(target, port)

    elif choice == "3":
        url = input("Enter website URL (with http/https): ")
        header_checker(url)

    elif choice == "4":
        password = input("Enter password to test: ")
        password_checker(password)

    elif choice == "5":
        print("Exiting Toolkit...")
        break

    else:
        print("Invalid Choice")
