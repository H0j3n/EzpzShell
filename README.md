![](https://github.com/H0j3n/EzpzShell/blob/main/demo.gif)

# What is EzpzShell?

Collection Of Reverse Shell that can easily generate using different Programming Language. Currently support in Python3 and Golang but will spend my time on others Programming Language. This repo is for my own educational purpose and I would like to refer back in future. Thank you!

**_Disclaimer: Do not use this script for illegal use. Any action you take upon the information on this repo is strictly at your own risk**

# How to use?

Please change the file path to `shell.txt` inside the code before doing the next step!

# Extra!!

Please check https://github.com/0dayCTF/reverse-shell-generator which you can check https://www.revshells.com/ 

```
Hosted Reverse Shell generator with a ton of functionality. -- (Great for CTFs) and really nice UI!
```

## Python

Specify the IP, Port and the options that are available.

```python
python3 ezpzShell.py 10.10.10.10 9001 py
```

Or just specify the interface that you want to use.

```python
python3 ezpzShell.py tun0 9001 py
```

## Golang

Build it first and specify the IP, Port and the options that are available.

```go
go build
EzpzShell 10.10.10.10 9001 py
```

Or just specify the interface that you want to use.

```go
go build
EzpzShell tun0 9001 py
```

## Rust (Still In Progress)

To install Rust you can check on this link and install the below dependencies needed

* https://www.techrepublic.com/article/how-to-install-rust-on-linux/

```
* sudo apt install libdbus-glib-1-dev
```

To run in rust way you can use this command

```rs
cd rust
cargo build --release

* The binary will located in `rust/target/release`
```

# Additional Information

If you want to add your reverse shell just customize `shell.txt` , `ezpzShell.py` , `ezpzShell.go` or `main.rs`

# Reverse Shell Available

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
* exe
* ssti
* cgi-bin
* jenkins
* tar-priv
* pickle (not supported in Go)
* java
* lua
* asp
* xxe
* jsp
* c#

# Todo

* Trying to develop in Rust while learning it.
* Base64 in rust

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
