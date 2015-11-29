# Breach-Digger
A quick and dirty upython based tool to harvest credentials from a leaked data dump

Just a handy tool for pentesters to recon their victims in scope. Using this tool one can identify the victims email account has been leaked during any breaches. The tool uses Troy Hunts haveibeenpwned api to search for accounts in breach dumps. 

Usage:
==============
git clone https://github.com/secworld/Breach-Miner.git && cd Breach-Miner
chmod +x breachminer.py requirements.sh
./requirements.sh
python breachminer.py


Tested On:
===========
Kali 2.0

To Do:
=======
A lot to do :)
[*] Currently supports only dumps from pastebin. To support other dumps too
[*] More efficient and fast searching of credentials in the dump
[*] Juicy information retrival from other sources respective to the account (other than using the API)
[*] If passwords found then create a wordlist/dictionary

