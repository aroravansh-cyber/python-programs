import os
import time
import ipaddress


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def show_banner():
    print("=" * 40)
    print("       IP SECURITY ANALYZER")
    print("=" * 40)


def show_menu():
    print("\n1. Analyze IP")
    print("2. Exit")
    print("=" * 40)


def loading():
    print("\nAnalyzing", end="")

    for i in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)

    print()


def analyze_ip(ip):
    try:
        address = ipaddress.ip_address(ip)

        print("\n--- IP INFORMATION ---")
        print(f"IP Address : {ip}")
        print(f"Version    : IPv{address.version}")
        print(f"Private IP : {'Yes' if address.is_private else 'No'}")
        print(f"Global IP  : {'Yes' if address.is_global else 'No'}")
        print(f"Loopback   : {'Yes' if address.is_loopback else 'No'}")
        print(f"Multicast  : {'Yes' if address.is_multicast else 'No'}")
        print(f"Reserved   : {'Yes' if address.is_reserved else 'No'}")

    except ValueError:
        print("\nInvalid IP address.")


def main():
    clear_screen()

    while True:
        show_banner()
        show_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            ip = input("\nEnter an IP address: ")

            loading()
            analyze_ip(ip)

        elif choice == "2":
            print("\nProgram closed.")
            break

        else:
            print("\nInvalid choice. Please try again.")


main()