#!/usr/bin/python3

def multiple_returns(text=''):
    if text:
        return len(text), text[0]
    else:
        return 0, None