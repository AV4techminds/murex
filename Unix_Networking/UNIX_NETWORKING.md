# Unix / Linux + Networking Topics List

## Purpose

Build a strong foundation in:

> Unix/Linux → Shell Scripting → Processes → Filesystems → Users/Security
> → Networking → Troubleshooting → Automation → Production Support

Learning approach:

> Concept → Command → Hands-on → Troubleshooting → Script → Real-world Scenario → Interview Questions → Glossary → Review

---

# PART A — UNIX / LINUX FUNDAMENTALS

## 01 — Unix/Linux Fundamentals

- [ ] What is Unix
- [ ] What is Linux
- [ ] Unix vs Linux
- [ ] Linux distributions
- [ ] Linux kernel
- [ ] Shell
- [ ] Terminal
- [ ] CLI
- [ ] GUI
- [ ] User space
- [ ] Kernel space
- [ ] System calls
- [ ] Linux architecture
- [ ] Boot process
- [ ] Login process
- [ ] Environment
- [ ] Hostname
- [ ] Machine/server concepts
- [ ] Client/server concepts

---

# 02 — Linux Filesystem

- [ ] Filesystem concept
- [ ] Root filesystem `/`
- [ ] `/bin`
- [ ] `/sbin`
- [ ] `/boot`
- [ ] `/dev`
- [ ] `/etc`
- [ ] `/home`
- [ ] `/lib`
- [ ] `/opt`
- [ ] `/proc`
- [ ] `/root`
- [ ] `/tmp`
- [ ] `/usr`
- [ ] `/var`
- [ ] `/run`
- [ ] `/mnt`
- [ ] `/media`
- [ ] Absolute path
- [ ] Relative path
- [ ] Current directory
- [ ] Parent directory
- [ ] Hidden files

---

# 03 — Essential Linux Commands

- [ ] `pwd`
- [ ] `ls`
- [ ] `cd`
- [ ] `mkdir`
- [ ] `rmdir`
- [ ] `touch`
- [ ] `cp`
- [ ] `mv`
- [ ] `rm`
- [ ] `cat`
- [ ] `less`
- [ ] `more`
- [ ] `head`
- [ ] `tail`
- [ ] `file`
- [ ] `stat`
- [ ] `clear`
- [ ] `history`
- [ ] `man`
- [ ] `which`
- [ ] `whereis`
- [ ] `type`

---

# 04 — File Permissions

- [ ] File permissions
- [ ] Read permission
- [ ] Write permission
- [ ] Execute permission
- [ ] Owner
- [ ] Group
- [ ] Others
- [ ] Permission notation
- [ ] Numeric permissions
- [ ] `chmod`
- [ ] `chown`
- [ ] `chgrp`
- [ ] Default permissions
- [ ] `umask`
- [ ] Special permissions
- [ ] SUID
- [ ] SGID
- [ ] Sticky bit
- [ ] Permission troubleshooting

---

# 05 — Users and Groups

- [ ] Users
- [ ] Groups
- [ ] User ID
- [ ] Group ID
- [ ] Root user
- [ ] `/etc/passwd`
- [ ] `/etc/shadow`
- [ ] `/etc/group`
- [ ] `/etc/sudoers`
- [ ] `who`
- [ ] `whoami`
- [ ] `id`
- [ ] `groups`
- [ ] `su`
- [ ] `sudo`
- [ ] `passwd`
- [ ] `useradd`
- [ ] `usermod`
- [ ] `userdel`
- [ ] `groupadd`
- [ ] `groupmod`
- [ ] `groupdel`

---

# 06 — Text Processing

- [ ] Standard input
- [ ] Standard output
- [ ] Standard error
- [ ] `stdin`
- [ ] `stdout`
- [ ] `stderr`
- [ ] `echo`
- [ ] `printf`
- [ ] `grep`
- [ ] `egrep`
- [ ] `cut`
- [ ] `sort`
- [ ] `uniq`
- [ ] `wc`
- [ ] `tr`
- [ ] `sed`
- [ ] `awk`
- [ ] `join`
- [ ] `paste`
- [ ] `xargs`
- [ ] Text filtering
- [ ] Text transformation
- [ ] Log analysis

---

# 07 — Pipes and Redirection

