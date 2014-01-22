mip
===

A simple password generator using cryptographic hash functions.

### How it works

```
new_password = hash(paint, secret_keyphrase, secret_file)[:32]
```

The hash function returns uses sha512 and the result is encoded in base64.

### Sample use

Uses a simple command line utility. Example session :
```
me@mycomputer:~$ mip
locker: 
locker (again): 
paint: login@example.com
ZTc1MDkwNzY3YjU2M2FmZjYyNGI1OWY3
paint: 
```
Note: The user did enter his secret secret passphrase after "locker:", but it is not displayed.
