import socket
import ipaddress


def get_local_ip():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    print("Your IPV4 is:", local_ip)
    return local_ip

def check_ip(ip):
    try:
        address = ipaddress.ip_address(ip)
        try:
            hostname = socket.gethostbyaddr(ip)[0]
        except socket.herror:
            hostname = "Unknown"
        print("\n--- IP Security Check ---")
        print(f"IP Address : {ip}")
        print(f"Hostname   :",hostname)
        print(f"Version    : IPv{address.version}")
        print(f"Private IP : {'Yes' if address.is_private else 'No'}")
        print(f"Global IP  : {'Yes' if address.is_global else 'No'}")
        print(f"Loopback   : {'Yes' if address.is_loopback else 'No'}")
        print(f"Multicast  : {'Yes' if address.is_multicast else 'No'}")

    except ValueError:
        print("Invalid IP address.")

print("Welcome to the IP Security Check Program!")
ch=input("Do you want to check your local IP address? (yes/no): ")
if ch.lower() == "yes":
    get_local_ip()
    while True:
        ip = input("\nEnter an IP address (or 'exit'): ")

        if ip.lower() == "exit":
            print("Program closed.")
            break

        check_ip(ip)
elif ch.lower()== "no":
    while True:
        ip = input("\nEnter an IP address (or 'exit'): ")

        if ip.lower() == "exit":
            print("Program closed.")
            break

        check_ip(ip)
