# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 21:01:30 2018

@author: appu
"""

import urllib.parse
import urllib.request
import urllib.error
from urllib.request import urlopen
import os
import sys
from bs4 import BeautifulSoup

url = input("Enter the URL:")
download_path = input(" Enter the download path in full:")

try:
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}
    i = 0
    request = urllib.request(url, None, headers)
    html = urlopen(request)
    soup = BeautifulSoup(html.read())
    
    for tag in soup.findAll('a', href = True):
        tag['href'] = urllib.parse.urljoin(url,tag ['href'])
        
        if os.path.splitext(os.path.basename(tag['href']))[1] =='.pdf':
            current = urlopen(tag['href'])
            
            print ("\n[*] Downloading: %s" %(os.path.basename(tag['href'],"wb")))
            f = open(download_path + "\\" +os.path.basename(tag['href'],"wb"))
            f.write(current.read())
            f.close()
            i+=1

    print ("\n[*] Downloaded %d files" %(i+1))
    input(" Press any key to exit --")

except KeyboardInterrupt:
    print ("[*] Exiting..")
    sys.exit(1)

except urllib.error.URLError as e:
    print ("[*] could not get information of the URL")
    sys.exit(2)

except:
    print ("Some issues")
    sys.exit(3)
