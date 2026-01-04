import socket
from concurrent.futures import ThreadPoolExecutor
import time

class PortScanner:
    def __init__(self, target, start_port, end_port, threads=100):
        self.target = target
        self.start_port = start_port
        self.end_port = end_port
        self.threads = threads
        self.timeout = 0.5
        self.open_ports = []

    def _check_port(self, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.8)
        result = s.connect_ex((self.target, port))
        if result == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = 'Unknown service'
            try:
                data = s.recv(1024)
                banner = data.decode(errors='ignore').replace('\n', ' ').strip()
                if not banner:
                    banner = 'No banner (silent srvice)'
            except:
                banner = 'No banner response'
            self.open_ports.append((port, service, banner))
        s.close()

    def run(self):
        try:
            start_time = time.time()
            print(f'Scanning for {self.target}...\nWaiting!')
            with ThreadPoolExecutor(self.threads) as executor:
                executor.map(self._check_port, range(self.start_port, self.end_port + 1))
            print(f'Scanning is finished! \nTotal time: {time.time() - start_time:.2f}')
        except KeyboardInterrupt:
            print('Scan Stopped')
            print(f'Total time: {time.time() - start_time:.2f}')
        except socket.error:
            print('Problems with Network')
            print(f'Total time: {time.time() - start_time:.2f}')

    def show_results(self):
        self.open_ports.sort()
        print(f"\n{'PORT':<7} | {'SERVICE':<15} | {'BANNER'}")
        for port, service, banner in self.open_ports:
            display_banner = (banner[:55] + '...') if len(banner) > 55 else banner
            print(f"{port:<7} | {service:<15} | {display_banner}")