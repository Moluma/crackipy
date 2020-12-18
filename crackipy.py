#Importamos librerias
import hashlib
import itertools as it
import string
import sys
from crack_functions import *
help = "Usage: python3 hash-cracker.py hash-type mode hashes (wordlist if necessary)\n\nHashes: md5, sha1, sha256, sha384, sha512, sha3_512, sha3_256, sha3_224\nModes: wordlist, bruteforce"
if len(sys.argv) <= 3:
    print(help)
    sys.exit(1)
#Leer y cargar hashes
hash_file = open(sys.argv[3], "r")
hashes = []
for line in hash_file:
    hashes.append(str(line.replace('\n','')))

def hash_type(type, guess):
    if type == "md5":
        return hash_md5(guess)
    elif type == "sha1":
        return hash_sha1(guess)
    elif type == "sha3_512":
        return hash_sha3_512(guess)
    elif type == "sha3_256":
        return hash_sha3_256(guess)
    elif type == "sha3_224":
        return hash_sha3_224(guess)
    elif type == "sha512":
        return hash_sha512(guess)
    elif type == "sha256":
        return hash_sha256(guess)
    elif type == "sha384":
        return hash_sha384(guess)
    else:
        print("Invalid hash type!\nValid types are: md5, sha1, sha256, sha384, sha512, sha3_512, sha3_256, sha3_224")
        sys.exit(1)

def pure_bruteforce():
    length = 1
    char_list = list(string.digits) + list(string.ascii_lowercase) + list(string.ascii_uppercase) + ['!','?','@','#','$']
    #Bucle magico de bruteforce
    while True:
        print("Bruteforcing status; round: " + str(length))
        permutations = it.product(char_list, repeat=length)
        for i in permutations:
            guess = ""
            for e in i:
                guess = str(guess) + str(e)
            cracked_hash = hash_type(sys.argv[1],(str(guess)))
            if cracked_hash in hashes:
                #Crea archivo de dump de hashes crackeados
                file.write(cracked_hash + ':' + guess + '\n')
                print("[+] Hash cracked: " + cracked_hash + ':' + guess)
                hashes.remove(cracked_hash)
                if len(hashes) == 0:
                    print("Done! :)\nSaved to " + str(file) + "!")
                    sys.exit(1)
        length = length + 1

def wordlist_bruteforce(wordlist_file):
    #Leer wordlist
    wordlist = open(wordlist_file, "r", errors="ignore")
    #Bucle bruteforce wordlist
    for line in wordlist:
        guess = line.replace('\n','')
        cracked_hash = hash_type(sys.argv[1],(str(guess)))
        if cracked_hash in hashes:
            #Crea archivo de dump de hashes crackeados
            file.write(cracked_hash + ':' + line)
            print("[+] Hash cracked: " + cracked_hash + ':' + line)
            hashes.remove(cracked_hash)
            if len(hashes) == 0:
                print("Done! :)\nSaved to " + str(file) + "!")
                sys.exit(1)
    print("[-] Wordlist exhausted! Cracked hashes were saved!")
    print("[-] Hashes left to crack: \n")
    for hash in hashes:
        print(hash+"\n")

if sys.argv[2] == "bruteforce":
    file = open("hashes.cracked", "a")
    pure_bruteforce()
elif sys.argv[2] == "wordlist":
    file = open("hashes.cracked", "a")
    wordlist_bruteforce(sys.argv[4])
else:
    print("Invalid mode! Valid ones are: bruteforce, wordlist")
