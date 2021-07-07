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

    USAGE: gtfobins_finder.py -f filename.txt

