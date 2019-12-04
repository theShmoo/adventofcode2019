def isValid(p):
    digits = str(p)
    has_same = False
    same_group = 1
    prev_digit = int(digits[0])
    for d in digits[1:]:
        i = int(d)
        if i < prev_digit:
            return False
        elif i == prev_digit:
            same_group += 1
        else:
            has_same = has_same or same_group == 2
            same_group = 1

        prev_digit = i

    has_same = has_same or same_group == 2

    return has_same


i = input()
r = i.split("-")
f = int(r[0])
t = int(r[1])
c = 0

for p in range(f, t + 1):
    if isValid(p):
        c += 1

print(c)
