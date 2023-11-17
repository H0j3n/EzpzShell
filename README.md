![](https://github.com/H0j3n/EzpzShell/blob/main/demo.gif)

# What is EzpzShell ❓

The idea is to collect all reverse shell methods that can be found on the internet to be used in CTF or if we found command execution vulnerability during penetration testing. Hopefully, this GitHub could be useful and resourceful. 

# Disclaimer ✅

Do not use this script for **illegal** use. Any action you take upon the information on this repo is strictly at your own risk

# How to use ❓

You can add this alias in your .bashrc or .zshrc

```bash
# Alias
alias listen="python3 /pathto/EzpzShell/ezpzShell.py"

# Usage
listen 10.10.10.10 443 py3
listen 10.10.10.10 443 py3 -payload (Only Payload)
```

# Extra ‼️

Please check https://github.com/0dayCTF/reverse-shell-generator which you can check https://www.revshells.com/

```
Hosted Reverse Shell generator with a ton of functionality. -- (Great for CTFs) and really nice UI!
```

## Python 🐍

Specify the IP, Port and the options that are available.

```python
python3 ezpzShell.py 10.10.10.10 9001 py

python3 ezpzShell.py 10.10.10.10 9001 py -payload
```

Or just specify the interface that you want to use.

```python
python3 ezpzShell.py tun0 9001 py

python3 ezpzShell.py eth0 9001 py

python3 ezpzShell.py eth0 9001 py -payload
```

# Additional Information

If you want to add your reverse shell just customize `updates.yaml`

# Reverse Shell Available ❇️

* py
* py3
* bash
* c
* nc
* php
* perl
* ruby
* haskell
* powershell
* node
* awk
* ncat
* msf_exe
* ssti

	-> Twig

	-> Jinja/Flask

	-> Tornado

	-> PugJS
* cgi-bin

	-> Apache 2.4.49 (CVE-2021-41773)
	
	-> Apache 2.4.50 (CVE-2021-42013)
* jenkins
* tar-priv
* pickle 
* java
* lua
* asp
* xxe
* jsp
* c#
* xsl
* yaml
* sql
* wordpress
* json.net (Deserialization)
* msf_raw
* msf_dll
* msf_elf
* dag
* firebird
* apt_confd
* gdb_server
* log4j
* zabbix
* mysql

        -> CVE-2021-27928
* lua

# Todo ✍🏼

[+] Update new reverse shell encountered
 
# References

[1] http://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet

[2] https://highon.coffee/blog/reverse-shell-cheat-sheet/

[3] https://gist.github.com/Robleh/28234d9fe40e9baa1787396c7ad54350

[4] https://github.com/hoainam1989/training-application-security/blob/master/shell/node_shell.py

[5] https://github.com/borjmz/aspx-reverse-shell

[6] https://github.com/antonioCoco/ConPtyShell

[7] https://github.com/0x03f3/php-emoji-reverse-shell

[8] https://github.com/juju/utils/blob/master/shell/powershell.go

[9] https://github.com/LukeDSchenk/rust-backdoors

[10] https://github.com/he4d/networkmanager-rs

[11] https://github.com/mabels/ipaddress

[12] https://rust-lang-nursery.github.io/rust-cookbook/file/read-write.html

[13] https://stackoverflow.com/questions/61297668/how-to-interact-with-a-reverse-shell-in-rust

[14] https://www.puckiestyle.nl/c-simple-reverse-shell/

[15] https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/XSLT%20Injection

[16] https://staaldraad.github.io/post/2019-03-02-universal-rce-ruby-yaml-load/

[17] https://www.exploit-db.com/docs/english/47655-yaml-deserialization-attack-in-python.pdf?utm_source=dlvr.it&utm_medium=twitter

[18] https://github.com/j0lt-github/python-deserialization-attack-payload-generator

[19] https://github.com/pwntester/ysoserial.net
