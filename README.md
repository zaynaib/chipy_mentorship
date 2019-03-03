
# Chipy Mentorship Project

I am exploring the Marvel API 

Details about Authorizing a call to the Marvel API can be found here.

https://developer.marvel.com/documentation/authorization

Resources:
Stack Overflow post about Marvel Authroization - https://stackoverflow.com/questions/28743530/you-must-provide-a-hash-error-when-using-api-to-download-data-in-r

Python timestamp - https://docs.python.org/3.3/library/datetime.html , http://timestamp.online/article/how-to-get-current-timestamp-in-python

Hash algorithms md5 - https://www.geeksforgeeks.org/md5-hash-python/ , https://docs.python.org/3/library/hashlib.html

Hiding API keys from Github - https://medium.freecodecamp.org/how-to-securely-store-api-keys-4ff3ea19ebda , https://www.slightedgecoder.com/2017/07/08/hiding-api-keys-github/ ,  https://stackoverflow.com/questions/44342276/how-to-push-code-to-github-hiding-the-api-keys

StackOverflow b string
https://stackoverflow.com/questions/6269765/what-does-the-b-character-do-in-front-of-a-string-literal

StackOverflow stings into bytes
https://stackoverflow.com/questions/7585435/best-way-to-convert-string-to-bytes-in-python-3





Authentication for Server-Side Applications
Server-side applications must pass two parameters in addition to the apikey parameter:

ts - a timestamp (or other long string which can change on a request-by-request basis)
hash - a md5 digest of the ts parameter, your private key and your public key (e.g. md5(ts+privateKey+publicKey)
For example, a user with a public key of "1234" and a private key of "abcd" could construct a valid call as follows: http://gateway.marvel.com/v1/public/comics?ts=1&apikey=1234&hash=ffd275c5130566a2916217b101f26150 (the hash value is the md5 digest of 1abcd1234)