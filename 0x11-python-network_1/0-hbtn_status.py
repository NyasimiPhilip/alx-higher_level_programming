#!/usr/bin/python3
"""Fetch a URL and display the body of the response"""

import urllib.request as request


def main():
    url = "https://alx-intranet.hbtn.io/status"

    with request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print("\t- Type: {}".format(type(body)))
        print("\t- Content: {}".format(body))
        print("\t- UTF-8 Content: {}".format(body.decode("utf-8")))


if __name__ == "__main__":
    main()
