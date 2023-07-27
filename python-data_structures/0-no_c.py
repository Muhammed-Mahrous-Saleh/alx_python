#!/usr/bin/env python3

def no_c(text):
    my_text = []
    for i in range(len(text)):
        if text[i] in ["c", "C"]:
            my_text.append('')
        else:
            my_text.append(text[i])
    return ''.join(my_text)
