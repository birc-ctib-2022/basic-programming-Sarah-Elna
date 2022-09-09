
# Print the pattern

a = ["*"]
b = ["*", "*"]
c = ["*", "*", "*"]
d = ["*", "*", "*", "*"]
e = ["*", "*", "*", "*", "*"]

pattern_list = [a, b, c, d, e, d, c, b, a]

for lst in pattern_list:
    print(*lst)
