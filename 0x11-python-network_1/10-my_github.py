#!/usr/bin/python3
"""Script to get GitHub credentials"""

import sys
import requests


def main():
    if len(sys.argv) != 3:
        print("Usage: {} <username> <password>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    auth = {"Authorization": "Bearer {}".format(password)}

    r = requests.get("https://api.github.com/user", headers=auth)
    
    if r.status_code == 200:
        print(r.json().get("id"))
    else:
        print("Authentication failed")


if __name__ == "__main__":
    main()
