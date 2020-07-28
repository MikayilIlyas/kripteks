import hashlib
import datetime
import sys
import os
import getopt
import enc
import dec
import cw_loj


# Coding for Cyber-Warrior.org
# this is not coded for use of GAVURS



def operation():
    banner = """ \33[31m \33[1m                             

    ██╗  ██╗██████╗ ██╗██████╗ ████████╗███████╗██╗  ██╗███████╗
    ██║ ██╔╝██╔══██╗██║██╔══██╗╚══██╔══╝██╔════╝██║ ██╔╝██╔════╝
    █████╔╝ ██████╔╝██║██████╔╝   ██║   █████╗  █████╔╝ ███████╗
    ██╔═██╗ ██╔══██╗██║██╔═══╝    ██║   ██╔══╝  ██╔═██╗ ╚════██║
    ██║  ██╗██║  ██║██║██║        ██║   ███████╗██║  ██╗███████║
    ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝        ╚═╝   ╚══════╝╚═╝  ╚═╝╚══════╝  
                            \33[5m                
[!] \33[0m Cyber-Warrior.org | Lojistik grup \33[31m \33[5m  \33[1m 

[!] \33[0m Mikayil Ilyasov (QARAKURT) | Special thanks to Kalem_21   \33[31m \33[5m \33[1m 

[!] \33[0m illegal_coder@protonmail.com                                                             
                                                             \33[0m                                                                                                                   
\33[31m*******************************************************************\33[0m \33[1m \33[31m\33[0m """
    e = None
    d = None
    s = None
    f = None
    c = None
    h = None

    argv = sys.argv[1:]
    try:
        opts, args = getopt.getopt(argv, "e:d:s:f:c:h:",["encrypt=","decrypt=","string=","file=","command=","hash="])
    except getopt.GetoptError as error:
        
        print(banner,"\n",error,"""
        
    please use\33[31m python3 kripteks.pt -c help\33[0m command and get to help

        """)
        
        sys.exit()


    for opt, arg in opts :
        if opt in ['-e','--encrypt']:
            e = arg
        elif opt in ['-d','--decrypt'] :
            d = arg
        elif opt in ['-s','--string']:
            s = arg
        elif opt in ['-f','--file']:
            f = arg
        elif opt in ['-c','--command']:
            c = arg
        elif opt in ['-h','--hash']:
            h = arg
        

#####################################################
    if (c=="info"):
        cw_loj.info()
        sys.exit()
# Encrypt
    print(banner)
    if (e=="md5") :
       enc.md5(s,f)

    elif (e=="sha3_224") :
        enc.sha3_224(s,f)
    
    elif (e=="sha1") :
        enc.sha1(s,f)

    elif (e=="sha3_384") :
        if (s==arg) :
            enc.sha3_384(s,f)
        elif (f == arg) :
            enc.sha3_384(s,f)

    elif (e=="sha384") :
        if (s==arg) :
            enc.sha384(s,f)
        elif (f == arg) :
            enc.sha384(s,f)

    elif (e=="blake2s") :
        if (s==arg) :
            enc.blake2s(s,f)
        elif (f == arg) :
            enc.blake2s(s,f)

    elif (e=="blake2b") :
        if (s==arg) :
            enc.blake2b(s,f)
        elif (f == arg) :
            enc.blake2b(s,f)
                    
    elif (e=="sha512") :
        if (s==arg) :
            enc.sha512(s,f)
        elif (f == arg) :
            enc.sha512(s,f)

    elif (e=="sha256") :
        if (s==arg) :
            enc.sha256(s,f)
        elif (f == arg) :
            enc.sha256(s,f)   

    elif (e=="sha3_512") :
        if (s==arg) :
            enc.sha3_512(s,f)
        elif (f == arg) :
            enc.sha3_512(s,f)  

    elif (e=="sha3_256") :
        if (s==arg) :
            enc.sha3_256(s,f)
        elif (f == arg) :
            enc.sha3_256(s,f)    


    elif (e=="sha224") :
        if (s==arg) :
            enc.sha224(s,f)
        elif (f == arg) :
            enc.sha224(s,f)  

#######################################################                  
    # Decrypt
    elif (d=="md5") :
        dec.md5(h,f)
        
    elif (d=="sha3_224"):
        dec.sha3_224(h,f)

    elif (d=="sha1"):
        dec.sha1(h,f)

    elif (d=="sha3_384"):
        dec.sha3_384(h,f)

    elif (d=="sha384"):
        dec.sha384(h,f)

    elif (d=="blake2b"):
        dec.blake2b(h,f)

    elif (d=="blake2s"):
        dec.blake2s(h,f)

    elif (d=="sha224"):
        dec.sha224(h,f)

    elif (d=="sha512"):
        dec.sha512(h,f)

    elif (d=="sha256"):
        dec.sha256(h,f)

    elif (d=="sha3_512"):
        dec.sha3_512(h,f)

    elif (d=="sha3_256"):
        dec.sha3_512(h,f)

    elif (c=="hashes"):
        cw_loj.hashes()

    elif (c=="help"):
        cw_loj.help()
    
    elif (c == "settings"):
        cw_loj.settings()
operation()