- [ ] Pipe `|`
- [ ] Output redirection `>`
- [ ] Append `>>`
- [ ] Input redirection `<`
- [ ] Error redirection `2>`
- [ ] Combined output
- [ ] `2>&1`
- [ ] `/dev/null`
- [ ] Command chaining
- [ ] `;`
- [ ] `&&`
- [ ] `||`
- [ ] Command substitution
- [ ] Backticks
- [ ] `$()`

---

# 08 — Search and File Discovery

- [ ] `find`
- [ ] `locate`
- [ ] `grep`
- [ ] Recursive search
- [ ] Search by filename
- [ ] Search by size
- [ ] Search by date
- [ ] Search by permissions
- [ ] Search by owner
- [ ] Search by content
- [ ] Combining `find` and `grep`
- [ ] Safe file deletion

---

# 09 — Processes

- [ ] Process concept
- [ ] PID
- [ ] PPID
- [ ] Parent process
- [ ] Child process
- [ ] Foreground process
- [ ] Background process
- [ ] Process states
- [ ] `ps`
- [ ] `top`
- [ ] `htop`
- [ ] `pgrep`
- [ ] `pkill`
- [ ] `kill`
- [ ] `killall`
- [ ] Signals
- [ ] SIGTERM
- [ ] SIGKILL
- [ ] SIGHUP
- [ ] SIGINT
- [ ] Process monitoring
- [ ] Zombie processes
- [ ] Orphan processes

---

# 10 — Jobs and Background Processing

- [ ] Background jobs
- [ ] `&`
- [ ] `jobs`
- [ ] `fg`
- [ ] `bg`
- [ ] `nohup`
- [ ] `disown`
- [ ] Session persistence
- [ ] Long-running processes

---

# 11 — CPU and Memory Monitoring

- [ ] CPU utilization
- [ ] Load average
- [ ] Memory
- [ ] RAM
- [ ] Swap
- [ ] Cache
- [ ] Buffer
- [ ] `free`
- [ ] `vmstat`
- [ ] `uptime`
- [ ] `top`
- [ ] `sar`
- [ ] CPU troubleshooting
- [ ] Memory troubleshooting
- [ ] High-load troubleshooting

---

# 12 — Disk and Storage

- [ ] Disk concepts
- [ ] Partition
- [ ] Filesystem
- [ ] Mount
- [ ] Unmount
- [ ] `df`
- [ ] `du`
- [ ] `mount`
- [ ] `umount`
- [ ] `lsblk`
- [ ] Disk usage analysis
- [ ] Inode
- [ ] Inode exhaustion
- [ ] Disk-full troubleshooting
- [ ] Large-file identification

---

# 13 — Archives and Compression

- [ ] `tar`
- [ ] `gzip`
- [ ] `gunzip`
- [ ] `zip`
- [ ] `unzip`
- [ ] Create archive
- [ ] Extract archive
- [ ] Compress files
- [ ] Decompress files
- [ ] Log archival
- [ ] Backup concepts

---

# 14 — Environment and Shell

- [ ] Environment variables
- [ ] Shell variables
- [ ] `PATH`
- [ ] `HOME`
- [ ] `USER`
- [ ] `SHELL`
- [ ] `PWD`
- [ ] `OLDPWD`
- [ ] `export`
- [ ] `env`
- [ ] `printenv`
- [ ] `.profile`
- [ ] `.bash_profile`
- [ ] `.bashrc`
- [ ] Shell startup
- [ ] Environment configuration

---

# PART B — SHELL SCRIPTING

# 15 — Shell Scripting Fundamentals

- [ ] What is shell scripting
- [ ] Bash
- [ ] Shell script structure
- [ ] Shebang
- [ ] Script permissions
- [ ] Executing scripts
- [ ] Variables
- [ ] Constants
- [ ] Comments
- [ ] Quoting
- [ ] Single quotes
- [ ] Double quotes
- [ ] Variable expansion
- [ ] Command substitution

---

# 16 — Shell Script Conditions

- [ ] `if`
- [ ] `elif`
- [ ] `else`
- [ ] `test`
- [ ] `[ ]`
- [ ] `[[ ]]`
- [ ] String comparison
- [ ] Numeric comparison
- [ ] File tests
- [ ] Directory tests
- [ ] Logical operators
- [ ] Nested conditions

---

# 17 — Shell Loops

- [ ] `for`
- [ ] `while`
- [ ] `until`
- [ ] Nested loops
- [ ] Loop control
- [ ] `break`
- [ ] `continue`
- [ ] Reading files line by line
- [ ] Processing command output

