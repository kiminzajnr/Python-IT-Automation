#! /usr/bin/env python3
import os
import requests

"""
this script uploads all the feedback stored in /data/feedback folder
to a django website without having to turn it into a dictionary one by one
"""

data_lst = []
dct_keys = ["title", "name", "date", "feedback"]
files_lst = os.listdir("/data/feedback")

def readlines(file):
    """
    reads file lines into a list
    """
    with open("/data/feedback") as fl:
        lines = fl.read().splitlines()
    return lines

for file in files_lst:
    lines = readlines(file)
    data_lst.append(dict(zip(dct_keys, lines)))

for _ in data_lst:
    response = requests.post("http://<extern ip address>/feedback/", data=_)
    if response.ok:
        print(success)
    else:
        print(response.status_code)
