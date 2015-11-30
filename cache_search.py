
import os
import requests

def cache_search(purl, email):
    headers = {'User-Agent': 'Mining-for-Pentest'}
    purl = purl
    email = email
    base_url = 'https://webcache.googleusercontent.com/search?q=cache:'
    url = base_url+purl+'&strip=0&vwsrc=1'
    print url
    r1 = requests.get(url, headers = headers)
    print r1.status_code
    if r1.status_code != 302:
        if r1.status_code != 404:
            print '\n'
            print "\033[94m"+"=============================================================================================================="
            print "\033[98m [*]   Got It !!! Dump found in google cache for email account : "+purl
            print "\033[94m"+"=============================================================================================================="
            print '\033[92m'
            os.system('invoke_phantom.sh get_cache.js "'+url+'" local_cache.txt')
        else:
            print '\n \033[31m Could not find data dump in archives \n'

    