---

# 18 — Shell Functions

- [ ] Function definition
- [ ] Function parameters
- [ ] Return status
- [ ] Local variables
- [ ] Function reuse
- [ ] Function libraries
- [ ] Modular scripting

---

# 19 — Shell Script Arguments

- [ ] `$0`
- [ ] `$1`
- [ ] `$2`
- [ ] `$#`
- [ ] `$@`
- [ ] `$*`
- [ ] `$?`
- [ ] `$$`
- [ ] `$!`
- [ ] Positional parameters
- [ ] Argument validation
- [ ] Usage messages

---

# 20 — Shell Script Exit Codes

- [ ] Exit status
- [ ] `$?`
- [ ] `exit`
- [ ] Success
- [ ] Failure
- [ ] Error propagation
- [ ] Return codes
- [ ] Error handling
- [ ] Controller scripts

---

# 21 — Shell Script Input and Output

- [ ] `read`
- [ ] User input
- [ ] File input
- [ ] Standard output
- [ ] Standard error
- [ ] Logging
- [ ] Redirecting output
- [ ] Temporary files

---

# 22 — Shell Script Production Standards

- [ ] Naming conventions
- [ ] Script structure
- [ ] Header comments
- [ ] Usage instructions
- [ ] Input validation
- [ ] Error handling
- [ ] Exit codes
- [ ] Logging
- [ ] Lock files
- [ ] Temporary directories
- [ ] Cleanup
- [ ] Signal handling
- [ ] Idempotency
- [ ] Safe execution
- [ ] ShellCheck concepts
- [ ] Code review

---

# 23 — Scheduling and Batch Processing

- [ ] `cron`
- [ ] `crontab`
- [ ] Cron syntax
- [ ] Environment differences in cron
- [ ] Scheduling scripts
- [ ] Batch jobs
- [ ] Job dependencies
- [ ] `at`
- [ ] Job monitoring
- [ ] Failed job handling
- [ ] Retry
- [ ] Recovery

---

# 24 — Linux Services

- [ ] Service concept
- [ ] Daemon
- [ ] `systemctl`
- [ ] Start service
- [ ] Stop service
- [ ] Restart service
- [ ] Enable service
- [ ] Disable service
- [ ] Service status
- [ ] Service logs
- [ ] `journalctl`
- [ ] Service troubleshooting

---

# 25 — Linux Logs

- [ ] System logs
- [ ] Application logs
- [ ] Authentication logs
- [ ] Log locations
- [ ] Log rotation
- [ ] `journalctl`
- [ ] `tail -f`
- [ ] `grep`
- [ ] `awk`
- [ ] `sed`
- [ ] Log filtering
- [ ] Error identification
- [ ] Incident investigation

---

# 26 — File Transfer

- [ ] FTP concepts
- [ ] SFTP
- [ ] SCP
- [ ] SSH
- [ ] File upload
- [ ] File download
- [ ] Authentication
- [ ] SSH keys
- [ ] Public key
- [ ] Private key
- [ ] Host key
- [ ] Known hosts
- [ ] Permissions
- [ ] Transfer failures
- [ ] File integrity
- [ ] Archive after transfer

---

# 27 — SSH

- [ ] SSH concepts
- [ ] SSH connection
- [ ] Hostname
- [ ] IP address
- [ ] Port
- [ ] Username
- [ ] Password authentication
- [ ] Key-based authentication
- [ ] SSH keys
- [ ] `ssh`
- [ ] `scp`
- [ ] `sftp`
- [ ] SSH troubleshooting
- [ ] SSH timeout
- [ ] Permission denied
- [ ] Host key issues

---

# PART C — NETWORKING FUNDAMENTALS

# 28 — Networking Basics

- [ ] What is networking
- [ ] Network
- [ ] Host
- [ ] Client
- [ ] Server
- [ ] LAN
- [ ] WAN
- [ ] Internet
- [ ] Intranet
- [ ] Network interface
- [ ] MAC address
- [ ] IP address
- [ ] Port
- [ ] Protocol
- [ ] Packet
- [ ] Frame

---

# 29 — OSI Model

- [ ] OSI model
- [ ] Layer 1 — Physical
- [ ] Layer 2 — Data Link
- [ ] Layer 3 — Network
- [ ] Layer 4 — Transport
- [ ] Layer 5 — Session
- [ ] Layer 6 — Presentation
- [ ] Layer 7 — Application
- [ ] Protocol examples by layer
- [ ] Troubleshooting using OSI layers

