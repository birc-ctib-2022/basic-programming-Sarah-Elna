import sys

if len(sys.argv) != 2:
    print(f"{sys.argv[0]} expected exactly one argument.")
    sys.exit(1)

password = sys.argv[1]
is_valid = False

# Do all the requirement checks here.

##At least 1 letter between [a-z] and 1 letter between [A-Z]. You can use the methods a.islower() and a.isupper() to check if the letter a is one of these.

##At least 1 number between [0-9]. You can use the method a.isnumeric() for this.

##At least 1 character from [$#@]; (a in "$#@" will test if a is one of these).

if len(password) > 16 or len(password) <= 6:
    lowercase = False
    uppercase = False
    numbers = False
    special = False
    for c in password:
        if c.islower() == True:
            lowercase = True
        if c.uppercase() == True:
            uppercase = True
        if c.isnumeric() == True:
            numbers = True
        if c in "$#@":
            special = True
    if lowercase == True and uppercase == True and numbers == True and special == True:
        is_valid = True

print(is_valid)
