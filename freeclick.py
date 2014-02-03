#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File Name : freeclick.py
# Purpose : Free Internet and Free click
# Creation Date : 1391345970
# Last Modified : Mon 03 Feb 2014 10:49:10 AM CST
# Release By : Doom.zhou
import urllib.request
import os
import re
from random import randrange

#print("start")

C_agent = {'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) \
               AppleWebKit/537.36 (KHTML, like Gecko) \
               Chrome/31.0.165063 Safari/537.36 AppEngine-Google."}

url = 'http://socksproxy-list.blogspot.ca/search/label/Socks%20Proxy'

def get_proxy(tarurl):
    c_proxy = {"http":"http://127.0.0.1:8087"}
    flag = '#fdc93c;">'
    flagre = re.compile('[0-9]\n</span>')
    page = urllib.request.FancyURLopener(c_proxy).open(tarurl).read().decode("utf-8")
    s = page.find(flag) + len(flag)
    e = flagre.search(page).start() + 1
    target = page[s:e]
    return target

def main():
    try:
        print("Wish you can get the latest Socke5 proxy list")
        #get_proxy(url)
        sock_list = get_proxy(url)
        print(sock_list.count(':'))
        sl = sock_list.split("\n")[randrange(sock_list.count(':'))]
        print("using %s" % format(sl))
        print("Fetch Complete!Well Done!")
        print("Next start Tor with Socke5Proxy option.....")
        cmd = "tor -f /etc/tor/torrc Socks5Proxy %s" % sl
        os.system(cmd)
    except:
        print("Network issue or proxy access!")

if __name__ == "__main__":
    main()
