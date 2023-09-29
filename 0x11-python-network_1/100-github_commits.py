#!/usr/bin/python3
"""Script to list GitHub commits of a repo"""

import requests
import sys


def main():
    if len(sys.argv) != 3:
        print("Usage: {} <repository> <owner>".format(sys.argv[0]))
        sys.exit(1)

    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits?per_page=10"

    try:
        r = requests.get(url)
        r.raise_for_status()
        response = r.json()

        for item in response:
            sha = item.get("sha")
            author = item.get("commit").get("author").get("name")
            print("{}: {}".format(sha, author))
    
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
