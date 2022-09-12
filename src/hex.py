import sys

# This program should take two arguments, a command--either "encode" or "decode"--
# and then a string.

if len(sys.argv) != 3:
    print("Incorrect number of arguments.", file=sys.stderr)
    print(f"Usage: {sys.argv[0]} command string\n", file=sys.stderr)
    sys.exit(1)

command, x = sys.argv[1:3]

match command:
    case "encode":
        # Implement the encoding here
        y = []
        for c in x:
            y.append(hex(ord(c)))
        encoding = ''.join(y)
        print(encoding)

    case "decode":
        # Implement the decoding here
        y = x.split('0x')[1:]
        z = []
        for c in y:
            z.append(chr(int(c, base = 16)))
        decoding = ''.join(z)
        print(decoding)
