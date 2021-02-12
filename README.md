![](https://github.com/H0j3n/EzpzShell/blob/main/demo.gif)

# What is EzpzShell?

Collection Of Reverse Shell that can easily generate using Python3 and Golang.


# How to use?

Please change the file path to `shell.txt` inside the code before doing the next step!

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

# Additional Information

If you want to add your reverse shell just customize `shell.txt` , `ezpzShell.py` or `ezpzShell.go`

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
* nodejs
	- Add Deserialization RCE (Only in Python)
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

# Todo

- Add Deserialization Node-js in Golang


# References

[1] http://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet

[2] https://highon.coffee/blog/reverse-shell-cheat-sheet/

[3] https://gist.github.com/Robleh/28234d9fe40e9baa1787396c7ad54350

[4] https://github.com/hoainam1989/training-application-security/blob/master/shell/node_shell.py

