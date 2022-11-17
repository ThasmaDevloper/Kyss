
from mimetypes import init
from os import remove, system 
import platform
import subprocess
import time



#TWFkZSBieSBEYW5ueSBBbGVzc2lv
#region Functions
def enc():
    if(platform.system() == 'Windows'):
        system('cls')
    else:
        system('clear')
    print(""" 
/$$$$$$$$                                                     /$$     /$$                    
| $$_____/                                                    | $$    |__/                    
| $$       /$$$$$$$   /$$$$$$$  /$$$$$$  /$$   /$$  /$$$$$$  /$$$$$$   /$$ /$$$$$$$   /$$$$$$ 
| $$$$$   | $$__  $$ /$$_____/ /$$__  $$| $$  | $$ /$$__  $$|_  $$_/  | $$| $$__  $$ /$$__  $$
| $$__/   | $$  \ $$| $$      | $$  \__/| $$  | $$| $$  \ $$  | $$    | $$| $$  \ $$| $$  \ $$
| $$      | $$  | $$| $$      | $$      | $$  | $$| $$  | $$  | $$ /$$| $$| $$  | $$| $$  | $$
| $$$$$$$$| $$  | $$|  $$$$$$$| $$      |  $$$$$$$| $$$$$$$/  |  $$$$/| $$| $$  | $$|  $$$$$$$
|________/|__/  |__/ \_______/|__/       \____  $$| $$____/    \___/  |__/|__/  |__/ \____  $$
                                        /$$  | $$| $$                               /$$  \ $$
                                        |  $$$$$$/| $$                              |  $$$$$$/
                                        \______/ |__/                               \______/  """)

    print("Welcome in the encryption system!")
    print("What you want to Encrypt?")
    selctedtype = input("[1]File\t[2]Directory?\n>> ")
    if selctedtype == "1":
        print("Files in current dir:")
        time.sleep(1.5)
        if(platform.system() == 'Windows'):
            system('dir /A-D /B')
        else:
            system('ls -l')
        file = input("\nSelect the name of the file >>> ")
        system('gpg -c ' + file)
        print("File is successfully crypted.")
        print("Do you want to save your password?[Y/n]")
        i3 = input(">>>")
        if i3 == "Y" or i3 == "y":
            print("Please insert the password of the encrypted file!")
            passwd = input(">>>")
            f = open("backup.txt", "a")
            f.write(" | " + file + "~" + passwd + "\n")
            print("Passphrase successfully saved!")
            flushKeys()
    else:
        print("the directory you will select will be zipped!")
        time.sleep(1.5)
        print("Directory in current dir")
        time.sleep(1.5)
        if(platform.system() == 'Windows'):
            system('dir /AD')
        else:
            system('ls -l | grep "^d"')
        dir = input("\nSelect the name of the directory >> ")
        if(platform.system() == 'Windows'):
            subprocess.run(["powershell", "Compress-Archive", "-Path", dir, "-DestinationPath", dir + ".zip"])
        if(platform.system() == 'Linux'):
            system('zip -r ' + dir + '.zip ' + dir > '/dev/null')
        
        system('gpg -c ' + dir + ".zip")
        remove(dir + ".zip")
        flushKeys()
        print("Directory is successfully crypted.")
        print("Do you want to save your password?[Y/n]")
        i3 = input(">>>")
        if i3 == "Y" or i3 == "y":
            print("Please insert the password of the encrypted file!")
            passwd = input(">>>")
            f = open("backup.txt", "a")
            f.write(" | " + dir + "~" + passwd + "\n")
            print("Passphrase successfully saved!")

        
    #* <------------ Dec Function ------------->
        


        
