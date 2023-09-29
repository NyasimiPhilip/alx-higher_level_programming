#!/usr/bin/python3
"""Script that takes in a URL, sends a request to the URL, and displays the body of the response (decoded in utf-8)."""

from urllib.request import urlopen
from urllib.error import HTTPError
import sys

def fetch_and_display(url):
    try:
        with urlopen(url) as response:
            body = response.read()
            decoded_body = body.decode("utf-8")
            return decoded_body
    except HTTPError as err:
        return f"Error code: {err.code}"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    response_body = fetch_and_display(url)
    print(response_body)
