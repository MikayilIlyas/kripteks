import hashlib
import random
import sys
import os
import gzip
def hashes(): 
    print ("""
\33[31m \33[1mSupported hashes :\33[0m

\33[32m[1]\33[0m md5      
\33[32m[2]\33[0m sha3_224 
\33[32m[3]\33[0m sha1  
\33[32m[4]\33[0m sha3_384 
\33[32m[5]\33[0m sha384 
\33[32m[6]\33[0m blake2b 
\33[32m[7]\33[0m blake2s 
\33[32m[8]\33[0m sha512
\33[32m[9]\33[0m sha224 
\33[32m[10]\33[0m sha256
\33[32m[11]\33[0m sha3_512 
\33[32m[12]\33[0m sha3_256 

    """)
    
def help(): 
    print("""
\33[31m\33[1m\33[3mHow to use?\33[0m

\33[1mOptions :\33[0m
    \33[32m-c (--command=) : \33[0m Runs the commands written below
        \33[32mhelp : \33[0m Get to help : python3 kripter.py -c help
        \33[32mhashes : \33[0m Show supported encryption/decryption algorithms
        \33[32minfo : \33[0m Get to software information : python3 kripter.py -c info
        \33[32mframework: \33[0m Get to kripteks-framework : python3 kripter.py -c framework
        \33[32msettings : \33[0m Get to settings : python3 kripter.py -c settings 
        

    \33[1mUsage :\33[0m
    python3 kripteks.py -c help 
    or  python3 kripteks.py --command=help  

\33[1mEncryption :\33[0m
    \33[32m-e (--encrypt=) : \33[0m write the hash algoritm. (md5,sha1,sha224 and ... [-c hashes])
    \33[32m-s (--string=) : \33[0m Add the word you want to encrypt here.
    \33[32m-f (--file=) : \33[0m Add the text file you want to encrypt here. (This is supported only .txt)

    \33[1mUsage :\33[0m
    python3 kripteks.py -e [algorithm] -s [string]
    python3 kripteks.py -e [algorithm] -f [file.txt]

\33[1mDecryption :\33[0m
    \33[32m-d (--decrypt=) : \33[0m write the hash algoritm. (md5,sha1,sha224 and ...[-c hashes])
    \33[32m-h (--hash=) : \33[0m Add encrypted text you want decrypt here. 
    \33[32m-f (--file=) : \33[0m Add your wordlist (This is supported only .txt)

    \33[1mUsage :\33[0m
    python3 kripteks.py -d [algorithm] -h [hashed_string] -f [wordlist.txt]
    or python3 kripteks.py --decrypt=[algorithm] --hash=[hashed_string] --file=[wordlist.txt]

*******************************************************************\33[0m 


""")



def info():
    print("""
    \33[32m\33[1m
                                                  
               .-:-.`                             
           `:+o/.                                 
         -+oo+.       ..`                         
       -oooo-     `-/:`      ``                   
     `+soso.    `:o/`     `. ```:.  `             
    .ososo.    .oo:        .      `/o-            
   -ossos-    .os+         `.       .` `          
  .oosooo    `ooo-            `--    `/.          
  +sssss/    -soo.        `-/ooo`     `-          
 .ssssso:    :soo-    .-/ososso- ..   ``          
 :sossso/    :ooo+.:+ooo+/--oo/    ````    `      
 /sssssso`   .osssso+:.`  `+oo`           .-      
 :ossssss:    /o/:.       :oo-           -+`      
 .oosssoso.              .os/          .+o.    `  
  +ssssssso.             +so`      `-/os+`    `:  
  .ossssssso:           :soo+++++ooooo+-     .+.  
   -ossssssos+.        .ossssoooso+/-`     `/o-   
    -osssssssss+-`      `.......`        ./oo-    
     .+sssssssssoo/-.                `-/ooo+.     
      `:ososssssssssso+/:-......--:/oossoo-       
        `:oossssssssssssssssosossssosos+-`        
           .:+oossssssssssssssssssso+:.           
              `-:+oooosssssooooo/:-`              
                    `..----..`  \33[0m

    \33[32m\33[1m[\33[0m     \33[32m\33[1m\33[5mCyber-Warrior.org | Lojistik Group\33[0m     \33[32m\33[1m] \33[0m           
        
\33[1m\33[31mKripteks\33[0m is an open source software that performs operations such as Encryption / Decryption with certain encryption algorithms.  
This software working is only Linux 

\33[31m\33[1m\33[3mInformation...\33[0m 

\33[32m\33[1m [>] Coded by : \33[0m Mikayil Ilyasov (QARAKURT) | Azerbaijani Coder
\33[32m\33[1m [>] Contact  : \33[0m illegal_coder[at]protonmail.com
\33[32m\33[1m [>] Website  : \33[0m Cyber-Warrior.org | Turkish Cyber Army
\33[32m\33[1m [>] Our mission  : \33[0m https://www.cyber-warrior.org/Misyon.asp
\33[32m\33[1m [>] Message to all : \33[0mNe mutlu Turkum diyene! Respects to all \33[4mTurkish\33[0m and \33[4mAzerbaijani\33[0m hackers. 
\33[32m\33[1m [>] Special thanks : \33[0m Thanks to all Cyber-Warrior mmembers and special thanks to my Master \33[1m\33[3mKalem_21\33[0m
\33[32m\33[1m [>] Loves    : \33[0m To \33[37m\33[1m\33[33m GALATA\33[31mSARAY
\33[32m\33[1m [>] Github   : \33[0m https://github.com/MikayilIlyas/kripteks
\33[32m\33[1m [>] Youtube  : \33[0m https://youtu.be/-tq5V07UXXc



\33[31m*******************************************************************\33[0m""")


