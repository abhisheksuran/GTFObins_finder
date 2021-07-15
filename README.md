#GTFObins


                            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                            @@@@@@@@@@%%%@@@@@%%%@@@@@@@@@
                            @@@@@@%%%%%%%%%%%%%%%%%%@@@@@@
                            @@@@@@@@@@%%%@@@@@%%%@@@@@@@@@
                            @@@@@@@@@@%%%@@@@@%%%@@@@@@@@@
                            @@@@@@%%%%%%%%%%%%%%%%%%@@@@@@
                            @@@@@@%%%%%%%%%%%%%%%%%%@@@@@@
                            @@@@@@@@@@%%%@@@@@%%%@@@@@@@@@
                            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

    This script takes a text file as an input which contains the output of command

    find / -type f -a \( -perm -u+s -o -perm -g+s \) -exec ls -l {} \; 2> /dev/null

    This script search for the bin on the https://gtfobins.github.io/ for the SUID exploit
    and returns the bins that have exploit available on gtfobins.

    USAGE: python3 gtfobins_finder.py -f filename.txt


##Description
1) This is a python3 script.
2) This script automates the process of finding SUID bins on the gtfobins.github.io, so you don't have to manually search every bin one by one.
3) Finds bins only with SUID available on gftobins.
4) Bins.txt is available for your reference.

##Usage 
1) Run ```find / -type f -a \( -perm -u+s -o -perm -g+s \) -exec ls -l {} \; 2> /dev/null``` on target machine.
2) Copy the output from terminal to a text file.
3) Run ``` python3 gtfobins_finder.py -f filename.txt```