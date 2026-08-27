import socket
import ipaddress

def check_ip(ip):
    try:
        address = ipaddress.ip_address(ip)

        print("\n--- IP Security Check ---")
        print(f"IP Address : {ip}")
        print(f"Version    : IPv{address.version}")
        print(f"Private IP : {'Yes' if address.is_private else 'No'}")
        print(f"Global IP  : {'Yes' if address.is_global else 'No'}")
        print(f"Loopback   : {'Yes' if address.is_loopback else 'No'}")
        print(f"Multicast  : {'Yes' if address.is_multicast else 'No'}")

    except ValueError:
        print("Invalid IP address.")


while True:
    ip = input("\nEnter an IP address (or 'exit'): ")

    if ip.lower() == "exit":
        print("Program closed.")
        break

    check_ip(ip)