---

# 30 — TCP/IP Model

- [ ] TCP/IP model
- [ ] Network access layer
- [ ] Internet layer
- [ ] Transport layer
- [ ] Application layer
- [ ] OSI vs TCP/IP

---

# 31 — IP Addressing

- [ ] IPv4
- [ ] IPv6
- [ ] Public IP
- [ ] Private IP
- [ ] Loopback
- [ ] `127.0.0.1`
- [ ] `0.0.0.0`
- [ ] Network address
- [ ] Broadcast address
- [ ] Subnet
- [ ] Subnet mask
- [ ] CIDR
- [ ] Default gateway
- [ ] Network prefix
- [ ] Host portion

---

# 32 — Subnetting

- [ ] Subnet concept
- [ ] Subnet mask
- [ ] CIDR notation
- [ ] `/8`
- [ ] `/16`
- [ ] `/24`
- [ ] `/32`
- [ ] Network calculation
- [ ] Host calculation
- [ ] Address ranges
- [ ] Subnetting practice

---

# 33 — TCP and UDP

- [ ] TCP
- [ ] UDP
- [ ] Connection-oriented
- [ ] Connectionless
- [ ] Reliability
- [ ] Ordering
- [ ] Flow control
- [ ] Congestion control
- [ ] TCP handshake
- [ ] SYN
- [ ] SYN-ACK
- [ ] ACK
- [ ] TCP termination
- [ ] FIN
- [ ] RST
- [ ] UDP use cases
- [ ] TCP vs UDP

---

# 34 — Ports and Sockets

- [ ] Port concept
- [ ] Well-known ports
- [ ] Registered ports
- [ ] Dynamic ports
- [ ] Source port
- [ ] Destination port
- [ ] Socket
- [ ] IP + port
- [ ] Listening port
- [ ] Connection
- [ ] Port troubleshooting

---

# 35 — Common Network Protocols

- [ ] HTTP
- [ ] HTTPS
- [ ] SSH
- [ ] SFTP
- [ ] FTP
- [ ] SMTP
- [ ] DNS
- [ ] DHCP
- [ ] NTP
- [ ] ICMP
- [ ] TCP
- [ ] UDP
- [ ] TLS

---

# 36 — DNS

- [ ] DNS concept
- [ ] Domain name
- [ ] Hostname
- [ ] Resolver
- [ ] DNS server
- [ ] DNS lookup
- [ ] A record
- [ ] AAAA record
- [ ] CNAME
- [ ] MX
- [ ] PTR
- [ ] TXT
- [ ] Forward lookup
- [ ] Reverse lookup
- [ ] DNS caching
- [ ] DNS troubleshooting
- [ ] `nslookup`
- [ ] `dig`
- [ ] `host`

---

# 37 — Routing

- [ ] Routing concept
- [ ] Router
- [ ] Routing table
- [ ] Default route
- [ ] Gateway
- [ ] Static route
- [ ] Dynamic routing concepts
- [ ] Route selection
- [ ] Network path
- [ ] `ip route`
- [ ] `route`
- [ ] Routing troubleshooting

---

# 38 — Network Interfaces

- [ ] Network interface
- [ ] Ethernet
- [ ] Virtual interface
- [ ] Loopback interface
- [ ] Interface IP
- [ ] Interface status
- [ ] `ip addr`
- [ ] `ip link`
- [ ] Interface troubleshooting
- [ ] Network configuration

---

# 39 — Network Troubleshooting Commands

- [ ] `ping`
- [ ] `traceroute`
- [ ] `tracepath`
- [ ] `ip`
- [ ] `ss`
- [ ] `netstat`
- [ ] `nslookup`
- [ ] `dig`
- [ ] `host`
- [ ] `curl`
- [ ] `wget`
- [ ] `telnet`
- [ ] `nc`
- [ ] `tcpdump`
- [ ] `lsof`
- [ ] `arp`
- [ ] `mtr`

---

# 40 — Network Connectivity Troubleshooting

- [ ] Host unreachable
- [ ] Network unreachable
- [ ] DNS failure
- [ ] Port unreachable
- [ ] Connection refused
- [ ] Connection timeout
- [ ] Connection reset
- [ ] Authentication failure
- [ ] Firewall blocking
- [ ] Routing problem
- [ ] Application problem
- [ ] Server availability
- [ ] Client availability
- [ ] Packet loss
- [ ] Latency
- [ ] Intermittent connectivity

