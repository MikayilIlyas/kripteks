
import hashlib
from datetime import datetime
import enc



def md5(h=None,f=None):
       if (h != None and f != None):
              with open(f, "r" , encoding="utf-8" ) as file :
                     for i in file :
                            now = datetime.now()
                            time = datetime.strftime(now,"%X")
                            time1 = datetime.strftime(now,"%X""_""%d""_""%m""_""%y").replace(":","_")
                            time2 = time1.replace("_",":")
                            data = i.replace('\n','')
                            hashed = hashlib.md5(data.encode('utf-8')).hexdigest()
                            ok = "\33[30m\33[41mFalse"
                            if (hashed == h) :
                                   ok = "\33[30m\33[42mTrue "
                                   print("\33[36m{}\33[0m \33[32m{}\33[0m".format(time, hashed)," \33[30m\33[42m[",ok,"\33[30m\33[42m""]\33[0m <- {} \n".format(data)) 
                                   file = open("logs/"+time2+"--md5-dec.txt","a",encoding="utf-8".format(time2))
                                   file.write("""
   LOG DATA :    
   [Decrypted : MD5 ] [ Date : {} ] [ Wordlist : {} ]
   ----------------------------------------------------------------------------------------------------

   {} [>] {} """.format(now,f,h,data))
                                   file.close()                                      
                                   break      
                            print("\33[36m{}\33[0m \33[32m{}\33[0m".format(time, hashed)," \33[30m\33[41m[",ok,"\33[30m\33[41m""]\33[0m <- {} ".format(data))
                             
#
def sha3_224(h=None,f=None):
       if (h != None and f != None):
              with open(f, "r" , encoding="utf-8" ) as file :
                     for i in file :
                            now = datetime.now()
                            time = datetime.strftime(now,"%X")
                            time1 = datetime.strftime(now,"%X""_""%d""_""%m""_""%y").replace(":","_")
                            time2 = time1.replace("_",":")                            
                            data = i.replace('\n','')
                            hashed = hashlib.sha3_224(data.encode('utf-8')).hexdigest()
                            ok = "\33[30m\33[41mFalse"
                            if (hashed == h) :
                                   ok = "\33[30m\33[42mTrue "
                                   print("\33[36m{}\33[0m \33[32m{}\33[0m".format(time, hashed)," \33[30m\33[42m[",ok,"\33[30m\33[42m""]\33[0m <- {} \n".format(data)) 
                                   file = open("logs/"+time2+"--sha3_224-dec.txt","a",encoding="utf-8".format(time2))
                                   file.write("""
   LOG DATA :    
   [Decrypted : SHA3_224 ] [ Date : {} ] [ Wordlist : {} ]
   ----------------------------------------------------------------------------------------------------

   {} [>] {} """.format(now,f,h,data))
                                   file.close()                                  
                                   break      
                            print("\33[36m{}\33[0m \33[32m{}\33[0m".format(time, hashed)," \33[30m\33[41m[",ok,"\33[30m\33[41m""]\33[0m <- {} ".format(data))   
#
def sha1(h=None,f=None):
       if (h != None and f != None):
              with open(f, "r" , encoding="utf-8" ) as file :
                     for i in file :
                            now = datetime.now()
                            time = datetime.strftime(now,"%X")
                            time1 = datetime.strftime(now,"%X""_""%d""_""%m""_""%y").replace(":","_")
                            time2 = time1.replace("_",":")                            
                            data = i.replace('\n','')
                            hashed = hashlib.sha1(data.encode('utf-8')).hexdigest()
                            ok = "\33[30m\33[41mFalse"
                            if (hashed == h) :
                                   ok = "\33[30m\33[42mTrue "
                                   print("\33[36m{}\33[0m \33[32m{}\33[0m".format(time, hashed)," \33[30m\33[42m[",ok,"\33[30m\33[42m""]\33[0m <- {} \n".format(data)) 
                                   file = open("logs/"+time2+"--sha1-dec.txt","a",encoding="utf-8".format(time2))
                                   file.write("""
   LOG DATA :    
   [Decrypted : SHA1 ] [ Date : {} ] [ Wordlist : {} ]
   ----------------------------------------------------------------------------------------------------

   {} [>] {} """.format(now,f,h,data))
                                   file.close()                                    
                                   break      
                            print("\33[36m{}\33[0m \33[32m{}\33[0m".format(time, hashed)," \33[30m\33[41m[",ok,"\33[30m\33[41m""]\33[0m <- {} ".format(data))
