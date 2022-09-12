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
            y.append(ord(c))
        z = ''.join(y)
        encoding = z
        print(encoding)

    case "decode":
        # Implement the decoding here
        x.split('0x')
        for c in x:
            decode += int(c, base = 16)
        decode [1:-1] = decoding
        print(decoding)
