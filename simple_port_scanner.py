import socket
import sys
import pyfiglet
from datetime import datetime

def list_ports(ports):
    #Print the results of the scan.
    print("Result of scan: ")
    for item in ports:
        print(f"{item} : open")

def scan(start,end,target_ip):
    ports = []
    socket.setdefaulttimeout(0.1)
    print(f"Started scanning at {datetime.now()}")

    #Loop through the specified port range.
    for port in range(start,end+1):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        connection = s.connect_ex((target_ip,port))
        if connection == 0:
            print(f"Port {port} is open.")
            ports.append(port)
        s.close()

    print("-" * 20)
    print(f"Scan finished at {datetime.now()}")
    print("-" * 20)
    list_ports(ports)

if __name__ == '__main__':
    #Print banner
    print(pyfiglet.figlet_format("Simple Port Scanner") + ("-" * 20))
    target_ip = input("Type target ip: ")

    #Try to resolve the hostname and exit on error.
    try:
        target_ip = socket.gethostbyname(target_ip)
    except socket.gaierror:
        print("\nError: Hostname could not be resolved.")
        sys.exit()
    except socket.error:
        print("\nError: Server not responding.")
        sys.exit()

    #Specify the range of scanned ports.
    start = int(input("Type starting port number: "))
    end = int(input("Type end port number: "))
    scan(start,end,target_ip)