'''Nive base and NiveCrypter is created and developped by Lorenzo Piarulli'''

import random
import math
import sys


############################ NIVE BASE #############################################################
'''In this section we can find the new base 'Nive' used by the crypter'''


nive_Base = ["g" ,"&" ,"1" ,"j" ,"=" ,"?" ,"k" ,"@" ,"9" ,"l" ,"m" ,"n" ,"$" ] #13



############################ CRYPTING AND DECRYPTING ###############################################
'''In this section we can find the definitin of
the functions used by the main program to encrypt and decrypt files'''


def Crypter(s, key):                        
    orded = ""
    for i in s:
            num = ""
            t = ord(i)+key
            while t != 0:
                k = t%13
                t = t//13
                g = nive_Base[k]
                num += g
            result = num[::-1]
            orded += result
    return orded

def Decrypter(s, key):                          
    a = s 
    c = ""
    counter = 0
    num = 0
    for i in a:
        if counter == 0:
            num = nive_Base.index(i)*13
            counter += 1
        elif counter == 1:
            num += nive_Base.index(i)*1
            counter += 1    
            c += chr(num-key)
            counter = 0
            num = 0
    return c

def Layout():
    print()
    print(10*"-","WELCOME TO NIVE CRYPTOR",10*"-")
    print("created by Lorenzo Piarulli")
    print()
    print("---> Crypter (1)","---> Decrypter (2)","quit (0)", sep="\n\n")
    print()
    print("... ", end="")

def new_Wrotefile(function,par1,par2,name):
        file = open(name+".txt", "w")
        file.write(function(par1,par2))
        file.close()



###################### MAIN PROGRAM ###################################################
'''in this section we can find the main program'''



a = 1
while a == 1:
    Layout()
    syst = int(input())
    if syst == 1:
        filename = input("File name> ")
        mainText = input("Text> ")
        key1 = int(input("Key> "))
        new_Wrotefile(Crypter,mainText,key1,filename)
        print()
        print("crypted text file created in the main directory")
        print()
        print("Restart (1)", "Quit(0)", sep ="\n")
        a = int(input("..."))
    elif syst == 2:
        filename = input("File name> ")
        mainText = input("Text> ")
        key1 = int(input("Key> "))
        new_Wrotefile(Decrypter,mainText,key1,filename)
        print()
        print("decrypted text file created in the main directory")
        print()
        print("Restart (1)", "Quit(0)", sep ="\n")
        a = int(input("..."))      
    elif syst == 0:
        sys.exit()
    

            
        
    
    