def dec():
    if(platform.system() == 'Windows'):
        system('cls')
    else:
        system('clear')
    print(""" /$$$$$$$                                                      /$$     /$$                    
| $$__  $$                                                    | $$    |__/                    
| $$  \ $$  /$$$$$$   /$$$$$$$  /$$$$$$  /$$   /$$  /$$$$$$  /$$$$$$   /$$ /$$$$$$$   /$$$$$$ 
| $$  | $$ /$$__  $$ /$$_____/ /$$__  $$| $$  | $$ /$$__  $$|_  $$_/  | $$| $$__  $$ /$$__  $$
| $$  | $$| $$$$$$$$| $$      | $$  \__/| $$  | $$| $$  \ $$  | $$    | $$| $$  \ $$| $$  \ $$
| $$  | $$| $$_____/| $$      | $$      | $$  | $$| $$  | $$  | $$ /$$| $$| $$  | $$| $$  | $$
| $$$$$$$/|  $$$$$$$|  $$$$$$$| $$      |  $$$$$$$| $$$$$$$/  |  $$$$/| $$| $$  | $$|  $$$$$$$
|_______/  \_______/ \_______/|__/       \____  $$| $$____/    \___/  |__/|__/  |__/ \____  $$
                                         /$$  | $$| $$                               /$$  \ $$
                                        |  $$$$$$/| $$                              |  $$$$$$/
                                         \______/ |__/                               \______/ """)
    print("Welcome in the decrytpion system!")
    print("What you want to Decrypt?")
    print("Files in current dir:")
    time.sleep(1.5)
    if(platform.system() == 'Windows'):
            system('dir /A-D /B')
    else:
            system('ls -l')
    file = input("Select the file you want to decrypt >> ")

    inp = input("Insert The Passphrase. >> ")


    system('gpg --passphrase ' + inp + " " + file) 
    print("File Successfully Decrypted")





