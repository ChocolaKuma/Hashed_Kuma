import os     #for os control
import shutil #for dir make and destruction
import random
import distutils.dir_util
import pickle
import hashlib
import time
import urllib.request

UpDate = False

if(UpDate==True):
    urllib.request.urlretrieve ("https://raw.githubusercontent.com/ChocolaKuma/Kuma_Hash/master/rawPassword.txt", "sys/rawPassword.txt")
    urllib.request.urlretrieve ("https://raw.githubusercontent.com/ChocolaKuma/Kuma_Hash/master/cryptPassword.txt", "sys/cryptPassword.txt")

    
time_start = time.time()

def value_lookup(LookupNum,raw,crypt):
    print(raw[LookupNum]," : ", crypt[LookupNum])
    
def one_hash(key_string,Crypt_type="MD5"):
    if(Crypt_type=="MD5"):
        key_string = key_string.encode('utf-8')
        e_pass = hashlib.md5(key_string).hexdigest()
    return e_pass

def list_hash(r_passwordlist):
    out = []
    for x in r_passwordlist:
        e_passwordlist = one_hash(x)
        out.append(e_passwordlist)
    return out

def write_Pickle_array(loc,array_out):
    with open(loc, "wb") as fp:   #Pickling "/sys/rawPassword.txt"
        pickle.dump(array_out, fp)
        
def read_Pickle_array(loc):
    with open(loc, "rb") as fp:   # Unpickling
        b = pickle.load(fp)
        return b

def ReadRawToArray(InputLoc):
    lines = []
    with open(InputLoc) as file:
        for line in file:
            line = line.strip() #or someother preprocessing
            lines.append(line)
    return lines

def main():
    raw = []
    crypt = []
    print("Start ")
    raw = ReadRawToArray("RawWordList/EveryWordInEnglish.txt")
    crypt = list_hash(raw)
    print("End")
    i = 0
    while(i<109583): #109583
        print(raw[i],":",crypt[i])
        i=i+1

    #print(one_hash("google",Crypt_type="MD5"),"\n\n")
    #value_lookup(0)
    #write_array("sys/cryptPassword.txt",E_passwordlist)

    



main()
#write_array("sys/rawPassword.txt",raw)
#write_array("sys/cryptPassword.txt",crypt)
print("\n\n\n\nTime to Complete:",time.time()-time_start,"Secs")