def settings():
    print("\33[31m\33[1mSelect the work\33[0m")
    print("""
\33[32m[1]\33[0m Install Wordlist        
\33[32m[2]\33[0m Clear logs
\33[32m[3]\33[0m Make wordlist (in the next update)
\33[32m[4]\33[0m Change banner (in the next update)
\33[32m[0]\33[0m Exit

***********************************\n""")
    command = input("\33[36m\33[1mkrpt> \33[0m")   
    if (command =="1"):
        
        print("\33[32mSelect the wordlist")
        print("""
---------------------------------------------------------------
\33[32m[1]\33[0m hashesorg2019                    [\33[1m12.79 GB]\33[0m       
\33[32m[2]\33[0m weakpass_2a                      [\33[1m85.44 GB] \33[0m 
\33[32m[3]\33[0m weakpass_2                       [\33[1m28.44 GB]  \33[0m
\33[32m[4]\33[0m HashesOrg                        [\33[1m4.14 GB]  \33[0m
\33[32m[5]\33[0m Rockyou                          [\33[1m133.44 Mb]  \33[0m
\33[32m[6]\33[0m DCHTPassv1.0                     [\33[1m22.84 GB]  \33[0m
\33[32m[7]\33[0m Md5decrypt-awesome-wordlist      [\33[1m19.63 GB]  \33[0m
\33[32m[8]\33[0m Crackstation                     [\33[1m14.62 GB]  \33[0m
\33[32m[9]\33[0m breachcompilation                [\33[1m8.98 GB]  \33[0m


\33[32m[0]\33[0m Back 
        """)
        while True :
            c = input("\33[36m\33[1mkrpt> \33[0m")   
            if (c=="1"):
                
                print("\33[31m hashesorg2019 wordlist downloading...\33[m\n")
                os.system('cd wordlist && wget https://download.weakpass.com/wordlists/1851/hashesorg2019.gz')
                print("\33[31m\n---------  \n Download completed. ")
            elif (c == "2"):
                print("\33[31m weakpass_2a wordlist downloading...\33[m\n")
                os.system("cd wordlist && wget https://download.weakpass.com/wordlists/1919/weakpass_2a.gz")
                print("\33[31m\n---------  \n Download completed. ")
            elif (c == "3"):
                print("\33[31m weakpass_2 wordlist downloading...\33[m\n")
                os.system("cd wordlist && wget https://download.weakpass.com/wordlists/1863/weakpass_2.gz")
                print("\33[31m\n---------  \n Download completed. ")        
            elif (c == "4"):
                print("\33[31m HashesOrg wordlist downloading...\33[m\n")
                os.system("cd wordlist && wget https://download.weakpass.com/wordlists/1802/HashesOrg.gz")
                print("\33[31m\n---------  \n Download completed. ")
            elif (c == "5"):
                print("\33[31m Rockyou wordlist downloading...\33[m\n")
                os.system("cd wordlist && wget https://download.weakpass.com/wordlists/90/rockyou.txt.gz")
                os.system('gzip -d wordlist/rockyou.txt.gz')
                print("\33[31m\n---------  \n Download completed. ")
            elif (c == "6"):
                print("\33[31m DCHTPassv1.0 wordlist downloading...\33[m\n")
                os.system("cd wordlist && wget https://download.weakpass.com/wordlists/1257/DCHTPassv1.0.txt.gz")
                print("\33[31m\n---------  \n Download completed. ")
            elif (c == "7"):
                print("\33[31m Md5decrypt-awesome-wordlist  downloading...\33[m\n")
                os.system("cd wordlist && wget https://download.weakpass.com/wordlists/1319/Md5decrypt-awesome-wordlist.gz")
                print("\33[31m\n---------  \n Download completed. ")
            elif (c == "8"):
                print("\33[31m Crackstation wordlist downloading...\33[m\n")
                os.system("cd wordlist && wget https://download.weakpass.com/wordlists/725/crackstation.txt.gz")
                print("\33[31m\n---------  \n Download completed. ")
            elif (c == "9"):
                print("\33[31m breachcompilation wordlist downloading...\33[m\n")
                os.system("cd wordlist && wget https://download.weakpass.com/wordlists/1849/breachcompilation.txt.gz")
                print("\33[31m\n---------  \n Download completed. ")
            elif (c == "0"):
                settings()
            else :
                print("\n\33[31mOps! False command  \n\33[0m")
    if (command == "2"):
        print("\33[33mYour logs \n---------\33[0m")
        os.system("cd logs && ls -l")

        dele = input("\n\33[33mAre you want delete all logs? [Y/n]  \33[0m")
        dele_c = ["Y","y","n","N"]
        if (dele == "y" or "Y"):
            os.system('rm -r logs')
            os.system('mkdir logs')
            print("\n\33[31mAll logs cleared...  \33[0m\n")
        elif (dele == "n" or "N"):
            ("\n\33[33mCancelled  \33[0m")
            settings()
    if (command == "0"):
        sys.exit()