def enc_cipher():
    if(platform.system() == 'Windows'):
        system('cls')
    else:
        system('clear')
    print("""  /$$$$$$                        /$$                                  
 /$$__  $$                      | $$                                  
| $$  \__/ /$$   /$$  /$$$$$$$ /$$$$$$    /$$$$$$  /$$$$$$/$$$$       
| $$      | $$  | $$ /$$_____/|_  $$_/   /$$__  $$| $$_  $$_  $$      
| $$      | $$  | $$|  $$$$$$   | $$    | $$  \ $$| $$ \ $$ \ $$      
| $$    $$| $$  | $$ \____  $$  | $$ /$$| $$  | $$| $$ | $$ | $$      
|  $$$$$$/|  $$$$$$/ /$$$$$$$/  |  $$$$/|  $$$$$$/| $$ | $$ | $$      
 \______/  \______/ |_______/    \___/   \______/ |__/ |__/ |__/      
                                                                      
                                                                      
                                                                      """)
    print("Welcome in the Custom Encryption System!\n")
    selectedtype = input("[1]File\t[2]Directory?\n>> ")
    if selectedtype == "1":

        print("Files in current dir:")
        time.sleep(1.5)
        if(platform.system() == 'Windows'):
            system('dir')
        else:
            system('ls -l')
        file = input("Select the file >> ")


        
            
            
        print("[1]IDEA\t\t[2]3DES\n[3]CAST5\t[4]BLOWFISH\n[5]AES\t\t[6]AES192\n[7]AES256\t[8]TWOFISH\n[9]CAMELLIA128\t[10]CAMELLIA192\t[11]CAMELLIA256")
        cypher = input("Enter the encryption Cypher algo Number you prefer: ")
        isSelected = True
        
        match cypher:
            case "1":
                if platform.system()  == "Windows":
                    system('gpg --allow-old-cipher-algos --cipher-algo IDEA -c ' + file)
                    flushKeys()

                else:
                    system('gpg --allow-old-cipher-algos --cipher-algo IDEA -c ' + file)
                    flushKeys()
                
            case "2":
                if platform.system()  == "Windows":
                    system('gpg --allow-old-cipher-algos --cipher-algo 3DES -c ' + file)
                    flushKeys()
                else:
                    system('gpg --allow-old-cipher-algos --cipher-algo 3DES -c ' + file)
                    flushKeys()
                
            case "3":
                if platform.system()  == "Windows":
                    system('gpg --allow-old-cipher-algos --cipher-algo CAST5 -c ' + file)
                    flushKeys()
                else:
                    system('gpg --allow-old-cipher-algos --cipher-algo CAST5 -c ' + file)
                    flushKeys()
                
            case "4":
                if platform.system()  == "Windows":
                    system('gpg --allow-old-cipher-algos --cipher-algo BLOWFISH -c ' + file)
                    flushKeys()
                else:
                    system('gpg --allow-old-cipher-algos --cipher-algo BLOWFISH -c ' + file)
                    flushKeys()
                
            case "5":
                if platform.system()  == "Windows":
                    system('gpg --allow-old-cipher-algos --cipher-algo AES -c ' + file)
                    flushKeys()
                else:
                    system('gpg --cipher-algo AES -c ' + file)
                    flushKeys()
                
            case "6":
                if platform.system()  == "Windows":
                    system('gpg --allow-old-cipher-algos --cipher-algo AES192 -c ' + file)
                    flushKeys()
                else:
                    system('gpg --cipher-algo AES192 -c ' + file)
                    flushKeys()
                
            case "7":
                if platform.system()  == "Windows":
                    system('gpg --allow-old-cipher-algos --cipher-algo AES256 -c ' + file)
                    flushKeys()
                else:
                    system('gpg --cipher-algo AES256 -c ' + file)
                    flushKeys()
                
            case "8":
                if platform.system()  == "Windows":
                    system('gpg --allow-old-cipher-algos --cipher-algo TWOFISH -c ' + file)
                    flushKeys()
                else:
                    system('gpg --cipher-algo TWOFISH -c ' + file)
                    flushKeys()
                  
            case "9":
                if platform.system()  == "Windows":
                    system('gpg --allow-old-cipher-algos --cipher-algo CAMELLIA128 -c ' + file)
                    flushKeys()
                else:
                    system('gpg --cipher-algo CAMELLIA128 -c ' + file)
                    flushKeys()
                
            case "10":
                if platform.system()  == "Windows":
                    system('gpg --allow-old-cipher-algos --cipher-algo CAMMELLIA192 -c ' + file)
                    flushKeys()
                else:
                    system('gpg --cipher-algo CAMELLIA192 -c ' + file)
                    flushKeys()
                
            case "11":
                if platform.system()  == "Windows":
                    system('gpg --allow-old-cipher-algos --cipher-algo CAMELLIA256 -c ' + file)
                    flushKeys()
                else:
                    system('gpg --cipher-algo CAMELLIA256 -c ' + file)
                    flushKeys()
                
            case _:
                print("\nNo cipher algorithm Selected")
                end = input("\nPress Enter to continue")
                isSelected = False
                exit
        if isSelected == True:
            print("File is successfully crypted.")
            print("Do you want to save your password?[Y/n]")
            i3 = input(">>>")
            if i3 == "Y" or i3 == "y":
                print("Please insert the password of the encrypted file!")
                passwd = input(">>>")
                f = open("backup.txt", "a")
                f.write(" | " + file + "~" + passwd + "\n")
                print("Passphrase successfully saved!")
            else:
                exit
    elif selectedtype == "2":
        print("the directory you will select will be zipped!")
        time.sleep(1.5)
        print("Directory in current dir")
        time.sleep(1.5)
        if(platform.system() == 'Windows'):
            system('dir /AD')
        else:
            system('ls -l | grep "^d"')
        dir = input("\nSelect the name of the directory >> ")
        if(platform.system() == 'Windows'):
            subprocess.run(["powershell", "Compress-Archive", "-Path", dir, "-DestinationPath", dir + ".zip"])
        if(platform.system() == 'Linux'):
            system('zip -r ' + dir + '.zip ' + dir)
            if(platform.system() == 'Linux'):
                system('clear')

                
        print("[1]IDEA\t\t[2]3DES\n[3]CAST5\t[4]BLOWFISH\n[5]AES\t\t[6]AES192\n[7]AES256\t[8]TWOFISH\n[9]CAMELLIA128\t[10]CAMELLIA192\t[11]CAMELLIA256")
        cypher = input("Enter the encryption Cypher algo Number you prefer: ")
        isSelected = True
        
        
        match cypher:
            case "1":
                if platform.system()  == "Windows":
                    system('gpg --allow-old-cipher-algo --cipher-algo IDEA -c ' + dir +".zip")
                    flushKeys()
                else:
                    system('gpg --allow-old-cipher-algos --cipher-algo IDEA -c ' + dir+".zip")
                    flushKeys()
                
            case "2":
                if platform.system()  == "Windows":
                    system('gpg --allow-old-cipher-algo --cipher-algo 3DES -c ' + dir+".zip")
                    flushKeys()
                else:
                    system('gpg --allow-old-cipher-algos --cipher-algo 3DES -c ' + dir+".zip")
                    flushKeys()
                
            case "3":
                if platform.system()  == "Windows":
                    system('gpg --allow-old-cipher-algo --cipher-algo CAST5 -c ' + dir+".zip")
                    flushKeys()
                else:
                    system('gpg --allow-old-cipher-algos --cipher-algo CAST5 -c ' + dir+".zip")
                    flushKeys()
                
            case "4":
                if platform.system()  == "Windows":
                    system('gpg --allow-old-cipher-algo --cipher-algo BLOWFISH -c ' + dir+".zip")
                    flushKeys()
                else:
                    system('gpg --allow-old-cipher-algos --cipher-algo BLOWFISH -c ' + dir+".zip")
                    flushKeys()
                
            case "5":
                if platform.system()  == "Windows":
                    system('gpg --allow-old-cipher-algo --cipher-algo AES -c ' + dir+".zip")
                    flushKeys()
                else:
                    system('gpg --cipher-algo AES -c ' + dir+".zip")
                    flushKeys()
                
            case "6":
                if platform.system()  == "Windows":
                    system('gpg --allow-old-cipher-algo --cipher-algo AES192 -c ' + dir+".zip")
                    flushKeys()
                else:
                    system('gpg --cipher-algo AES192 -c ' + dir+".zip")
                    flushKeys()
                
            case "7":
                if platform.system()  == "Windows":
                    system('gpg --allow-old-cipher-algo --cipher-algo AES256 -c ' + dir+".zip")
                    flushKeys()
                else:
                    system('gpg --cipher-algo AES256 -c ' + dir+".zip")
                    flushKeys()
                
            case "8":
                if platform.system()  == "Windows":
                    system('gpg --allow-old-cipher-algo --cipher-algo TWOFISH -c ' + dir+".zip")
                    flushKeys()
                else:
                    system('gpg --cipher-algo TWOFISH -c ' + dir+".zip")
                    flushKeys()
                
            case "9":
                if platform.system()  == "Windows":
                    system('gpg --allow-old-cipher-algo --cipher-algo CAMELLIA128 -c ' + dir+".zip")
                    flushKeys()
                else:
                    system('gpg --cipher-algo CAMELLIA128 -c ' + dir +".zip")
                    flushKeys()
                
            case "10":
                if platform.system()  == "Windows":
                    system('gpg --allow-old-cipher-algo --cipher-algo CAMMELLIA192 -c ' + dir+".zip")
                    flushKeys()
                else:
                    system('gpg --cipher-algo CAMELLIA192 -c ' + dir+".zip")
                    flushKeys()
                
            case "11":
                if platform.system()  == "Windows":
                    system('gpg --allow-old-cipher-algo --cipher-algo CAMELLIA256 -c ' + dir+".zip")
                    flushKeys()
                else:
                    system('gpg --cipher-algo CAMELLIA256 -c ' + dir+".zip")
                    flushKeys()
                
            case _:
                print("No cipher algorithm Selected")
                isSelected = False
        if isSelected == True:
            print("Directory is successfully crypted.")
            print("Do you want to save your password?[Y/n]")
            i3 = input(">>>")
            if i3 == "Y" or i3 == "y":
                print("Please insert the password of the encrypted file!")
                passwd = input(">>>")
                f = open("backup.txt", "a")
                f.write(" | " + dir + ".zip" + "~" + passwd + "~" + "Directory\n")
                print("Passphrase successfully saved!")
        
