import hashlib
from datetime import datetime



def md5(s=None,f=None):
    if (s != None): 
        now = datetime.now()
        time = datetime.strftime(now,"%X")
        time1 = datetime.strftime(now,"%X""_""%d""_""%m""_""%y").replace(":","_")
        time2 = time1.replace("_",":")
        hashed = hashlib.md5(s.encode('utf-8')).hexdigest()
        print("\33[36m{}\33[0m \33[32m{}\33[0m".format(time, hashed)," \33[30m\33[42m[ Encrypted ]\33[0m\33[0m \33[0m  <- {} ".format(s),"\n")
        file = open("logs/"+time2+"--md5-enc.txt","a",encoding="utf-8".format(time2))
        file.write("""
    LOG DATA :    
    [Encrypted : MD5 ] [ Date : {} ] 
    ------------------------------------------------------------

{} [>] {} """.format(now,s,hashed))
        file.close()
    elif (f != None):
        with open(f, "r" , encoding="utf-8" ) as file :
            for i in file :
                now = datetime.now()
                time = datetime.strftime(now,"%X")
                time1 = datetime.strftime(now,"%X""_""%d""_""%m""_""%y").replace(":","_")
                time2 = time1.replace("_",":")
                data = i.replace('\n','')
                hashed = hashlib.md5(data.encode('utf-8')).hexdigest()
                print("\33[36m{}\33[0m \33[32m{}\33[0m".format(time, hashed)," \33[30m\33[42m[ Encrypted ]\33[0m \33[0m \33[0m <- {} ".format(data))
                file = open("logs/"+time2+"--md5-enc.txt","a",encoding="utf-8".format(time2))
                file.write("""
            LOG DATA :    
            [Encrypted : MD5 ] [ Date : {} ] 
            ------------------------------------------------------------
{} [>] {}\n
        """.format(now,data,hashed))
            file.close()
    print("\n")
 #   
def sha3_224(s=None,f=None):
    if (s != None):
        now = datetime.now()
        time = datetime.strftime(now,"%X")
        time1 = datetime.strftime(now,"%X""_""%d""_""%m""_""%y").replace(":","_")
        time2 = time1.replace("_",":")        
        hashed = hashlib.sha3_224(s.encode('utf-8')).hexdigest()
        print("\33[36m{}\33[0m \33[32m{}\33[0m".format(time, hashed)," \33[30m\33[42m[ Encrypted ]\33[0m \33[0m \33[0m <- {} ".format(s),"\n")
        file = open("logs/"+time2+"--sha3_224-enc.txt","a",encoding="utf-8".format(time2))
        file.write("""
    LOG DATA :    
    [Encrypted : SHA3_224 ] [ Date : {} ] 
    ------------------------------------------------------------

{} [>] {} """.format(now,s,hashed))
        file.close()    

    elif (f != None):
        with open(f, "r" , encoding="utf-8" ) as file :
            for i in file :
                now = datetime.now()
                time = datetime.strftime(now,"%X")
                time1 = datetime.strftime(now,"%X""_""%d""_""%m""_""%y").replace(":","_")
                time2 = time1.replace("_",":")                  
                data = i.replace('\n','')
                hashed = hashlib.sha3_224(data.encode('utf-8')).hexdigest()
                print("\33[36m{}\33[0m \33[32m{}\33[0m".format(time, hashed)," \33[30m\33[42m[ Encrypted ]\33[0m \33[0m \33[0m <- {} ".format(data))
                file = open("logs/"+time2+"--sha3_224-enc.txt","a",encoding="utf-8".format(time2))
                file.write("""
            LOG DATA :    
            [Encrypted : SHA3_224 ] [ Date : {} ] 
            ------------------------------------------------------------
{} [>] {}\n
        """.format(now,data,hashed))
            file.close()    
    print("\n")
