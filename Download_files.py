from bs4 import BeautifulSoup
import urllib
import os
import requests
r  = requests.get("https://archive.org/download/gov.uscourts.ned.69317")
data = r.text
soup = BeautifulSoup(data, "lxml")
url = "https://archive.org/download/gov.uscourts.ned.69317"
a = []
i=0
for link in soup.find_all('a'):
    print(link.get('href'))
    a[i] = link.get('href')
    i = i+1
print(i)


'''    
i = 0
for tag in soup.findAll('a', href = True):
    tag['href'] = urllib.parse.urljoin(url,tag ['href'])
        
    if os.path.splitext(os.path.basename(tag['href']))[1] =='.pdf':
        current = urllib.request.urlopen(tag['href'])
            
        print ("\n[*] Downloading: %s" %(os.path.basename(tag['href'],"wb")))
        f = open("I:" + "\\" +os.path.basename(tag['href'],"wb"))
        f.write(current.read())
        f.close()
        i+=1      
            
print ("\n[*] Downloaded %d files" %(i+1))
input(" Press any key to exit --")

'''