#
def sha3_384(h=None,f=None):
       if (h != None and f != None):
              with open(f, "r" , encoding="utf-8" ) as file :
                     for i in file :
                            now = datetime.now()
                            time = datetime.strftime(now,"%X")
                            time1 = datetime.strftime(now,"%X""_""%d""_""%m""_""%y").replace(":","_")
                            time2 = time1.replace("_",":")                            
                            data = i.replace('\n','')
                            hashed = hashlib.sha3_384(data.encode('utf-8')).hexdigest()
                            ok = "\33[30m\33[41mFalse"
                            if (hashed == h) :
                                   ok = "\33[30m\33[42mTrue "
                                   print("\33[36m{}\33[0m \33[32m{}\33[0m".format(time, hashed)," \33[30m\33[42m[",ok,"\33[30m\33[42m""]\33[0m <- {} \n".format(data))
                                   file = open("logs/"+time2+"--md5-dec.txt","a",encoding="utf-8".format(time2))
                                   file.write("""
   LOG DATA :    
   [Decrypted : MD5 ] [ Date : {} ] [ Wordlist : {} ]
   ----------------------------------------------------------------------------------------------------

   {} [>] {} """.format(now,f,h,data))
                                   file.close()                                    
                                   break
                            print("\33[36m{}\33[0m \33[32m{}\33[0m".format(time, hashed)," \33[30m\33[41m[",ok,"\33[30m\33[41m""]\33[0m <- {} ".format(data))
#
def sha384(h=None,f=None):
       if (h != None and f != None):
              with open(f, "r" , encoding="utf-8" ) as file :
                     for i in file :
                            now = datetime.now()
                            time = datetime.strftime(now,"%X")
                            time1 = datetime.strftime(now,"%X""_""%d""_""%m""_""%y").replace(":","_")
                            time2 = time1.replace("_",":")                            
                            data = i.replace('\n','')
                            hashed = hashlib.sha384(data.encode('utf-8')).hexdigest()
                            ok = "\33[30m\33[41mFalse"
                            if (hashed == h) :
                                   ok = "\33[30m\33[42mTrue "
                                   print("\33[36m{}\33[0m \33[32m{}\33[0m".format(time, hashed)," \33[30m\33[42m[",ok,"\33[30m\33[42m""]\33[0m <- {} \n".format(data))
                                   file = open("logs/"+time2+"--sha384-dec.txt","a",encoding="utf-8".format(time2))
                                   file.write("""
   LOG DATA :    
   [Decrypted : SHA3844 ] [ Date : {} ] [ Wordlist : {} ]
   ----------------------------------------------------------------------------------------------------

   {} [>] {} """.format(now,f,h,data))
                                   file.close()                                  
                                   break
                            print("\33[36m{}\33[0m \33[32m{}\33[0m".format(time, hashed)," \33[30m\33[41m[",ok,"\33[30m\33[41m""]\33[0m <- {} ".format(data))
#
def blake2b(h=None,f=None):
       if (h != None and f != None):
              with open(f, "r" , encoding="utf-8" ) as file :
                     for i in file :
                            now = datetime.now()
                            time = datetime.strftime(now,"%X")
                            time1 = datetime.strftime(now,"%X""_""%d""_""%m""_""%y").replace(":","_")
                            time2 = time1.replace("_",":")                            
                            data = i.replace('\n','')
                            hashed = hashlib.blake2b(data.encode('utf-8')).hexdigest()
                            ok = "\33[30m\33[41mFalse"
                            if (hashed == h) :
                                   ok = "\33[30m\33[42mTrue "
                                   print("\33[36m{}\33[0m \33[32m{}\33[0m".format(time, hashed)," \33[30m\33[42m[",ok,"\33[30m\33[42m""]\33[0m <- {} \n".format(data))
                                   file = open("logs/"+time2+"--blake2b-dec.txt","a",encoding="utf-8".format(time2))
                                   file.write("""
   LOG DATA :    
   [Decrypted : BLAKE2B ] [ Date : {} ] [ Wordlist : {} ]
   ----------------------------------------------------------------------------------------------------

   {} [>] {} """.format(now,f,h,data))
                                   file.close()                                    
                                   break
                            print("\33[36m{}\33[0m \33[32m{}\33[0m".format(time, hashed)," \33[30m\33[41m[",ok,"\33[30m\33[41m""]\33[0m <- {} ".format(data))