#
def sha1(s=None,f=None):
    if (s != None):
        now = datetime.now()
        time = datetime.strftime(now,"%X")
        time1 = datetime.strftime(now,"%X""_""%d""_""%m""_""%y").replace(":","_")
        time2 = time1.replace("_",":")              
        hashed = hashlib.sha1(s.encode('utf-8')).hexdigest()
        print("\33[36m{}\33[0m \33[32m{}\33[0m".format(time, hashed)," \33[30m\33[42m[ Encrypted ]\33[0m \33[0m \33[0m <- {} ".format(s),"\n")
        file = open("logs/"+time2+"--sha1-enc.txt","a",encoding="utf-8".format(time2))
        file.write("""
    LOG DATA :    
    [Encrypted : SHA1 ] [ Date : {} ] 
    ------------------------------------------------------------

{} [>] {} """.format(now,s,hashed))
        file.close()      
    elif (f != None):
        with open(f, "r" , encoding="utf-8" ) as file :
            for i in file :
                now = datetime.now()
                time = datetime.strftime(now,"%X")
                time1 = datetime.strftime(now,"%X""_""%d""_""%m""_""%y").replace(":","_")
                time2 = time1.replace("_",":")                 
                data = i.replace('\n','')
                hashed = hashlib.sha1(data.encode('utf-8')).hexdigest()
                print("\33[36m{}\33[0m \33[32m{}\33[0m".format(time, hashed)," \33[30m\33[42m[ Encrypted ]\33[0m \33[0m \33[0m <- {} ".format(data))
                file = open("logs/"+time2+"--sha1-enc.txt","a",encoding="utf-8".format(time2))
                file.write("""
            LOG DATA :    
            [Encrypted : SHA1 ] [ Date : {} ] 
            ------------------------------------------------------------
{} [>] {}\n
        """.format(now,data,hashed))
            file.close()     
    print("\n")
#
def sha3_384(s=None,f=None):
    if (s != None):
        now = datetime.now()
        time = datetime.strftime(now,"%X")
        time1 = datetime.strftime(now,"%X""_""%d""_""%m""_""%y").replace(":","_")
        time2 = time1.replace("_",":")            
        hashed = hashlib.sha3_384(s.encode('utf-8')).hexdigest()
        print("\33[36m{}\33[0m \33[32m{}\33[0m".format(time, hashed)," \33[30m\33[42m[ Encrypted ]\33[0m \33[0m \33[0m <- {} ".format(s),"\n")
        file = open("logs/"+time2+"--sha3_384-enc.txt","a",encoding="utf-8".format(time2))
        file.write("""
    LOG DATA :    
    [Encrypted : SHA3_384 ] [ Date : {} ] 
    ------------------------------------------------------------

{} [>] {} """.format(now,s,hashed))
        file.close()    

    elif (f != None):
        with open(f, "r" , encoding="utf-8" ) as file :
            for i in file :
                now = datetime.now()
                time = datetime.strftime(now,"%X")
                time1 = datetime.strftime(now,"%X""_""%d""_""%m""_""%y").replace(":","_")
                time2 = time1.replace("_",":")                 
                data = i.replace('\n','')
                hashed = hashlib.sha3_384(data.encode('utf-8')).hexdigest()
                print("\33[36m{}\33[0m \33[32m{}\33[0m".format(time, hashed)," \33[30m\33[42m[ Encrypted ]\33[0m \33[0m \33[0m <- {} ".format(data))
                file = open("logs/"+time2+"--sha3_384-enc.txt","a",encoding="utf-8".format(time2))
                file.write("""
            LOG DATA :    
            [Encrypted : SHA3_384 ] [ Date : {} ] 
            ------------------------------------------------------------
{} [>] {}\n
        """.format(now,data,hashed))
            file.close()      
    print("\n")
#
def sha384(s=None,f=None):
    if (s != None):
        now = datetime.now()
        time = datetime.strftime(now,"%X")
        time1 = datetime.strftime(now,"%X""_""%d""_""%m""_""%y").replace(":","_")
        time2 = time1.replace("_",":")            
        hashed = hashlib.sha384(s.encode('utf-8')).hexdigest()
        print("\33[36m{}\33[0m \33[32m{}\33[0m".format(time, hashed)," \33[30m\33[42m[ Encrypted ]\33[0m \33[0m \33[0m <- {} ".format(s),"\n")
        file = open("logs/"+time2+"--sha384-enc.txt","a",encoding="utf-8".format(time2))
        file.write("""
    LOG DATA :    
    [Encrypted : SHA384 ] [ Date : {} ] 
    ------------------------------------------------------------

{} [>] {} """.format(now,s,hashed))
        file.close()    

    elif (f != None):
        with open(f, "r" , encoding="utf-8" ) as file :
            for i in file :
                now = datetime.now()
                time = datetime.strftime(now,"%X")
                time1 = datetime.strftime(now,"%X""_""%d""_""%m""_""%y").replace(":","_")
                time2 = time1.replace("_",":")                 
                data = i.replace('\n','')
                hashed = hashlib.sha384(data.encode('utf-8')).hexdigest()
                print("\33[36m{}\33[0m \33[32m{}\33[0m".format(time, hashed)," \33[30m\33[42m[ Encrypted ]\33[0m \33[0m \33[0m <- {} ".format(data))
                file = open("logs/"+time2+"--sha384-enc.txt","a",encoding="utf-8".format(time2))
                file.write("""
            LOG DATA :    
            [Encrypted : SHA384 ] [ Date : {} ] 
            ------------------------------------------------------------
{} [>] {}\n
        """.format(now,data,hashed))
            file.close()     
    print("\n")
