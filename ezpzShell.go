package main

import (
	"fmt"
	"os"
	"net"
	"regexp"
	"strings"
	"io/ioutil"
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
	
	fmt.Print("\n\n",string(colorCyan),"[Usage]",string(colorReset),"\n")
	fmt.Print(string(colorOrange),"ezpzShell 10.10.10.10 9001 py",string(colorReset),"\n")
	fmt.Print(string(colorOrange),"ezpzShell tun0 9001 py",string(colorReset),"\n")
}

//Function Load Shell
func loadShell(mapPayload map[string][]string) {
	mapPayload["py"] = append(mapPayload["py"],"")
	mapPayload["py3"] = append(mapPayload["py3"],"")
	return
}

func main(){
	mapPayload := map[string][]string{}
	//FilePath
	filename := "/opt/OtherTools/EazyH0j3n/EzpzShell/shell.txt"
	//Regex For Ip Address
	re := regexp.MustCompile(`(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}`)
	header()
	port := os.Args[2]
	options := os.Args[3]
	//Check if interfaces specify available
	ip := os.Args[1]
	checkerip := re.MatchString(ip)
	
	if checkerip != true {
		interfaces,err := net.InterfaceByName(ip)
		if err != nil {
			fmt.Println("The interface might not available! Check Again")
			os.Exit(1)
		}else{
			addr,err := interfaces.Addrs()
			if err != nil {
				fmt.Println("The interface might not available! Check again")
				os.Exit(1)
			}
			ip = re.FindAllString(addr[0].String(),-1)[0]
		}
	}
	fmt.Println(port)
	fmt.Println(options)
	fmt.Println(ip)
	//Read File
	fileBytes, err := ioutil.ReadFile(filename)
	if err != nil{
		fmt.Println(err)
		os.Exit(1)
	}
	//Split By #INDEX
	loadShell(mapPayload)
	sliceData := strings.Split(string(fileBytes), "#INDEX")[1:]
	fmt.Println(mapPayload)
	for _,data := range sliceData{
		mapPayload["py"] = append(mapPayload["py"],data)
	}
	for key, _ := range mapPayload {
	    	fmt.Println("Key:", key)
	}
	//fmt.Print(mapPayload["py"])

	
	
	
}
