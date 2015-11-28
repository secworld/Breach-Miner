#! /usr/bin/python

import requests
import urllib
import os.path
import re
import colorama

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = ''
    RED = '\033[31m'

def CredMiner(f,strn):
    with open(f) as f:
        for line in f:
            match = re.findall(strn, line)
            if match == None:
                print line
                
            

headers = {'User-Agent' : 'Digging-for-Pentesting', 'Accept' : 'application/vnd.haveibeenpwned.v2+json'}
BaseUrl = 'https://haveibeenpwned.com/api/v2/pasteaccount/'
os.system('clear')
EmailList = raw_input("\033[92m Enter the path of the file containing Email Accounts : ")
choice = raw_input("\033[92m Do you want to go for a detailed analysis \033[93m[Y/N] : ")

os.system('clear')
print ("\n  [*] "+"\033[92m"+"I am mining ... Sit back and relax !!!")

with open(EmailList) as f:
    for email in f:
        Url1 = urllib.quote(email, safe='')
        Url = BaseUrl+Url1
        Url = Url[:-3]
        r = requests.get(Url, headers = headers)
        try:
            JsonData =  (r.json())
        except ValueError, e:
            print "\n \033[31m [*] No data found for " + email
            
        if (r.status_code == 200):
            print ('\n')
            print ("\033[94m *************************************************************************************")
            print '  \033[93m  [*] Located email account in leaked data dumps for : \033[93m'+email
            print ("\033[94m *************************************************************************************")
            print ('\n')
            for item in JsonData:
                source = item.get('Source')
                did = item.get('Id')
                title = item.get('Title')
                if title is None:
                    title = "None"
                    
                if choice.lower() == 'n':
                    print ('\n')
                    print "\033[92m Title of the dump : "+title
                    print "\033[92m Source of the dump : "+source
                    print "\033[92m Breach data can be found at : "+source+"/"+did
                    print ('\n')
                    
                if choice.lower() == 'y':
                    if source == 'Pastebin':
                        puid = did
                        purl = 'http://pastebin.com/raw.php?i='+puid
                        r1 = requests.get(purl, headers = headers)
                        if r1.status_code != 302:
                            if r1.status_code != 404:
                                print '\n'
                                print "\033[94m"+"=============================================================================================================="
                                print "\033[98m [*]   Got It !!! Dump found at "+purl+' for email account \033[93m'+email
                                print "\033[94m"+"=============================================================================================================="
                                CurrPath =  os.getcwd()+'/tmp.txt'
                                grab = str('wget '+purl+' -O  '+CurrPath+' > /dev/null 2>&1')
                                os.system(grab)
                                #CredMiner(CurrPath, email)
                                print '\033[92m'
                                os.system('cat '+CurrPath+' | grep -B 1 -A 1 '+email)
                                if os.path.exists(CurrPath):
                                    #os.system('mv '+CurrPath+' tmp.txt.bkp')
                                    os.system('rm '+CurrPath)
                                
                            else:
                                print "\n \033[31m [*] Sorry !!! The pastebin dumb seems to be missing at "+source+"/"+did+"  :( "
                            
                            

print "\n   \033[92m +++++++ \033[31m Happy Hunting \033[92m +++++++++"

