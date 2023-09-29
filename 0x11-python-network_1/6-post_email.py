#!/usr/bin/python3
"""Script to send a POST request to a passed URL"""

import requests
import sys

def main():
    url = sys.argv[1]
    emailAddress = sys.argv[2]
    data = {
        "email": emailAddress
    }
    r = requests.post(url, data=data)
    print(r.text)

if __name__ == "__main__":
    main()