#
def blake2s(h=None,f=None):
       if (h != None and f != None):
              with open(f, "r" , encoding="utf-8" ) as file :
                     for i in file :
                            now = datetime.now()
                            time = datetime.strftime(now,"%X")
                            time1 = datetime.strftime(now,"%X""_""%d""_""%m""_""%y").replace(":","_")
                            time2 = time1.replace("_",":")                            
                            data = i.replace('\n','')
                            hashed = hashlib.blake2s(data.encode('utf-8')).hexdigest()
                            ok = "\33[30m\33[41mFalse"
                            if (hashed == h) :
                                   ok = "\33[30m\33[42mTrue "
                                   print("\33[36m{}\33[0m \33[32m{}\33[0m".format(time, hashed)," \33[30m\33[42m[",ok,"\33[30m\33[42m""]\33[0m <- {} \n".format(data))
                                   file = open("logs/"+time2+"--blake2s-dec.txt","a",encoding="utf-8".format(time2))
                                   file.write("""
   LOG DATA :    
   [Decrypted : BLAKE2S ] [ Date : {} ] [ Wordlist : {} ]
   ----------------------------------------------------------------------------------------------------

   {} [>] {} """.format(now,f,h,data))
                                   file.close()                                   
                                   break
                            print("\33[36m{}\33[0m \33[32m{}\33[0m".format(time, hashed)," \33[30m\33[41m[",ok,"\33[30m\33[41m""]\33[0m <- {} ".format(data))
#
def sha224(h=None,f=None):
       if (h != None and f != None):
              with open(f, "r" , encoding="utf-8" ) as file :
                     for i in file :
                            now = datetime.now()
                            time = datetime.strftime(now,"%X")
                            time1 = datetime.strftime(now,"%X""_""%d""_""%m""_""%y").replace(":","_")
                            time2 = time1.replace("_",":")                            
                            data = i.replace('\n','')
                            hashed = hashlib.sha224(data.encode('utf-8')).hexdigest()
                            ok = "\33[30m\33[41mFalse"
                            if (hashed == h) :
                                   ok = "\33[30m\33[42mTrue "
                                   print("\33[36m{}\33[0m \33[32m{}\33[0m".format(time, hashed)," \33[30m\33[42m[",ok,"\33[30m\33[42m""]\33[0m <- {} \n".format(data))
                                   file = open("logs/"+time2+"--sha224-dec.txt","a",encoding="utf-8".format(time2))
                                   file.write("""
   LOG DATA :    
   [Decrypted : SHA224 ] [ Date : {} ] [ Wordlist : {} ]
   ----------------------------------------------------------------------------------------------------

   {} [>] {} """.format(now,f,h,data))
                                   file.close()                                   
                                   break
                            print("\33[36m{}\33[0m \33[32m{}\33[0m".format(time, hashed)," \33[30m\33[41m[",ok,"\33[30m\33[41m""]\33[0m <- {} ".format(data))
#
def sha512(h=None,f=None):
       if (h != None and f != None):
              with open(f, "r" , encoding="utf-8" ) as file :
                     for i in file :
                            now = datetime.now()
                            time = datetime.strftime(now,"%X")
                            time1 = datetime.strftime(now,"%X""_""%d""_""%m""_""%y").replace(":","_")
                            time2 = time1.replace("_",":")                            
                            data = i.replace('\n','')
                            hashed = hashlib.sha512(data.encode('utf-8')).hexdigest()
                            ok = "\33[30m\33[41mFalse"
                            if (hashed == h) :
                                   ok = "\33[30m\33[42mTrue "
                                   print("\33[36m{}\33[0m \33[32m{}\33[0m".format(time, hashed)," \33[30m\33[42m[",ok,"\33[30m\33[42m""]\33[0m <- {} \n".format(data))
                                   file = open("logs/"+time2+"--sha512-dec.txt","a",encoding="utf-8".format(time2))
                                   file.write("""
   LOG DATA :    
   [Decrypted : SHA512 ] [ Date : {} ] [ Wordlist : {} ]
   ----------------------------------------------------------------------------------------------------

   {} [>] {} """.format(now,f,h,data))
                                   file.close()                                    
                                   break
                            print("\33[36m{}\33[0m \33[32m{}\33[0m".format(time, hashed)," \33[30m\33[41m[",ok,"\33[30m\33[41m""]\33[0m <- {} ".format(data))
