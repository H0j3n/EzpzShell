//////////////////////////////////////////////////////////////////////
//Script Name	: EzpzShell
//Description	: Collection Of Reverse Shell that can easily generate
//Author       	: H0j3n
//Twitter       : @h0j3n
//Github Link   : https://github.com/H0j3n/EzpzShell
//////////////////////////////////////////////////////////////////////

//Important
#![allow(unused_imports)]
#![allow(warnings)]

//Color Definition
extern crate termion;
use termion::{color,style};
//Arguments
use std::env;
//Process
use std::process;
//Networks
extern crate ifaces;
//Regex
use regex::Regex;
//Read File
use std::fs::File;
use std::io::{Write, BufReader, BufRead, Error};

//Header Function (Receives Vector String)
//fn header(args: &Vec<String>) {

fn header() {
	let s = r#"
  ______               _____ _          _ _ 
 |  ____|             / ____| |        | | |
 | |__   _____ __ ___| (___ | |__   ___| | |
 |  __| |_  / '_ \_  /\___ \| '_ \ / _ \ | |
 | |____ / /| |_) / / ____) | | | |  __/ | |
 |______/___| .__/___|_____/|_| |_|\___|_|_|
            | |                             
            |_|
"#;
	println!("{}\n{}[Payload Available]{}\npy,py3,bash,c,nc,php,perl,ruby,haskell,powershell,nodejs,awk,ncat,exe,ssti,cgibin,jenkins,tarpriv,pickle,java,lua,asp,xxe,jsp\n\n{}[Usage]\n{}ezpzShell 10.10.10.10 9001 py\nezpzShell tun0 9001 py{}", s,color::Fg(color::LightGreen),color::Fg(color::Reset),color::Fg(color::LightGreen),color::Fg(color::Yellow),color::Fg(color::Reset));
}

//Listen Function (Credits : https://stackoverflow.com/questions/61297668/how-to-interact-with-a-reverse-shell-in-rust)
fn pipe_thread<R, W>(mut r: R, mut w: W) -> std::thread::JoinHandle<()>
where R: std::io::Read + Send + 'static,
      W: std::io::Write + Send + 'static
{
    std::thread::spawn(move || {
        let mut buffer = [0; 1024];
        loop {
            let len = r.read(&mut buffer).unwrap();
            if len == 0 {
                break;
            }
            w.write(&buffer[..len]).unwrap();
            w.flush().unwrap();
        }
    })
}

fn listen(port: u16) {
   let x = std::net::TcpListener::bind(("0.0.0.0", port)).unwrap();
   let (mut stream, _) = x.accept().unwrap();
   let t1 = pipe_thread(std::io::stdin(), stream.try_clone().unwrap());
   let t2 = pipe_thread(stream, std::io::stdout());
   t1.join();
   t2.join();
}

fn main() -> Result<(), Error>{
    //Arguments (Vector Strings)
    let args: Vec<String> = env::args().collect();
    header();
    //Check Length Arguments (Must
    if ((args.len() - 1) < 3){
    	process::exit(1);
    }
    //Setup Ip,Port,Options
    let mut ip = args[1].to_string();
    let port = &args[2];
    let options = &args[3];
    //Get List Network Interface IP
    for iface in
        ifaces::Interface::get_all().unwrap()
            .into_iter() {
                //println!("{}\t{:?}\t{:?}", iface.name, iface.kind, iface.addr);
                let tempKind = format!("{:?}",iface.kind);  
                let tempaddr = format!("{:?}",iface.addr); 
                let len = tempaddr.len() - 3;
                if (ip.eq(&iface.name) && (tempKind.eq("Ipv4"))){
                	let mut slice = &tempaddr[5..len];    
                	ip = slice.to_string();
                }
            }
    //Check IP Valid or Not
    let re = Regex::new(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$").unwrap();
    if !(re.is_match(&ip)){
    	println!("\nCheck if IP is valid!");
    	process::exit(1);
    }
    //Read File
    let path = "/opt/Others/EzpzShell/shell.txt";
    let input = File::open(path)?;
    let buffered = BufReader::new(input);
    let mut files = String::new();
    for line in buffered.lines() {
    	let tempFiles = format!("{:?}",line?); 
    	//Replacing \t, \', \"
    	let tempFiles2 = str::replace(&tempFiles, r#"\t"#, r#""#);
    	let tempFiles3 = str::replace(&tempFiles2, r#"\'"#, r#"'"#);
    	let tempFiles4 = str::replace(&tempFiles3, r#"\""#, r#"""#);
    	let len = tempFiles4.len() - 1;
        files += &tempFiles4.to_string()[1..len];
        files += "\n";
    }
    //Store the Payload Options EzpzShell Has
    let mut cmpIndex = -1;
    match options.as_str(){
    	"py" => cmpIndex=0,
    	"py3" => cmpIndex=1,
    	"bash" => cmpIndex=2,
	"c"=> cmpIndex=3,
	"nc"=> cmpIndex=4,
	"php"=> cmpIndex=5,
	"perl"=> cmpIndex=6,
	"ruby"=> cmpIndex=7,
	"haskell"=> cmpIndex=8,
	"powershell"=> cmpIndex=9,
	"nodejs"=> cmpIndex=10,
	"awk"=> cmpIndex=11,
	"ncat"=> cmpIndex=12,
	"exe"=> cmpIndex=13,
	"ssti"=> cmpIndex=14,
	"cgibin"=> cmpIndex=15,
	"jenkins"=> cmpIndex=16,
	"tarpriv"=> cmpIndex=17,
	"pickle"=> cmpIndex=18,
	"java"=> cmpIndex=19,
	"lua"=> cmpIndex=20,
	"asp"=> cmpIndex=21,
	"xxe"=> cmpIndex=22,
	"jsp"=> cmpIndex=23,
    	_ => cmpIndex=-1
    }
    //Split By #INDEX
    if cmpIndex == -1{
    	println!("\nOptions Not Found!");
    	process::exit(1);
    }
    
    let mut index = 0;
    for part in files.split("#INDEX").skip(1) {
    	let mut part = part.replace("{IP}",&ip);
    	part = part.replace("{PORT}",&port);
    	if index == cmpIndex{
    		let mut counter = 0;
    		for part2 in part.split("#EXAMPLE").skip(1){
    			println!("\n{}EXAMPLE {}{}",color::Fg(color::LightGreen),counter+1,color::Fg(color::Reset));
    			println!("\n{}", part2.trim());
    			counter = counter + 1;
    		}
    	    
    	}
    	index = index +1;
    }
    //Listen to Port
    println!("\n{}[*]{} Starting the listener on port {}",color::Fg(color::LightGreen),color::Fg(color::Reset),port);
    listen(port.parse::<u16>().unwrap());
    Ok(())
   }
