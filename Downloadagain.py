import requests
PDF_URL = "https://media.defcon.org/DEF CON 25/DEF CON 25 presentations/"

if __name__ == "__main__":
    urls = [line.rstrip('\n') for line in open('filestodownload')]
    for url in urls:
        response = requests.get(PDF_URL+str(url))
        if response.status_code == 200:
            with open(str(url), 'wb') as fout:
                fout.write(response.content)
        else:
            print("[ERROR] I could not grab %s" % str(url))