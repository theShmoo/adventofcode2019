hold = input()
base = [0, 1, 0, -1]
arepeats = 100
# for _ in range(arepeats):
#     new = ""
#     for i in range(1, len(hold) + 1):
#         offset = 0
#         curloc = 0
#         val = 0
#         for j in hold:
#             offset += 1
#             if offset == i:
#                 offset = 0
#                 curloc += 1
#                 if curloc == 4:
#                     curloc = 0
#             val += int(j) * base[curloc]
#         new += str(val)[-1]
#     hold = new
# print(hold[:8])
time = int(hold[0:7])
print(time)
print(len(hold) * 10000)
print(len(hold) * 10000 - time)
size = len(hold) * 10000 - time
extra = -1 * size % len(hold)
print(extra)
repeats = size // len(hold)
print(repeats)
new = list(hold[extra:])
for _ in range(repeats):
    new.extend(list(hold))
print(len(new))

for b in range(arepeats):
    print(b)
    temp = [0] * len(new)
    cursum = 0
    for i in range(len(new) - 1, -1, -1):
        cursum += int(new[i])
        cursum = cursum % 10
        temp[i] = cursum
    new = temp[:]
print(new[0:8])
