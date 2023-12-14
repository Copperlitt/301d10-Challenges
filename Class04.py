#!usr/bin/python3

import os
import socket
import psutil

# Function to print the menu options
def print_menu():
    print("Menu")
    print("1. Hello world")
    print("2. Ping self")
    print("3. IP info")
    print("4, Exit")

 # Function to handle the "Hello world" option
    def hello_world():
        print("Hello world")

# Function to handle the "Ping self" option
        
def ping_self():
    localhost = "127.0.0.1"
    response = os.system(f"ping {localhost}")
    if response == 0:
        print(f"{localhost} is reachable")
    else:
        print(f"{localhost} is unreachable")


# Funchtion to handle the "IP info" option
def ip_info():
    # Get network adapter information
    for interface, addrs in psutil.net_if_addrs().items()
        print(f"Interface: {interface}")
        for addr in addrs:
            print(f"  Address: {addr.address} Netmask: {addr.netmask} Broadcast: {addr.broadcast}")

# Main function to run the menu system
def main():
    while True:
        print_menu()


        # Get user input
        choice = input("Enter your choice (1-4): ")


        # Use a conditional statement to evaluate the user's input
        if choice =="1":
            hello_world()
        elif choice =="2":
            ping_self()
        elif choice =="3":
            ip_info()
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4")


if __name__ == "_main_":
    main()
    