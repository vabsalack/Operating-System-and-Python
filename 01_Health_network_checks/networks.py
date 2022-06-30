import requests
import socket


def check_localhost():
    """ To know about localhost/loopback IPV4 adder:
         https://www.lifewire.com/network-computer-special-ip-address-818385"""

    localhost = socket.gethostbyname('localhost')
    return localhost == "127.0.0.1"


def check_connectivity():
    """This returns the website's status code. This status code is an integer value. Now,
       assign the result to a response variable and check the status_code attribute of that variable.
       It should return 200."""
    request = requests.get("http://www.google.com")
    return request.status_code == int(200)
