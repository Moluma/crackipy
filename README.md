Crackipy cracks hashes using different methods and saves them into a file for you.
Only works with ascii at the moment!

It needs some parameters such as:

- Hash-type (md5, sha1, sha256, sha384, sha512, sha3_512, sha3_256, sha3_224)
- Mode (bruteforce, wordlist)
- Hash file (1 hash per line)
- Wordlist path (if using wordlist mode)

The resultant file (cracked hashes) will be named hashes.cracked and will be formatted like this hash:password

Usage: python3 wordlistpuzzle.py

