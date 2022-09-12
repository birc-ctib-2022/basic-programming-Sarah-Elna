
# Print the pattern

# my cluncky solution
# (which I love, because it is funny):

# a = ["*"]
# b = ["*", "*"]
# c = ["*", "*", "*"]
# d = ["*", "*", "*", "*"]
# e = ["*", "*", "*", "*", "*"]

# pattern_list = [a, b, c, d, e, d, c, b, a]

# for lst in pattern_list:
#     print(*lst)

# New code inspired from class code

stars = []

for _ in range(9):
    if _ <= 4:
        stars.append('*')
        print(*stars)
    elif _ > 4:
        stars.pop()
        print(*stars)