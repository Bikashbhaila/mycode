#!/usr/bin/env python3

# open file in read mode
with  open("dnsservers.txt", "r") as dnsfile:
    # indent to keep the dns object open
    # loop over lines
    for line in dnsfile:
        line = line.rstrip("\n") # remove new line char if exists
        
        # if the line ends with org, append to org-domain.txt or com-domain.txt (not write as it will override previous)
        if line.endswith("org"):
            with open("org-domain.txt", "a") as srvfile:
                srvfile.write(line + "\n")
        elif line.endswith("com"):
            with open("com-domain.txt", "a") as srvfile:
                srvfile.write(line + "\n")
        # print and end without a newline
       # print(line, end="")
# no need to close out file - closed automatically once once indentation ends
# dnsfile.close()
