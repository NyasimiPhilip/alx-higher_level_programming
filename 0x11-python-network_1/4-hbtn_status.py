#!/usr/bin/python3
"""Script to fetch URL using the requests module"""
import requests

def main():
    r = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))

if __name__ == "__main__":
    main()
