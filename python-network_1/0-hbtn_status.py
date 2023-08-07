#!/usr/bin/python3
"Module that fetches https://alx-intranet.hbtn.io/status"
import requests


if __name__ == "__main__":
    with requests.get("https://alx-intranet.hbtn.io/status") as r:
        print('Body response:')
        print('\t- type: {}'.format(type(r.text)))
        print('\t- content: {}'.format(r.text))