#
def blake2s(s=None,f=None):
    if (s != None):
        now = datetime.now()
        time = datetime.strftime(now,"%X")
        time1 = datetime.strftime(now,"%X""_""%d""_""%m""_""%y").replace(":","_")
        time2 = time1.replace("_",":")          
        hashed = hashlib.blake2s(s.encode('utf-8')).hexdigest()
        print("\33[36m{}\33[0m \33[32m{}\33[0m".format(time, hashed)," \33[30m\33[42m[ Encrypted ]\33[0m \33[0m \33[0m <- {} ".format(s),"\n")
        file = open("logs/"+time2+"--blake2s-enc.txt","a",encoding="utf-8".format(time2))
        file.write("""
    LOG DATA :    
    [Encrypted : BLAKE2S ] [ Date : {} ] 
    ------------------------------------------------------------

{} [>] {} """.format(now,s,hashed))
        file.close()     
    elif (f != None):
        now = datetime.now()
        time = datetime.strftime(now,"%X")
        time1 = datetime.strftime(now,"%X""_""%d""_""%m""_""%y").replace(":","_")
        time2 = time1.replace("_",":")          
        with open(f, "r" , encoding="utf-8" ) as file :
            for i in file :
                now = datetime.now()
                time = datetime.strftime(now,"%X")
                time1 = datetime.strftime(now,"%X""_""%d""_""%m""_""%y").replace(":","_")
                time2 = time1.replace("_",":")                 
                data = i.replace('\n','')
                hashed = hashlib.blake2s(data.encode('utf-8')).hexdigest()
                print("\33[36m{}\33[0m \33[32m{}\33[0m".format(time, hashed)," \33[30m\33[42m[ Encrypted ]\33[0m \33[0m \33[0m <- {} ".format(data))
                file = open("logs/"+time2+"--blake2s-enc.txt","a",encoding="utf-8".format(time2))
                file.write("""
            LOG DATA :    
            [Encrypted : BLAKE2S ] [ Date : {} ] 
            ------------------------------------------------------------
{} [>] {}\n
        """.format(now,data,hashed))
            file.close()    
    print("\n")
#
def sha256(s=None,f=None):
    if (s != None):
        now = datetime.now()
        time = datetime.strftime(now,"%X")
        time1 = datetime.strftime(now,"%X""_""%d""_""%m""_""%y").replace(":","_")
        time2 = time1.replace("_",":")          
        hashed = hashlib.sha256(s.encode('utf-8')).hexdigest()
        print("\33[36m{}\33[0m \33[32m{}\33[0m".format(time, hashed)," \33[30m\33[42m[ Encrypted ]\33[0m \33[0m \33[0m <- {} ".format(s),"\n")
        file = open("logs/"+time2+"--sha256-enc.txt","a",encoding="utf-8".format(time2))
        file.write("""
    LOG DATA :    
    [Encrypted : SHA256 ] [ Date : {} ] 
    ------------------------------------------------------------

{} [>] {} """.format(now,s,hashed))
        file.close()         
    elif (f != None):
        with open(f, "r" , encoding="utf-8" ) as file :
            for i in file :
                now = datetime.now()
                time = datetime.strftime(now,"%X")
                time1 = datetime.strftime(now,"%X""_""%d""_""%m""_""%y").replace(":","_")
                time2 = time1.replace("_",":")                 
                data = i.replace('\n','')
                hashed = hashlib.sha256(data.encode('utf-8')).hexdigest()
                print("\33[36m{}\33[0m \33[32m{}\33[0m".format(time, hashed)," \33[30m\33[42m[ Encrypted ]\33[0m \33[0m \33[0m <- {} ".format(data))
                file = open("logs/"+time2+"--sha256-enc.txt","a",encoding="utf-8".format(time2))
                file.write("""
            LOG DATA :    
            [Encrypted : SHA256 ] [ Date : {} ] 
            ------------------------------------------------------------
{} [>] {}\n
        """.format(now,data,hashed))
            file.close()       
    print("\n")