def infoPage():
    if(platform.system() == 'Windows'):
        system('cls')
    else:
        system('clear')
    getInfo = True
    while(getInfo == True):
            if(platform.system() == 'Windows'):
                system('cls')
            else:
                system('clear')
            print(""" /$$$$$$            /$$$$$$          /$$$$$$$                              
|_  $$_/           /$$__  $$        | $$__  $$                             
  | $$   /$$$$$$$ | $$  \__//$$$$$$ | $$  \ $$ /$$$$$$   /$$$$$$   /$$$$$$ 
  | $$  | $$__  $$| $$$$   /$$__  $$| $$$$$$$/|____  $$ /$$__  $$ /$$__  $$
  | $$  | $$  \ $$| $$_/  | $$  \ $$| $$____/  /$$$$$$$| $$  \ $$| $$$$$$$$
  | $$  | $$  | $$| $$    | $$  | $$| $$      /$$__  $$| $$  | $$| $$_____/
 /$$$$$$| $$  | $$| $$    |  $$$$$$/| $$     |  $$$$$$$|  $$$$$$$|  $$$$$$$
|______/|__/  |__/|__/     \______/ |__/      \_______/ \____  $$ \_______/
                                                        /$$  \ $$          
                                                       |  $$$$$$/          
                                                        \______/           """)
            print("\nHello dear user, now here you can find infos about the cipher algorithms!")
            print("[1]IDEA\t\t[2]3DES\n[3]CAST5\t[4]BLOWFISH\n[5]AES\t\t[6]TWOFISH\n[7]CAMELLIA128\n[8]Exit from the InfoPage!")
            infop = input("Select the cipher algorithm you want to Know About >>> ")
            match infop:

                
                case "1":
                    print("\nIDEA uses a 128-bit key and operates on 64-bit blocks. Essentially, \nit encrypts a 64-bit block of plaintext into a 64-bit block of ciphertext.\nThis input plaintext block is divided into four subblocks of 16 bits each\nEx. ciao = nBCdLgVeBsI=")

                case "2":
                    print("\nIt works by taking three 56-bit keys (K1, K2 and K3), and encrypting first with K1, \ndecrypting next with K2 and encrypting a last time with K3. \n3DES has two-key and three-key versions. In the two-key version, \nthe same algorithm runs three times, but uses K1 for the first and last steps.")

                case "3":
                    print("\nCAST5 is a symmetric block cipher with a block-size of 8 bytes and a variable key-size of up to 128 bits. \nThe CAST5 encryption algorithm has been designed to allow a key size that can vary from 40 bits to 128 bits, \nin 8-bit increments.\nEx. ciao = 2Wo7w7qOPT8=")
                case "4":
                    print("\nBlowfish is a symmetric-key block cipher, \ndesigned in 1993 by Bruce Schneier and included in many cipher suites and encryption products. \nBlowfish provides a good encryption rate in software, and no effective cryptanalysis of it has been found to date. \nHowever, the Advanced Encryption Standard (AES) now receives more attention, and Schneier recommends Twofish for modern applications.\nEx. ciao = VNMR6agIEHo=")
                case "5":
                    
                    print("\nThe AES Encryption algorithm is a symmetric block cipher algorithm with a block/chunk size of 128 bits. \nIt converts these individual blocks using keys of 128, 192, and 256 bits.\nOnce it encrypts these blocks, it joins them together to form the ciphertext.\nEx. ciao = +3WcFbbxxO+jcAfvV2MhSQ==")

                case "6":
                    print("\nTwofish is a symmetric key block cipher with a block size of 128 bits and key sizes up to 256 bits. \nIt was one of the five finalists of the Advanced Encryption Standard contest, \nbut it was not selected for standardization. \nTwofish is related to the earlier block cipher Blowfish.")
                case "7":
                    print("\nCamellia is considered a modern, safe cipher. Even using the smaller key size option (128 bits), \nit's considered infeasible to break it by brute-force attack on the keys with current technology. \nThere are no known successful attacks that weaken the cipher considerably.")

                case "8":
                    getInfo = False
                    print("Thanks for the use!")

                case _:
                    print("No cipher algorithm Selected")
            input("Press Enter to continue...")        

    #<---------------Info zone ------------------>
