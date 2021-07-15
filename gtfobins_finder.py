#! /bin/python
import sys
from lxml import html
import requests
import argparse
#from requests.exceptions import HTTPError

def main(txt_file):

    '''
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
         '''

    all_bins = []

    try:
        with open(txt_file, "r") as bins:
            for lines in bins.readlines():
                b = lines.split(' ')[-1].split('/')[-1].strip('\n')
                all_bins.append(b)

        #print(all_bins)

    except Exception:
        print(FileNotFoundError)
        sys.exit()

    ok_status = []
    all_status = []
    for bins in all_bins:

        try:
            status = requests.get(f"https://gtfobins.github.io/gtfobins/{bins}/")
            site_content = status.text
            site_content = html.document_fromstring(site_content)
            id = [e.text_content() for e in site_content.xpath("//h2[@id = 'suid']")]
            all_status.append(status)

            if status.status_code == 200 and len(id) > 0:
                ok_status.append(bins)

        except Exception:
            print("************** KINDLY CHECK THE INTERNET CONNECTIVITY **************")
            sys.exit()


    if len(ok_status) >0:
        print("[+] FOLLOWING BINS ARE AVAILABLE FOR THE SUID [+]")
        for b in ok_status:
            print(f'> {b}')
    else:
        print("[-] NO BINS AVAILBLE FOR THE SUID ON GTFOBINS [-]")

    #print(ok_status)
    #print(all_status)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=print(main.__doc__))
    parser.add_argument('-f', type=str, required=True, metavar='string_value', help="KINDY PROVIDE A TXT FILE containing info as described above")
    args = parser.parse_args()
    bin_file = args.f
    if bin_file.endswith('.txt'):
        main(bin_file)
    else:
        print("********* KINDLY PROVIDE TXT FILE WITH '.txt' EXTENSION *********")
