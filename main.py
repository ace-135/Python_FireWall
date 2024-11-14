import sys
import subprocess

def network_interface():
    result = subprocess.run(['ifconfig'], capture_output=True, text=True)

    interfaces = []
    n = 0

    for line in result.stdout.splitlines():
        if line.strip() and line[0].isalpha():
            n += 1
            interface_name = line.split()[0]
            interface_name_clean = interface_name.replace(':', '')
            # print(f"{n} -> {interface_name.replace(':', '')}")
            interfaces.append((n, interface_name_clean))

    print(f'[+] Available network interfaces:')
    for num, iface in interfaces:
        print(f'{num} -> {iface}')

    while True:
        try:
            user_choice = int(input("[?] Enter the network interface number you want to select: "))
            if 1 <= user_choice <= len(interfaces):
                selected_interface = interfaces[user_choice - 1][1]
                print(f"[+] You selected: {selected_interface}")
                break
            else:
                print(f"[!] Invalid choice. Please select a number between 1 and {len(interfaces)}.")
        except ValueError:
            print("[!] Invalid input. Please enter a valid number.")

    return selected_interface

def main():
    net_interface = network_interface()


if __name__ == "__main__":
    main()
    # if len(sys.argv) != 2:
    #     print(f'[!] Usage: {sys.argv[0]} <network_interface')
    #     sys.exit(1)

    # interface = sys.argv[1]
    # main(sys.argv[1])