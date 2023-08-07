#!/usr/bin/python3
"Module that fetches https://alx-intranet.hbtn.io/status"
import requests


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with requests.get(url) as r:
        print('Body response:')
        print('\t- type: {}'.format(type(r.text)))
        print('\t- content: {}'.format(r.text))
        print('\t- content2: {}'.format(r))
