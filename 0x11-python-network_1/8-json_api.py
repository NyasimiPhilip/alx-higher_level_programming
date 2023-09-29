#!/usr/bin/python3
"""Script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user with the letter as a parameter."""

import sys
import requests


def main():
    letter = ""
    url = "http://0.0.0.0:5000/search_user"

    if len(sys.argv) >= 2:
        letter = sys.argv[1]

    data = {"q": letter}
    r = requests.post(url, data=data)

    try:
        res = r.json()

        if len(res.keys()) == 0:
            print("No result")
        else:
            print("[{}] {}".format(res.get("name"), res.get("name")))

    except Exception:
        print("Not a valid JSON")


if __name__ == "__main__":
    main()
