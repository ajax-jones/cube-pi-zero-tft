#!/usr/bin/python
########################################################################
#
# A Python script for retrieving views of projects of an Instructable Author
# Author : Ajax Jones
# Date : 5 Dec 2018
# For more information, https://www.instructables.com/member/Ajaxjones/
########################################################################    
import urllib2 
import re
import requests
import time

# URL get routine with timeout options
def get_url(url, time_out=120):
    r = requests.get(url)
    sleep_time = 1.0
    while r.status_code != 200:
        print("sleep {}s".format(sleep_time))
        print(url)
        time.sleep(sleep_time)
        r = requests.get(url)
        sleep_time += 2
        if (sleep_time > time_out):
            # We have slept for over 2 minutes, so we give up
            break
    if r.status_code != 200:
        print("failed to retrieve {}".format(url))
    else:
        return r

def get_views(text):
    pattern = "total-views\">((\d+).(\d{3}))"
    matched = re.findall(pattern, text)
    author_views =  matched[0][1]+matched[0][2]
    return int(author_views)

########################################################################    
# Main Routine

author = "Ajaxjones"
base_url = "https://www.instructables.com/member/{}"
url = base_url.format(author)

contents = get_url(url).text
views  =  get_views(contents)
print (views)
