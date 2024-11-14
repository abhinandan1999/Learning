## Package Management

There are mainly two types of packages: <br>
    1) Debian Style (.deb): Debian, Ubuntu, Linux Mint, Raspbian <br>
    2) Red Hat Style (.rpm): Fedora, CentOS,  Red hat Enterprise

Package Management usually consists of two type of tools: <br>
    1) Low level tools: which handles tasks of installing and removing package files <br>
    2) High level tools: That searches metadata searching and dependency resolutions


|Distributions                              | Low level tools | High Level tools       |
|:-----------------------------------------:|:---------------:|:----------------------:|
| Debian Style                              |     dpkg        | apt, apt-get, aptitude |          
| Fedora, Red hat, Enterprise Linux, CentOS |     rpm         |      yum, dnf          |

<br> </br>
* Find a package in repository
```
apt-get update; apt-cache search <search_string>
```
```
yum search <search_string>
```

* To install a package:
```
apt-get update; apt-get install <package_name>
```
```
yum install <package_name>
```

* If the package has been downloaded from source other than repository, it can be installed using low level tool:
```
dpkg -i <package_name>
```
```
rpm -i <package_name>
```
Note: dpkg does not install the dependencies on it own.
If install fails after running dpkg command, then run the following command
```
sudo apt-get -f install
```

* To remove a package
```
apt-get remove <package_name>
```
```
yum erase <package_name>
```

* To update a package
```
apt-get update; apt-get upgrade
```
```
yum update
```

* Listing all installed packages
```
dpkg -l
```
```
rpm -qa
```

* Determine if package is installed
```
dpkg -s <package_name>
```
```
dpkg --status <package_name>
```
```
rpm -q <package_name>
```

* Display information about package name
```
apt-cache show <package_name>
```
```
yum info <package_name>
```

* To find which package installed a file
```
dpkg -S <file_name>
```
```
rpm -qf <file_name>
```
Ex: ```dpkg -S /usr/bin/vim```




## Storage Media

* Viewing a list of mounted file system <br>
It is used to mount filesystem. Without any arguments it will display all the mounted filesystem
```
mount
``` 


* To Unmount
```
unmount <device_name>
```

* To mount to a specific directory
```
mkdir /mnt/cdrom
mount -t iso9600 <device_name> <path_to_mount>
```

#### Creating a new filesystem disks
* fdisk is one of a host of programs (both command line and graphical) that allow us to
interact directly with disk-like devices (such as hard disk drives and flash drives) at a
very low level. With this tool we can edit, delete, and create partitions on the device. To
work with our flash drive, we must first *unmount* it (if needed) and then invoke the
fdisk program as follows:

```
sudo fdisk <device_name>
```
```
sudo mkfs -t ext4 [<filesystem_name>] /dev/sdb1 [<device_name>]
```

* To Test and Repair filesystems
```
sudo fsck <device_name>
```

* Moving data directly to and from Devices
```
dd if=input_file of=output_file [bs=block_size [count=blocks]]
```
```
dd if=/dev/sdb of=/dev/sdc
```

## Networking

**Internet Protocol (IP) address:**
An Internet Protocol (IP) address is a unique numerical identifier for every device or network that connects to the internet. Typically assigned by an internet service provider (ISP), an IP address is an online device address used for communicating across the internet.

**Port:**
A port name, or simply a port, is a numerical identifier used to specify a specific process or service running on a device. 

**Host and Domain Name:**
A host name is a unique label for a device within a local network, while a domain name is a user-friendly and hierarchical naming system used to identify resources (websites, servers, etc.) on the internet. Domain names make it easier for users to access internet resources without having to remember complex IP addresses.


#### Examining and Monitoring a network
* The ping command sends a special network packet called an ICMP ECHO_REQUEST to a specified host. 
Most network devices receiving this packet will reply to it, allowing the network connection to be verified.
```
ping <host_name>
``` 
 
* The traceroute program (some systems use the similar tracepath program instead) lists all the “hops” network traffic takes to get from the local system to a specified host
```
traceroute 
```


* With ip, we can examine a system's network interfaces and routing table.
```
ip a
```

* The netstat program is used to examine various network settings and statistics.
```
netstat -ie
```



#### Transporting Files Over a Network
* ftp is used to transfer file over the network.
```
ftp <remoter-server-name or ip address>
```

* lftp works much like the traditional ftp program but has many additional convenience features including multipleprotocol support (including HTTP), automatic retry on failed downloads, background processes, tab completion of path names, and many more.
```
lftp <remoter-server-name or ip address>
```

* wget is useful for downloading content from both web and FTP sites.
```
wget
``` 

#### Secure Communication with Remote Hosts
* The SSH client program used to connect to remote SSH servers. By default it listens on Port 22
```
ssh <remote-server-name or ip address>
```
```
ssh <username@remote-server-name or ip address>
```

* Scp is used to copy the files from remotehost to local machines.
```
scp <remoter-server-name:path_in_server> <path_in_local>
```
```
scp <username@remoter-server-name:path_in_server> <path_in_local>
```


* sftp is used same as ftp only in more secure way.
```
sftp <remote-server-name or ip address>
```


## Searching for Files

```
locate  <substring>
```
The locate program performs a rapid database search of pathnames, and then outputs every name that matches a given substring

```
find <directory_name>
```
```
find <directory_name> -type [d, f] -name <pattern_of_filename> -size <+1M>
```
find program searches a given directory (and its subdirectories) for files based on a variety of attributes


Find with Operators and actions
```
find <directory_name> (expression1) <logical-operator> (expression2) <actions>
```
```
<logical-operator>: [-and, -or, -not]
```
```
Expression1: \(-type d -and -not -perm 0600 \)
```
Note: Backslash is used as parentheses have special meaning to shell. 
```
Actions: -print, -delete, 
```

Find with USER DEFINED actions
```
find <directory_name> -exec <command> '{}' ';'
```
```
Commands: ls, rm, etc
```
*'{}': represents current path obtained using find, quotes are put as braces have special meaning to shell* <br>
*';': represents end of command.*

Used to create empty file and change file times
```
touch <filename>
```

Display file or filesystem status
```
stat <filename>
```


## Archiving and Backup [TO DO]

Compressing files
gzip <options> <file1> <file2>
Gzip program is used to compress one or more files.
Options: -c: Write output to stdout
                -d: Decompress the file
                -f: Force compression, if compress version already exists
                -h: Display usage information
                -l: List compressed statistics for each file compressed
                -r: If one more command line is a directory, recursively compress file contained within them
                -t: Test the integrity of a compressed file
                -v: Display verbose message while compressing
               -number: Set amount of compression. 1(fast) and 9(slowest)

bzip2 <Options> <ffile1> <file2>
Bzip2 works in similar way as gzip, but with higher compression and in slower time.

Archiving files
tar mode[options] <tarfile> <pathname>
<tarfile>: name of archived file. Somename.tar
Modes:
    1) c: Creates an archive from list of files and directories
    2) x: Extract and archive
    3) r: Append specified pathname to end of an archive
    4) t: List the content of an archive

Options:
    1) f: To specify the file

zip options zipfile file …
This is used to zip the file with name <zipfile.zip>.

unzip <zipfile>
This will unzip the file

Synchronizing Files and Directories 
rsync options source destination
where source and destination are one of the following:
    • A local file or directory 
    • A remote file or directory in the form of [user@]host:path 
    • A remote rsync server specified with a URI of rsync://[user@]host[:port]/path 
This program can synchronize both local and remote directories by using the rsync remote-update protocol, which allows rsync to quickly detect the differences between two directories and perform the minimum amount of copying required to bring them into sync. 