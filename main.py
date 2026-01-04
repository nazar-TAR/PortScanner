import ipaddress
import socket
from scanner_class import PortScanner

def print_banner():
    print('=' * 80)
    banner = f"""
  _____  __     __        _____  _____          _   _ _   _ ______ _____  
 |  __ \ \ \   / /       / ____|/ ____|   /\   | \ | | \ | |  ____|  __ \ 
 | |__) | \ \_/ / _____ | (___ | |       /  \  |  \| |  \| | |__  | |__) |
 |  ___/   \   / |_____| \___ \| |      / /\ \ | . ` | . ` |  __| |  _  / 
 | |        | |          ____) | |____ / ____ \| |\  | |\  | |____| | \ \ 
 |_|        |_|         |_____/ \_____/_/    \_\_| \_|_| \_|______|_|  \_\

                [+] Created by: https://github.com/nazar-TAR
                [+] Version: 1.0
    """
    print(banner)
    print('Every open port is a story waiting to be told;)')
    print('=' * 80)

def get_target_ip():
    print(f'Write IP or Domain address:')
    ip = input()
    try:
        target = str(ipaddress.ip_address(ip))
    except ValueError:
        try:
            target = socket.gethostbyname(ip)
            print(f"Target IP: {target}")
        except socket.gaierror:
            print('Hostname could not be resolved')
            exit()
    return target

def get_port_range():
    print(f'Choose scanning mode:\n1: Default (1-1024),\n2: All ports (1-65535),\n3: Set by yourself.')
    user_choice = input()
    if user_choice == '1':
        start_port = 1
        end_port = 1024
    elif user_choice == '2':
        start_port = 1
        end_port = 65535
    else:
        print('Enter range of ports which you want to scan.')
        print('Start port:')
        start_port = int(input())
        print('End port:')
        end_port = int(input())
    return start_port, end_port

if __name__ == "__main__":
    print_banner()
    target = get_target_ip()
    start, end = get_port_range()
    scanner = PortScanner(target, start, end)
    scanner.run()
    scanner.show_results()