---

# 41 — HTTP Troubleshooting

- [ ] HTTP request
- [ ] HTTP response
- [ ] Status codes
- [ ] 2xx
- [ ] 3xx
- [ ] 4xx
- [ ] 5xx
- [ ] HTTP headers
- [ ] Request timeout
- [ ] Connection timeout
- [ ] SSL/TLS issues
- [ ] Certificate issues
- [ ] Proxy issues
- [ ] API connectivity testing
- [ ] `curl` troubleshooting

---

# 42 — TLS / SSL Fundamentals

- [ ] Encryption concept
- [ ] TLS
- [ ] SSL terminology
- [ ] Certificate
- [ ] Certificate authority
- [ ] Public key
- [ ] Private key
- [ ] Certificate chain
- [ ] Trust store
- [ ] Expired certificate
- [ ] Hostname mismatch
- [ ] TLS handshake
- [ ] TLS troubleshooting
- [ ] `openssl` basics

---

# 43 — Firewalls and Security Basics

- [ ] Firewall concept
- [ ] Inbound traffic
- [ ] Outbound traffic
- [ ] Port filtering
- [ ] Network security
- [ ] Host firewall
- [ ] Firewall rules
- [ ] `iptables` concepts
- [ ] `firewalld` concepts
- [ ] Security groups concepts
- [ ] Troubleshooting blocked ports

---

# 44 — Proxy Concepts

- [ ] Proxy
- [ ] Forward proxy
- [ ] Reverse proxy
- [ ] HTTP proxy
- [ ] HTTPS proxy
- [ ] Proxy environment variables
- [ ] Authentication
- [ ] Proxy troubleshooting

---

# 45 — Load Balancing Concepts

- [ ] Load balancer
- [ ] Client
- [ ] Load balancer
- [ ] Backend servers
- [ ] Health checks
- [ ] Active/standby
- [ ] Round robin
- [ ] Session persistence
- [ ] Failover
- [ ] Load-balancer troubleshooting

---

# PART D — PRODUCTION SUPPORT

# 46 — Linux Production Support

- [ ] Server health check
- [ ] CPU check
- [ ] Memory check
- [ ] Disk check
- [ ] Process check
- [ ] Service check
- [ ] Log check
- [ ] Network check
- [ ] User/permission check
- [ ] File-system check
- [ ] Batch-job check

---

# 47 — Batch Job Troubleshooting

- [ ] Job started?
- [ ] Job completed?
- [ ] Process running?
- [ ] Exit code
- [ ] Input file available?
- [ ] Input file complete?
- [ ] Permissions correct?
- [ ] Disk space available?
- [ ] Database available?
- [ ] Network available?
- [ ] Dependent service available?
- [ ] Log analysis
- [ ] Retry
- [ ] Recovery
- [ ] Reconciliation

---

# 48 — File-Based Integration Troubleshooting

- [ ] File missing
- [ ] File delayed
- [ ] File empty
- [ ] File incomplete
- [ ] Duplicate file
- [ ] Incorrect filename
- [ ] Incorrect permissions
- [ ] Incorrect format
- [ ] Invalid records
- [ ] File transfer failure
- [ ] Archive failure
- [ ] Processing failure
- [ ] Recovery procedure

---

# 49 — Linux + Python Integration

- [ ] Execute Python from shell
- [ ] Pass arguments
- [ ] Environment variables
- [ ] Capture exit codes
- [ ] Capture stdout
- [ ] Capture stderr
- [ ] Log Python execution
- [ ] Shell controller
- [ ] Python worker
- [ ] Error propagation
- [ ] Retry
- [ ] Batch automation

---

# 50 — Linux + Oracle Integration

- [ ] Oracle client concepts
- [ ] Environment configuration
- [ ] Database connectivity
- [ ] Connection testing
- [ ] SQL execution
- [ ] Batch scripts
- [ ] Database health checks
- [ ] Query execution from shell
- [ ] Error handling
- [ ] Transaction concepts
- [ ] Monitoring

---

# 51 — Linux + Murex-Relevant Operations