def flushKeys():

    system('gpg-connect-agent reloadagent /bye > dev/null')

#endregion
#region Linux


def onLinux():
    #* <------------ Welcome ------------->
    system('clear')
    print("Hello, Welcome in the encrypt Linux system!\n")
    print(""" /$$   /$$ /$$     /$$  /$$$$$$      /$$$$$$    
| $$  /$$/|  $$   /$$/ /$$__  $$    /$$__  $$   
| $$ /$$/  \  $$ /$$/ | $$  \__/   | $$  \__/   
| $$$$$/    \  $$$$/  |  $$$$$$    |  $$$$$$    
| $$  $$     \  $$/    \____  $$    \____  $$   
| $$\  $$     | $$     /$$  \ $$    /$$  \ $$   
| $$ \  $$ /$$| $$ /$$|  $$$$$$//$$|  $$$$$$//$$
|__/  \__/|__/|__/|__/ \______/|__/ \______/|__/
                                            
""")
    print("Do you want to use the script? Press[Y/n]")
    time.sleep(1.5)
    i0 = input(">>> ")
    if i0 == 'y' or i0== 'Y':
        system('clear')
        print("""
 /$$      /$$                              
| $$$    /$$$                              
| $$$$  /$$$$  /$$$$$$  /$$$$$$$  /$$   /$$
| $$ $$/$$ $$ /$$__  $$| $$__  $$| $$  | $$
| $$  $$$| $$| $$$$$$$$| $$  \ $$| $$  | $$
| $$\  $ | $$| $$_____/| $$  | $$| $$  | $$
| $$ \/  | $$|  $$$$$$$| $$  | $$|  $$$$$$/
|__/     |__/ \_______/|__/  |__/ \______/ 
                                           
""")
        print ("\n[1]Encrypt")
        print ("[2]Decrypt")
        print ("[3]Custom Encrypting")
        print ("[4]Informations")
        i1 = input("What Service You Want To Use? >> ")
        # * <------------ Enc Function  ------------->
        
        




    #* <------------ Execute ------------->
        if i1 == "1":
            
            enc()

        if i1 == "2":
            dec()    
        if i1 == "3":
            enc_cipher()

    if i0 == "n" or i0 == "N":
        print("\nSee you Soon!")


