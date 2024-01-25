![](https://github.com/H0j3n/EzpzShell/blob/main/demo.gif)

### What is EzpzShell ❓

The idea is to collect all reverse shell methods that can be found on the internet to be used in CTF or if we found command execution vulnerability during penetration testing. Hopefully, this GitHub could be useful and resourceful. 

### Disclaimer ✅

Do not use this script for **illegal** use. Any action you take upon the information on this repo is strictly at your own risk

### How to intall & use ❓

```bash
# Install
git clone https://github.com/H0j3n/EzpzShell.git
cd EzpzShell
python3 setup.py install

# Usage
listen 10.10.10.10 443 py3
listen 10.10.10.10 443 py3 -payload (Only Payload)
```

# Extra ‼️

Please check https://github.com/0dayCTF/reverse-shell-generator which you can check https://www.revshells.com/

```
Hosted Reverse Shell generator with a ton of functionality. -- (Great for CTFs) and really nice UI!
```

# Additional Information

If you want to add your reverse shell just customize `ezpzShell/utils/update_yaml.py`

# Reverse Shell Available ❇️

```cs
  ______               _____ _          _ _
 |  ____|             / ____| |        | | |
 | |__   _____ __ ___| (___ | |__   ___| | |
 |  __| |_  / '_ \_  /\___ \| '_ \ / _ \ | |
 | |____ / /| |_) / / ____) | | | |  __/ | |
 |______/___| .__/___|_____/|_| |_|\___|_|_|
            | |
            |_| by H0j3n

-------- [ PAYLOAD AVAILABLE ] --------

[ansible] [apt_confd] [asp] [awk] [bash] [c] [c#] [cgibin] [dag] [firebird] 
[gdb_server] [haskell] [java] [jenkins] [json.net] [jsp] [log4j] [lua] [msf_dll] [msf_elf] 
[msf_exe] [msf_raw] [mysql] [nc] [ncat] [node] [perl] [php] [php_lfi] [pickle] 
[powershell] [py] [py3] [ruby] [splunk_rce] [sql] [sqlite3] [ssti] [tarpriv] [tomcat] 
[wordpress] [xsl] [xxe] [yaml] [zabbix] 
```

| Payload |  Description |
| ------ |  ---- |
| ansible | |
| apt_confd | |
| asp | |
| awk | |
| bash | |
| c | |
| c# | |
| cgibin | |
| dag | |
| firebird | |
| gdb_server | |
| haskell | |
| java | |
| jenkins | |
| json.net | |
| jsp | |
| log4j | |
| lua | |
| msf_dll | |
| msf_elf | |
| msf_exe | |
| msf_raw | |
| mysql | |
| nc | |
| ncat | |
| node | |
| perl | |
| php | |
| php_lfi | |
| pickle | |
| powershell | |
| py | |
| py3 | |
| ruby | |
| sql | |
| sqlite3 | |
| ssti | |
| tarpriv | |
| tomcat | |
| wordpress | |
| xsl | |
| xxe | |
| yaml | |
| zabbix | |
| splunk_rce | [Splunk Enterprise 7.2.4 - Custom App Remote Command Execution](https://www.exploit-db.com/exploits/46487)|

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
