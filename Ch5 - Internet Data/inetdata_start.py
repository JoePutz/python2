# 
# Example file for retrieving data from the internet
# LinkedIn Learning Python course by Joe Marini
#

import urllib.request

def main():
    weburl = urllib.request.urlopen("http://www.google.com")
    print("result code:", weburl.getcode())
    # result code (200 if it's working)
    data = weburl.read()
    print(data)
    # the html code for google homepage
    

if __name__ == "__main__":
    main()