if(platform.system() == 'Linux'):
    onLinux() 
#endregion


#region Windows

def onWindows():
    system('cls')
    print("Welcome in Windows GPG Encryption/Decryption program!\n")
    print(""" /$$   /$$ /$$     /$$  /$$$$$$      /$$$$$$    
| $$  /$$/|  $$   /$$/ /$$__  $$    /$$__  $$   
| $$ /$$/  \  $$ /$$/ | $$  \__/   | $$  \__/   
| $$$$$/    \  $$$$/  |  $$$$$$    |  $$$$$$    
| $$  $$     \  $$/    \____  $$    \____  $$   
| $$\  $$     | $$     /$$  \ $$    /$$  \ $$   
| $$ \  $$ /$$| $$ /$$|  $$$$$$//$$|  $$$$$$//$$
|__/  \__/|__/|__/|__/ \______/|__/ \______/|__/
                                          
""")
    print("Do you want to use the script? Press[Y/n]")
    modality = input(">>>")
    system('cls')
    if modality == "Y" or modality == "y":
        print("""
 /$$      /$$                              
| $$$    /$$$                              
| $$$$  /$$$$  /$$$$$$  /$$$$$$$  /$$   /$$
| $$ $$/$$ $$ /$$__  $$| $$__  $$| $$  | $$
| $$  $$$| $$| $$$$$$$$| $$  \ $$| $$  | $$
| $$\  $ | $$| $$_____/| $$  | $$| $$  | $$
| $$ \/  | $$|  $$$$$$$| $$  | $$|  $$$$$$/
|__/     |__/ \_______/|__/  |__/ \______/ 
                                           
""")
        print("What Service You Want To Use?")
        print("[1]Encrypt\n[2]Decrypt\n[3]Custom Encrypting\n[4]Informations")
        i1 = input("\n>>> ")
        if i1 == "1":
            
            enc()
        if i1 == "2":
            dec()
        if i1 == "3":
            enc_cipher()
        if i1 == "4":
            infoPage()
    if modality == "N" or modality == "n":
        print("See you soon!")


if(platform.system() == 'Windows'):
    onWindows()

