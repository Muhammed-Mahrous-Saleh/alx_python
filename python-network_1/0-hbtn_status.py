#!/usr/bin/python3
"Module that fetches https://alx-intranet.hbtn.io/status"
import requests


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    r = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(r.text))
    print("\t- content: {}".format(r.text))