#
def blake2b(s=None,f=None):
    if (s != None):
        now = datetime.now()
        time = datetime.strftime(now,"%X")
        time1 = datetime.strftime(now,"%X""_""%d""_""%m""_""%y").replace(":","_")
        time2 = time1.replace("_",":")           
        hashed = hashlib.blake2b(s.encode('utf-8')).hexdigest()
        print("\33[36m{}\33[0m \33[32m{}\33[0m".format(time, hashed)," \33[30m\33[42m[ Encrypted ]\33[0m \33[0m \33[0m <- {} ".format(s),"\n")
        file = open("logs/"+time2+"--blake2b-enc.txt","a",encoding="utf-8".format(time2))
        file.write("""
    LOG DATA :    
    [Encrypted : BLAKE2B ] [ Date : {} ] 
    ------------------------------------------------------------

{} [>] {} """.format(now,s,hashed))
        file.close()            
    elif (f != None):
        with open(f, "r" , encoding="utf-8" ) as file :
            for i in file :
                now = datetime.now()
                time = datetime.strftime(now,"%X")
                time1 = datetime.strftime(now,"%X""_""%d""_""%m""_""%y").replace(":","_")
                time2 = time1.replace("_",":")                 
                data = i.replace('\n','')
                hashed = hashlib.blake2b(data.encode('utf-8')).hexdigest()
                print("\33[36m{}\33[0m \33[32m{}\33[0m".format(time, hashed)," \33[30m\33[42m[ Encrypted ]\33[0m \33[0m \33[0m <- {} ".format(data))
                file = open("logs/"+time2+"--blake2b-enc.txt","a",encoding="utf-8".format(time2))
                file.write("""
            LOG DATA :    
            [Encrypted : BLAKE2B ] [ Date : {} ] 
            ------------------------------------------------------------
{} [>] {}\n
        """.format(now,data,hashed))
            file.close()           
    print("\n")
#
def sha512(s=None,f=None):
    if (s != None):
        now = datetime.now()
        time = datetime.strftime(now,"%X")
        time1 = datetime.strftime(now,"%X""_""%d""_""%m""_""%y").replace(":","_")
        time2 = time1.replace("_",":")           
        hashed = hashlib.sha512(s.encode('utf-8')).hexdigest()
        print("\33[36m{}\33[0m \33[32m{}\33[0m".format(time, hashed)," \33[30m\33[42m[ Encrypted ]\33[0m \33[0m \33[0m <- {} ".format(s),"\n")
        file = open("logs/"+time2+"--sha512-enc.txt","a",encoding="utf-8".format(time2))
        file.write("""
    LOG DATA :    
    [Encrypted : SHA512 ] [ Date : {} ] 
    ------------------------------------------------------------

{} [>] {} """.format(now,s,hashed))
        file.close()       
    elif (f != None):
        with open(f, "r" , encoding="utf-8" ) as file :
            for i in file :
                now = datetime.now()
                time = datetime.strftime(now,"%X")
                time1 = datetime.strftime(now,"%X""_""%d""_""%m""_""%y").replace(":","_")
                time2 = time1.replace("_",":")                 
                data = i.replace('\n','')
                hashed = hashlib.sha512(data.encode('utf-8')).hexdigest()
                print("\33[36m{}\33[0m \33[32m{}\33[0m".format(time, hashed)," \33[30m\33[42m[ Encrypted ]\33[0m \33[0m \33[0m <- {} ".format(data))
                file = open("logs/"+time2+"--sha512-enc.txt","a",encoding="utf-8".format(time2))
                file.write("""
            LOG DATA :    
            [Encrypted : SHA512 ] [ Date : {} ] 
            ------------------------------------------------------------
{} [>] {}\n
        """.format(now,data,hashed))
            file.close()       
    print("\n")
#
def sha3_512(s=None,f=None):
    if (s != None):
        now = datetime.now()
        time = datetime.strftime(now,"%X")
        time1 = datetime.strftime(now,"%X""_""%d""_""%m""_""%y").replace(":","_")
        time2 = time1.replace("_",":")         
        hashed = hashlib.sha3_512(s.encode('utf-8')).hexdigest()
        print("\33[36m{}\33[0m \33[32m{}\33[0m".format(time, hashed)," \33[30m\33[42m[ Encrypted ]\33[0m \33[0m \33[0m <- {} ".format(s),"\n")
        file = open("logs/"+time2+"--sha3_512-enc.txt","a",encoding="utf-8".format(time2))
        file.write("""
    LOG DATA :    
    [Encrypted : SHA3_512 ] [ Date : {} ] 
    ------------------------------------------------------------

{} [>] {} """.format(now,s,hashed))
        file.close()       
    elif (f != None):
        with open(f, "r" , encoding="utf-8" ) as file :
            for i in file :
                now = datetime.now()
                time = datetime.strftime(now,"%X")
                time1 = datetime.strftime(now,"%X""_""%d""_""%m""_""%y").replace(":","_")
                time2 = time1.replace("_",":")                 
                data = i.replace('\n','')
                hashed = hashlib.sha3_512(data.encode('utf-8')).hexdigest()
                print("\33[36m{}\33[0m \33[32m{}\33[0m".format(time, hashed)," \33[30m\33[42m[ Encrypted ]\33[0m \33[0m \33[0m <- {} ".format(data))
                file = open("logs/"+time2+"--sha3_512-enc.txt","a",encoding="utf-8".format(time2))
                file.write("""
            LOG DATA :    
            [Encrypted : SHA3_512 ] [ Date : {} ] 
            ------------------------------------------------------------
{} [>] {}\n
        """.format(now,data,hashed))
            file.close()         
    print("\n")