- [ ] Murex application/server concepts
- [ ] Application processes
- [ ] Batch processing
- [ ] Scheduler concepts
- [ ] Input files
- [ ] Output files
- [ ] Logs
- [ ] Database connectivity
- [ ] File-based integration
- [ ] Network-based integration
- [ ] SFTP integration
- [ ] XML processing
- [ ] Trade processing support
- [ ] Error investigation
- [ ] Reconciliation
- [ ] Restart/recovery concepts
- [ ] Production incident troubleshooting

---

# 52 — Troubleshooting Methodology

- [ ] Understand the symptom
- [ ] Identify scope
- [ ] Check recent changes
- [ ] Check logs
- [ ] Check process
- [ ] Check service
- [ ] Check filesystem
- [ ] Check CPU
- [ ] Check memory
- [ ] Check network
- [ ] Check database
- [ ] Identify root cause
- [ ] Apply fix
- [ ] Validate
- [ ] Monitor
- [ ] Document
- [ ] Prevent recurrence

---

# 53 — Interview Preparation

## Unix/Linux

- [ ] Linux fundamentals
- [ ] Filesystem
- [ ] Permissions
- [ ] Users/groups
- [ ] Processes
- [ ] Memory
- [ ] CPU
- [ ] Disk
- [ ] Shell scripting
- [ ] Cron
- [ ] Logs
- [ ] SSH
- [ ] SFTP
- [ ] Production troubleshooting

## Networking

- [ ] OSI
- [ ] TCP/IP
- [ ] IP addressing
- [ ] Subnetting
- [ ] TCP
- [ ] UDP
- [ ] Ports
- [ ] DNS
- [ ] Routing
- [ ] HTTP
- [ ] HTTPS
- [ ] TLS
- [ ] Firewall
- [ ] Proxy
- [ ] Load balancer
- [ ] Network troubleshooting

## Scenario Questions

- [ ] Application is down
- [ ] Server is slow
- [ ] CPU is high
- [ ] Memory is high
- [ ] Disk is full
- [ ] File is missing
- [ ] File transfer failed
- [ ] SFTP connection failed
- [ ] Database connection failed
- [ ] Port is unreachable
- [ ] DNS is not resolving
- [ ] API is timing out
- [ ] Process is stuck
- [ ] Batch job failed
- [ ] Cron job did not execute
- [ ] Permission denied
- [ ] SSL certificate failure
- [ ] Intermittent network failure

---

# 54 — Practical Labs

## Lab 01 — Linux Fundamentals

- [ ] Navigate filesystem
- [ ] Create files
- [ ] Modify files
- [ ] Copy files
- [ ] Move files
- [ ] Delete files
- [ ] Search files

## Lab 02 — Permissions

- [ ] Create users
- [ ] Create groups
- [ ] Change ownership
- [ ] Change permissions
- [ ] Test access

## Lab 03 — Log Analysis

- [ ] Generate sample log
- [ ] Search errors
- [ ] Filter timestamps
- [ ] Count errors
- [ ] Generate report

## Lab 04 — Shell Automation

- [ ] Input validation
- [ ] File processing
- [ ] Logging
- [ ] Exit codes
- [ ] Error handling

## Lab 05 — Network Troubleshooting

- [ ] Ping host
- [ ] Resolve DNS
- [ ] Check port
- [ ] Trace route
- [ ] Inspect connections
- [ ] Test HTTP endpoint

## Lab 06 — File Transfer

- [ ] SSH
- [ ] SCP
- [ ] SFTP
- [ ] Upload
- [ ] Download
- [ ] Validate file
- [ ] Archive file

## Lab 07 — End-to-End Automation

Input File
→ Shell Controller
→ Python Processing
→ Oracle
→ Validation
→ Output File
→ Archive
→ Logging
→ Error Handling
→ Recovery

---

# Completion Criteria

A topic is COMPLETE only when:

- [ ] Concept understood
- [ ] Command understood
- [ ] Command executed
- [ ] Hands-on practice completed
- [ ] Failure scenario tested
- [ ] Troubleshooting understood
- [ ] Notes prepared
- [ ] Glossary updated
- [ ] Interview questions answered
- [ ] Git commit completed

---

# Daily Learning Rule

Do not memorize commands blindly.

Use:

> Understand → Execute → Break → Troubleshoot → Automate → Explain → Document

---

# Final Goal

Be able to troubleshoot a production-style issue using:

Linux
+
Shell Script
+
Networking
+
Python
+
Oracle
+
File Transfer
+
Logs
+
Batch Processing
+
Murex Integration Concepts

and explain the complete troubleshooting path confidently in an interview.
