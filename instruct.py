#from bs4 import BeautifulSoup    
import urllib2 
import re
import requests
import time

#url = urllib2.urlopen("https://www.instructables.com/member/Ajaxjones/")    
#content = url.read()    

#print soup

def get_url(url, time_out=600):
    r = requests.get(url)
    sleep_time = 1.0
    while r.status_code != 200:
        print("sleep {}s".format(sleep_time))
        print(url)
        time.sleep(sleep_time)
        r = requests.get(url)
        sleep_time += 2
        if (sleep_time > time_out):
            # We have sleeped for over 10 minutes, the page probably does
            # not exist.
            break
    if r.status_code != 200:
        print("failed to retrieve {}".format(url))
    else:
        return r
        # return r.text


def get_views(text):
    myviews =[]
#    pattern = "(\d+\s)Views"
#    pattern = "total-views\">(\d+.\d{3})"
    pattern = "total-views\">((\d+).(\d{3}))"
    matched = re.findall(pattern, text)
#    print ("m0",matched[0][2])
    kio =  matched[0][1]+matched[0][2]
#    print (kio)
    return int(kio)
#    return [int(val) for val in kio]


author = "Ajaxjones"
base_url = "https://www.instructables.com/member/{}"
url = base_url.format(author)

contents = get_url(url).text
views  =  get_views(contents)
#print (contents)
print (views)