#                            
def sha256(h=None,f=None):
       if (h != None and f != None):
              with open(f, "r" , encoding="utf-8" ) as file :
                     for i in file :
                            now = datetime.now()
                            time = datetime.strftime(now,"%X")
                            time1 = datetime.strftime(now,"%X""_""%d""_""%m""_""%y").replace(":","_")
                            time2 = time1.replace("_",":")                            
                            data = i.replace('\n','')
                            hashed = hashlib.sha256(data.encode('utf-8')).hexdigest()
                            ok = "\33[30m\33[41mFalse"
                            if (hashed == h) :
                                   ok = "\33[30m\33[42mTrue "
                                   print("\33[36m{}\33[0m \33[32m{}\33[0m".format(time, hashed)," \33[30m\33[42m[",ok,"\33[30m\33[42m""]\33[0m <- {} \n".format(data))
                                   file = open("logs/"+time2+"--sha256-dec.txt","a",encoding="utf-8".format(time2))
                                   file.write("""
   LOG DATA :    
   [Decrypted : SHA256 ] [ Date : {} ] [ Wordlist : {} ]
   ----------------------------------------------------------------------------------------------------

   {} [>] {} """.format(now,f,h,data))
                                   file.close()                                    
                                   break
                            print("\33[36m{}\33[0m \33[32m{}\33[0m".format(time, hashed)," \33[30m\33[41m[",ok,"\33[30m\33[41m""]\33[0m <- {} ".format(data))#
#
def sha3_512(h=None,f=None):
       if (h != None and f != None):
              with open(f, "r" , encoding="utf-8" ) as file :
                     for i in file :
                            now = datetime.now()
                            time = datetime.strftime(now,"%X")
                            time1 = datetime.strftime(now,"%X""_""%d""_""%m""_""%y").replace(":","_")
                            time2 = time1.replace("_",":")                            
                            data = i.replace('\n','')
                            hashed = hashlib.sha3_512(data.encode('utf-8')).hexdigest()
                            ok = "\33[30m\33[41mFalse"
                            if (hashed == h) :
                                   ok = "\33[30m\33[42mTrue "
                                   print("\33[36m{}\33[0m \33[32m{}\33[0m".format(time, hashed)," \33[30m\33[42m[",ok,"\33[30m\33[42m""]\33[0m <- {} \n".format(data))
                                   file = open("logs/"+time2+"--sha3_512-dec.txt","a",encoding="utf-8".format(time2))
                                   file.write("""
   LOG DATA :    
   [Decrypted : SHA3_512 ] [ Date : {} ] [ Wordlist : {} ]
   ----------------------------------------------------------------------------------------------------

   {} [>] {} """.format(now,f,h,data))
                                   file.close()                                    
                                   break
                            print("\33[36m{}\33[0m \33[32m{}\33[0m".format(time, hashed)," \33[30m\33[41m[",ok,"\33[30m\33[41m""]\33[0m <- {} ".format(data))
#
def sha3_256(h=None,f=None):
       if (h != None and f != None):
              with open(f, "r" , encoding="utf-8" ) as file :
                     for i in file :
                            now = datetime.now()
                            time = datetime.strftime(now,"%X")
                            time1 = datetime.strftime(now,"%X""_""%d""_""%m""_""%y").replace(":","_")
                            time2 = time1.replace("_",":")                            
                            data = i.replace('\n','')
                            hashed = hashlib.sha3_256(data.encode('utf-8')).hexdigest()
                            ok = "\33[30m\33[41mFalse"
                            if (hashed == h) :
                                   ok = "\33[30m\33[42mTrue "
                                   print("\33[36m{}\33[0m \33[32m{}\33[0m".format(time, hashed)," \33[30m\33[42m[",ok,"\33[30m\33[42m""]\33[0m <- {} \n".format(data))
                                   file = open("logs/"+time2+"--sha3_256-dec.txt","a",encoding="utf-8".format(time2))
                                   file.write("""
   LOG DATA :    
   [Decrypted : SHA3_256 ] [ Date : {} ] [ Wordlist : {} ]
   ----------------------------------------------------------------------------------------------------

   {} [>] {} """.format(now,f,h,data))
                                   file.close()                                  
                                   break
                            print("\33[36m{}\33[0m \33[32m{}\33[0m".format(time, hashed)," \33[30m\33[41m[",ok,"\33[30m\33[41m""]\33[0m <- {} ".format(data))
