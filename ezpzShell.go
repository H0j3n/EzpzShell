package main

import (
	"fmt"
	"os"
	"net"
	"regexp"
)

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
}

func main(){
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
	
	
	
}