#
def sha3_256(s=None,f=None):
    if (s != None):
        now = datetime.now()
        time = datetime.strftime(now,"%X")
        time1 = datetime.strftime(now,"%X""_""%d""_""%m""_""%y").replace(":","_")
        time2 = time1.replace("_",":")         
        hashed = hashlib.sha3_256(s.encode('utf-8')).hexdigest()
        print("\33[36m{}\33[0m \33[32m{}\33[0m".format(time, hashed)," \33[30m\33[42m[ Encrypted ]\33[0m \33[0m \33[0m <- {} ".format(s),"\n")
        file = open("logs/"+time2+"--sha3_256-enc.txt","a",encoding="utf-8".format(time2))
        file.write("""
    LOG DATA :    
    [Encrypted : SHA3_256 ] [ Date : {} ] 
    ------------------------------------------------------------

{} [>] {} """.format(now,s,hashed))
        file.close()      
    elif (f != None):
        with open(f, "r" , encoding="utf-8" ) as file :
            for i in file :
                now = datetime.now()
                time = datetime.strftime(now,"%X")
                time1 = datetime.strftime(now,"%X""_""%d""_""%m""_""%y").replace(":","_")
                time2 = time1.replace("_",":")                 
                data = i.replace('\n','')
                hashed = hashlib.sha3_256(data.encode('utf-8')).hexdigest()
                print("\33[36m{}\33[0m \33[32m{}\33[0m".format(time, hashed)," \33[30m\33[42m[ Encrypted ]\33[0m \33[0m \33[0m <- {} ".format(data))
                file = open("logs/"+time2+"--sha3_256-enc.txt","a",encoding="utf-8".format(time2))
                file.write("""
            LOG DATA :    
            [Encrypted : SHA3_256 ] [ Date : {} ] 
            ------------------------------------------------------------
{} [>] {}\n
        """.format(now,data,hashed))
            file.close()         
    print("\n")
#
def sha224(s=None,f=None):
    if (s != None):
        now = datetime.now()
        time = datetime.strftime(now,"%X")
        time1 = datetime.strftime(now,"%X""_""%d""_""%m""_""%y").replace(":","_")
        time2 = time1.replace("_",":")          
        hashed = hashlib.sha224(s.encode('utf-8')).hexdigest()
        print("\33[36m{}\33[0m \33[32m{}\33[0m".format(time, hashed)," \33[30m\33[42m[ Encrypted ]\33[0m \33[0m \33[0m <- {} ".format(s),"\n")
        file = open("logs/"+time2+"--sha224-enc.txt","a",encoding="utf-8".format(time2))
        file.write("""
    LOG DATA :    
    [Encrypted : SHA224 ] [ Date : {} ] 
    ------------------------------------------------------------

{} [>] {} """.format(now,s,hashed))
        file.close()   
    elif (f != None):
        with open(f, "r" , encoding="utf-8" ) as file :
            for i in file :
                now = datetime.now()
                time = datetime.strftime(now,"%X")
                time1 = datetime.strftime(now,"%X""_""%d""_""%m""_""%y").replace(":","_")
                time2 = time1.replace("_",":")                 
                data = i.replace('\n','')
                hashed = hashlib.sha224(data.encode('utf-8')).hexdigest()
                print("\33[36m{}\33[0m \33[32m{}\33[0m".format(time, hashed)," \33[30m\33[42m[ Encrypted ]\33[0m \33[0m \33[0m <- {} ".format(data))
                file = open("logs/"+time2+"--sha224-enc.txt","a",encoding="utf-8".format(time2))
                file.write("""
            LOG DATA :    
            [Encrypted : SHA224 ] [ Date : {} ] 
            ------------------------------------------------------------
{} [>] {}\n
        """.format(now,data,hashed))
            file.close()        
    print("\n")