# Breach-Miner
A quick and dirty upython based tool to harvest credentials from a leaked data dump

A handy tool for pentesters to recon their victims in scope. Using this tool one can identify the victims email account has been leaked during any breaches. The tool uses Troy Hunts haveibeenpwned api to search for accounts in breach dumps. 

It has two modes : Basic Mode and Detailed Analysis Mode. If the account is found in any breaches, it searches the respective site (pastebin/slexy/pastie) and do an advance search in google cache the data is not found in the paste sites. The results are then written to a HTML file for easy usage.

Usage:
==============
git clone https://github.com/secworld/Breach-Miner.git && cd Breach-Miner 

./requirements.sh

chmod +x breachminer.py

python breachminer.py


Tested On:
===========
Kali 2.0

To Do:
=======

A lot to do :)

[*] More efficient and fast searching of credentials in the dump

[*] Juicy information retrival from other sources respective to the account (other than using the API)

[*] If passwords found then create a wordlist/dictionary

